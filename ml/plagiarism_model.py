"""Training and inference helpers for plagiarism type classifiers."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import joblib
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin, clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

LABELS = ("TYPE_I", "TYPE_II", "TYPE_III", "TYPE_IV")
LABEL_DISPLAY = {
    "TYPE_I": "Tipo I: copia casi exacta",
    "TYPE_II": "Tipo II: cambios de nombres/literales",
    "TYPE_III": "Tipo III: cambios estructurales parciales",
    "TYPE_IV": "Tipo IV: misma idea con implementación distinta",
}

FEATURE_SETS = {
    "family": [
        "score_lexical",
        "score_syntactic",
        "score_structural",
        "score_stochastic",
        "score_semantic",
    ],
    "core": [
        "lexical_edit",
        "lexical_jaccard",
        "raw_edit",
        "raw_jaccard",
        "ast_sequence",
        "control_profile",
        "cyclomatic",
        "nesting_depth",
        "markov_js",
        "entropy",
        "semantic_normalized_ast",
    ],
}


def load_training_data(csv_path: Path, feature_set: str = "all") -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Load the supervised metrics table as X/y arrays."""
    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        rows = list(csv.DictReader(csv_file))

    if not rows:
        raise ValueError(f"No rows found in {csv_path}")

    if feature_set == "all":
        feature_names = [column for column in rows[0] if column != "label"]
    else:
        feature_names = FEATURE_SETS[feature_set]

    x = np.array([[float(row[name]) for name in feature_names] for row in rows], dtype=float)
    y = np.array([row["label"] for row in rows])
    return x, y, feature_names


def build_classifier(kind: str) -> object:
    """Build a supported multiclass classifier."""
    if kind == "logistic":
        return Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    LogisticRegression(
                        class_weight="balanced",
                        max_iter=3000,
                        random_state=42,
                        solver="liblinear",
                    ),
                ),
            ]
        )
    if kind == "forest":
        return RandomForestClassifier(
            class_weight="balanced",
            max_depth=5,
            min_samples_leaf=2,
            n_estimators=300,
            random_state=42,
        )
    if kind == "specialists":
        return SpecialistEnsemble()
    raise ValueError(f"Unsupported classifier: {kind}")


@dataclass
class FoldResult:
    accuracy: float
    macro_f1: float
    confusion: np.ndarray


class SpecialistEnsemble(BaseEstimator, ClassifierMixin):
    """One binary classifier per plagiarism type, combined by confidence."""

    def __init__(self, labels: Iterable[str] = LABELS) -> None:
        self.labels = tuple(labels)
        self.models: dict[str, Pipeline] = {}
        self.classes_ = np.array(self.labels)

    def _base_model(self) -> Pipeline:
        return Pipeline(
            [
                ("scaler", StandardScaler()),
                (
                    "classifier",
                    LogisticRegression(
                        class_weight="balanced",
                        max_iter=3000,
                        random_state=42,
                        solver="liblinear",
                    ),
                ),
            ]
        )

    def fit(self, x: np.ndarray, y: np.ndarray) -> "SpecialistEnsemble":
        self.models = {}
        for label in self.labels:
            binary_y = np.array([1 if value == label else 0 for value in y])
            model = self._base_model()
            model.fit(x, binary_y)
            self.models[label] = model
        return self

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        scores = []
        for label in self.labels:
            model = self.models[label]
            label_scores = model.predict_proba(x)[:, 1]
            scores.append(label_scores)
        probabilities = np.vstack(scores).T
        totals = probabilities.sum(axis=1, keepdims=True)
        return np.divide(probabilities, totals, out=np.zeros_like(probabilities), where=totals != 0)

    def predict(self, x: np.ndarray) -> np.ndarray:
        probabilities = self.predict_proba(x)
        return np.array([self.labels[index] for index in probabilities.argmax(axis=1)])


def cross_validate_model(model: object, x: np.ndarray, y: np.ndarray, folds: int) -> FoldResult:
    splitter = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)
    predictions = np.empty_like(y)

    for train_index, test_index in splitter.split(x, y):
        fold_model = clone(model)
        fold_model.fit(x[train_index], y[train_index])
        predictions[test_index] = fold_model.predict(x[test_index])

    return FoldResult(
        accuracy=accuracy_score(y, predictions),
        macro_f1=f1_score(y, predictions, average="macro"),
        confusion=confusion_matrix(y, predictions, labels=list(LABELS)),
    )


def evaluate_models(
    x: np.ndarray,
    y: np.ndarray,
    folds: int = 5,
    candidates: Iterable[str] = ("logistic", "forest", "specialists"),
) -> dict[str, FoldResult]:
    return {
        candidate: cross_validate_model(build_classifier(candidate), x, y, folds)
        for candidate in candidates
    }


def select_best_model(results: dict[str, FoldResult]) -> str:
    return max(results, key=lambda name: (results[name].macro_f1, results[name].accuracy))


def train_final_model(
    x: np.ndarray,
    y: np.ndarray,
    feature_names: list[str],
    kind: str,
    output_path: Path,
    feature_set: str,
) -> dict[str, object]:
    model = build_classifier(kind)
    model.fit(x, y)
    artifact = {
        "model": model,
        "model_kind": kind,
        "labels": list(LABELS),
        "label_display": LABEL_DISPLAY,
        "feature_names": feature_names,
        "feature_set": feature_set,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(artifact, output_path)
    return artifact
