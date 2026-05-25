"""Predict the plagiarism type for two Python files or snippets."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import numpy as np

from metrics import extract_all_metrics
from ml.plagiarism_model import LABEL_DISPLAY


def read_code(value: str) -> str:
    path = Path(value)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Predict plagiarism type for a pair of Python programs.")
    parser.add_argument("--code-a", required=True, help="First code snippet or path.")
    parser.add_argument("--code-b", required=True, help="Second code snippet or path.")
    parser.add_argument(
        "--model",
        default="models/plagiarism_model.joblib",
        help="Model artifact created by train_models.py.",
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable output.")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    artifact = joblib.load(args.model)
    metrics = extract_all_metrics(read_code(args.code_a), read_code(args.code_b))
    feature_names = artifact["feature_names"]
    x = np.array([[float(metrics[name]) for name in feature_names]], dtype=float)

    model = artifact["model"]
    prediction = str(model.predict(x)[0])
    probabilities = model.predict_proba(x)[0]
    labels = list(artifact["labels"])
    model_classes = [str(label) for label in getattr(model, "classes_", labels)]
    raw_probability_by_label = {
        label: float(probabilities[index]) for index, label in enumerate(model_classes)
    }
    probability_by_label = {label: raw_probability_by_label.get(label, 0.0) for label in labels}
    confidence = probability_by_label[prediction]

    payload = {
        "prediction": prediction,
        "description": artifact.get("label_display", LABEL_DISPLAY).get(prediction, prediction),
        "confidence": confidence,
        "probabilities": probability_by_label,
        "model_kind": artifact["model_kind"],
        "hybrid_score": metrics["hybrid_score"],
        "family_scores": {
            "lexical": metrics["score_lexical"],
            "syntactic": metrics["score_syntactic"],
            "structural": metrics["score_structural"],
            "stochastic": metrics["score_stochastic"],
            "semantic": metrics["score_semantic"],
        },
    }

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
        return

    print("Plagiarism type prediction")
    print("=" * 26)
    print(f"Prediction: {payload['description']}")
    print(f"Confidence: {confidence:.3f}")
    print(f"Model: {payload['model_kind']}")
    print(f"Hybrid score: {metrics['hybrid_score']:.3f}")
    print()
    print("Probabilities")
    for label, value in sorted(probability_by_label.items()):
        description = artifact.get("label_display", LABEL_DISPLAY).get(label, label)
        print(f"{label:<8} {value:.3f}  {description}")
    print()
    print("Family scores")
    for name, value in payload["family_scores"].items():
        print(f"{name:<10} {value:.3f}")


if __name__ == "__main__":
    main()
