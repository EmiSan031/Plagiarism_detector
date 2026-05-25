"""Train and evaluate plagiarism type classifiers."""

from __future__ import annotations

import argparse
from pathlib import Path

from ml import evaluate_models, load_training_data, train_final_model
from ml.plagiarism_model import LABELS, select_best_model


def format_confusion(confusion: object) -> str:
    rows = ["              pred " + " ".join(f"{label:>8}" for label in LABELS)]
    for label, values in zip(LABELS, confusion):
        rows.append(f"true {label:>8} " + " ".join(f"{int(value):8d}" for value in values))
    return "\n".join(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate multiclass and specialist plagiarism type models."
    )
    parser.add_argument(
        "--input",
        default="dataset/training_metrics.csv",
        help="CSV produced by build_training_table.py.",
    )
    parser.add_argument(
        "--output",
        default="models/plagiarism_model.joblib",
        help="Path where the trained model artifact will be saved.",
    )
    parser.add_argument(
        "--feature-set",
        choices=["all", "family", "core"],
        default="core",
        help="Feature group used for training.",
    )
    parser.add_argument("--folds", type=int, default=5, help="Stratified CV folds.")
    parser.add_argument(
        "--model",
        choices=["auto", "logistic", "forest", "specialists"],
        default="auto",
        help="Model to train. auto chooses the best macro-F1 from evaluation.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    x, y, feature_names = load_training_data(Path(args.input), args.feature_set)
    results = evaluate_models(x, y, folds=args.folds)

    print("Plagiarism model evaluation")
    print("=" * 28)
    print(f"Rows: {len(y)}")
    print(f"Features: {len(feature_names)} ({args.feature_set})")
    print(f"Folds: {args.folds}")
    print()

    for name, result in sorted(results.items(), key=lambda item: item[1].macro_f1, reverse=True):
        print(f"{name:<12} accuracy={result.accuracy:.3f} macro_f1={result.macro_f1:.3f}")

    selected = select_best_model(results) if args.model == "auto" else args.model
    print()
    print(f"Selected model: {selected}")
    print(format_confusion(results[selected].confusion))

    train_final_model(
        x=x,
        y=y,
        feature_names=feature_names,
        kind=selected,
        output_path=Path(args.output),
        feature_set=args.feature_set,
    )
    print()
    print(f"Saved artifact: {args.output}")


if __name__ == "__main__":
    main()
