"""Train and evaluate plagiarism type classifiers."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from ml import evaluate_models, feature_importance, load_training_data, train_final_model
from ml.evaluation_report import (
    ReportMetadata,
    format_html_report,
    format_terminal_details,
    format_terminal_summary,
)
from ml.plagiarism_model import select_best_model


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
        choices=["auto", "logistic", "forest", "forest_refined", "specialists", "hierarchical"],
        default="auto",
        help="Model to train. auto chooses the best macro-F1 from evaluation.",
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="Print full per-model tables and confusion matrices in the terminal.",
    )
    parser.add_argument(
        "--top-features",
        type=int,
        default=12,
        help="Number of feature importances to print in the terminal summary.",
    )
    parser.add_argument(
        "--report",
        default="reports/plagiarism_evaluation.html",
        help="Path for the HTML evaluation report.",
    )
    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip writing the HTML evaluation report file.",
    )
    parser.add_argument(
        "--color",
        choices=["auto", "always", "never"],
        default="auto",
        help="Colorize terminal output. auto enables color only for an interactive terminal.",
    )
    return parser


def use_terminal_color(color_mode: str) -> bool:
    return color_mode == "always" or (color_mode == "auto" and sys.stdout.isatty())


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    if not args.no_report and Path(args.report).suffix.lower() not in {".html", ".htm"}:
        parser.error("--report must point to an .html or .htm file")

    x, y, feature_names = load_training_data(Path(args.input), args.feature_set)
    results = evaluate_models(x, y, folds=args.folds)
    selected = select_best_model(results) if args.model == "auto" else args.model

    artifact = train_final_model(
        x=x,
        y=y,
        feature_names=feature_names,
        kind=selected,
        output_path=Path(args.output),
        feature_set=args.feature_set,
    )
    importances = feature_importance(artifact["model"], feature_names)
    metadata = ReportMetadata(
        rows_count=len(y),
        feature_count=len(feature_names),
        feature_set=args.feature_set,
        folds=args.folds,
    )

    colors = use_terminal_color(args.color)
    print(
        format_terminal_summary(
            results=results,
            selected=selected,
            importances=importances,
            metadata=metadata,
            top_features=args.top_features,
            colors=colors,
        )
    )

    if args.details:
        print()
        print(format_terminal_details(results, colors=colors))

    if not args.no_report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            format_html_report(
                results=results,
                selected=selected,
                importances=importances,
                metadata=metadata,
            ),
            encoding="utf-8",
        )
        print()
        print(f"Full HTML report: {report_path}")

    print()
    print(f"Saved artifact: {args.output}")


if __name__ == "__main__":
    main()
