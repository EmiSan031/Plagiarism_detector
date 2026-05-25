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
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_recall_fscore_support
from sklearn.model_selection import StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

LABELS = ("NO_PLAGIO", "TYPE_I", "TYPE_II", "TYPE_III", "TYPE_IV")
LABEL_DISPLAY = {
    "NO_PLAGIO": "No plagio detectado",
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
        "statement_count",
        "function_count",
        "return_count",
        "call_count",
        "assignment_count",
        "branch_count",
        "loop_count",
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
    if kind == "forest_refined":
        return TypeIIIIVRefinedClassifier()
    if kind == "specialists":
        return SpecialistEnsemble()
    raise ValueError(f"Unsupported classifier: {kind}")


@dataclass
class FoldResult:
    accuracy: float
    macro_f1: float
    confusion: np.ndarray
    per_class: dict[str, dict[str, float]]
    one_vs_rest_confusion: dict[str, dict[str, int]]


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


class TypeIIIIVRefinedClassifier(BaseEstimator, ClassifierMixin):
    """Multiclass forest with a binary refinement for TYPE_III vs TYPE_IV."""

    def __init__(self, labels: Iterable[str] = LABELS) -> None:
        self.labels = tuple(labels)
        self.base_model = RandomForestClassifier(
            class_weight="balanced",
            max_depth=5,
            min_samples_leaf=2,
            n_estimators=300,
            random_state=42,
        )
        self.refiner = RandomForestClassifier(
            class_weight="balanced",
            max_depth=4,
            min_samples_leaf=2,
            n_estimators=200,
            random_state=84,
        )
        self.classes_ = np.array(self.labels)

    def fit(self, x: np.ndarray, y: np.ndarray) -> "TypeIIIIVRefinedClassifier":
        self.base_model.fit(x, y)
        mask = np.isin(y, ["TYPE_III", "TYPE_IV"])
        if np.sum(mask) > 0:
            binary_y = np.array([1 if value == "TYPE_IV" else 0 for value in y[mask]])
            self.refiner.fit(x[mask], binary_y)
        return self

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        base_classes = [str(label) for label in self.base_model.classes_]
        base_probabilities = self.base_model.predict_proba(x)
        probabilities = np.zeros((x.shape[0], len(self.labels)))

        for label_index, label in enumerate(self.labels):
            if label in base_classes:
                probabilities[:, label_index] = base_probabilities[:, base_classes.index(label)]

        type_iii_index = self.labels.index("TYPE_III")
        type_iv_index = self.labels.index("TYPE_IV")
        type_total = probabilities[:, type_iii_index] + probabilities[:, type_iv_index]
        refined = self.refiner.predict_proba(x)
        type_iv_probability = refined[:, 1]
        probabilities[:, type_iii_index] = type_total * (1.0 - type_iv_probability)
        probabilities[:, type_iv_index] = type_total * type_iv_probability

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

    precision, recall, f1, support = precision_recall_fscore_support(
        y,
        predictions,
        labels=list(LABELS),
        zero_division=0,
    )
    per_class = {
        label: {
            "precision": float(precision[index]),
            "recall": float(recall[index]),
            "f1": float(f1[index]),
            "support": float(support[index]),
        }
        for index, label in enumerate(LABELS)
    }
    one_vs_rest_confusion = {}
    for label in LABELS:
        true_positive = int(np.sum((y == label) & (predictions == label)))
        false_positive = int(np.sum((y != label) & (predictions == label)))
        false_negative = int(np.sum((y == label) & (predictions != label)))
        true_negative = int(np.sum((y != label) & (predictions != label)))
        one_vs_rest_confusion[label] = {
            "tp": true_positive,
            "fp": false_positive,
            "fn": false_negative,
            "tn": true_negative,
        }

    return FoldResult(
        accuracy=accuracy_score(y, predictions),
        macro_f1=f1_score(y, predictions, average="macro"),
        confusion=confusion_matrix(y, predictions, labels=list(LABELS)),
        per_class=per_class,
        one_vs_rest_confusion=one_vs_rest_confusion,
    )


def evaluate_models(
    x: np.ndarray,
    y: np.ndarray,
    folds: int = 5,
    candidates: Iterable[str] = ("logistic", "forest", "forest_refined", "specialists"),
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


def feature_importance(model: object, feature_names: list[str], limit: int = 12) -> list[tuple[str, float]]:
    candidate = model
    if isinstance(candidate, TypeIIIIVRefinedClassifier):
        candidate = candidate.base_model
    if isinstance(candidate, Pipeline):
        classifier = candidate.named_steps.get("classifier")
        if hasattr(classifier, "coef_"):
            weights = np.mean(np.abs(classifier.coef_), axis=0)
            return sorted(zip(feature_names, weights), key=lambda item: item[1], reverse=True)[:limit]
    if hasattr(candidate, "feature_importances_"):
        return sorted(
            zip(feature_names, candidate.feature_importances_),
            key=lambda item: item[1],
            reverse=True,
        )[:limit]
    return []
