"""Build a supervised-learning table from the code-pair dataset."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from metrics import extract_all_metrics

DATASET_LABELS = {
    "type_1": "TYPE_I",
    "type_2": "TYPE_II",
    "type_3": "TYPE_III",
    "type_4": "TYPE_IV",
}

INTERNAL_COLUMNS = ["pair_id", "code_a_path", "code_b_path"]


def discover_pairs(dataset_dir: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for folder_name, label in DATASET_LABELS.items():
        clone_dir = dataset_dir / folder_name
        if not clone_dir.exists():
            continue

        files_a = sorted(clone_dir.glob("pair_*_a.py"))
        for code_a_path in files_a:
            pair_number = code_a_path.stem.removeprefix("pair_").removesuffix("_a")
            code_b_path = clone_dir / f"pair_{pair_number}_b.py"
            if not code_b_path.exists():
                raise FileNotFoundError(f"Missing pair file: {code_b_path}")

            rows.append(
                {
                    "pair_id": f"{folder_name}_pair_{pair_number}",
                    "code_a_path": str(code_a_path.as_posix()),
                    "code_b_path": str(code_b_path.as_posix()),
                    "label": label,
                }
            )

    return rows


def build_metric_row(pair: dict[str, str]) -> dict[str, str | float]:
    code_a = Path(pair["code_a_path"]).read_text(encoding="utf-8")
    code_b = Path(pair["code_b_path"]).read_text(encoding="utf-8")
    metrics = extract_all_metrics(code_a, code_b)
    return {**pair, **metrics}


def write_training_table(dataset_dir: Path, output_path: Path) -> list[dict[str, str | float]]:
    pairs = discover_pairs(dataset_dir)
    if not pairs:
        raise ValueError(f"No code pairs found in {dataset_dir}")

    rows = [build_metric_row(pair) for pair in pairs]
    metric_columns = sorted(
        column for column in rows[0] if column not in [*INTERNAL_COLUMNS, "label"]
    )
    fieldnames = [*metric_columns, "label"]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({column: row[column] for column in fieldnames})

    return [{column: row[column] for column in fieldnames} for row in rows]


def summarize(rows: list[dict[str, str | float]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        label = str(row["label"])
        counts[label] = counts.get(label, 0) + 1
    return counts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a CSV table with clone-detection metrics and labels."
    )
    parser.add_argument(
        "--dataset-dir",
        default="dataset",
        help="Directory containing type_1, type_2, type_3 and type_4 folders.",
    )
    parser.add_argument(
        "--output",
        default="dataset/training_metrics.csv",
        help="CSV output path.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    rows = write_training_table(Path(args.dataset_dir), Path(args.output))
    counts = summarize(rows)

    print(f"Generated table: {args.output}")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(rows[0])}")
    for label, count in sorted(counts.items()):
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
