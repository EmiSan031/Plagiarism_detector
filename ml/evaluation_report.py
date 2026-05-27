"""Terminal and HTML reporting helpers for model evaluation results."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
import html

from ml.plagiarism_model import LABELS

RESET = "\033[0m"
COLORS = {
    "bold": "\033[1m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "red": "\033[31m",
    "cyan": "\033[36m",
}


@dataclass(frozen=True)
class ReportMetadata:
    rows_count: int
    feature_count: int
    feature_set: str
    folds: int


def color_text(text: str, color: str, enabled: bool) -> str:
    if not enabled:
        return text
    return f"{COLORS[color]}{text}{RESET}"


def color_best_metric(value: float, best_value: float, enabled: bool) -> str:
    text = f"{value:.3f}"
    if value == best_value:
        return color_text(text, "green", enabled)
    return text


def color_data_metric(value: float, enabled: bool) -> str:
    return color_text(f"{value:.3f}", "cyan", enabled)


def color_count(value: int, enabled: bool) -> str:
    text = f"{value:>5d}"
    if value >= 5:
        return color_text(text, "red", enabled)
    return color_text(text, "yellow", enabled)


def macro_metric(result: object, metric: str) -> float:
    return sum(result.per_class[label][metric] for label in LABELS) / len(LABELS)


def ranked_results(results: dict[str, object]) -> list[tuple[str, object]]:
    return sorted(results.items(), key=lambda item: item[1].macro_f1, reverse=True)


def format_confusion(confusion: object) -> str:
    rows = ["              pred " + " ".join(f"{label:>8}" for label in LABELS)]
    for label, values in zip(LABELS, confusion):
        rows.append(f"true {label:>8} " + " ".join(f"{int(value):8d}" for value in values))
    return "\n".join(rows)


def format_per_class(result: object) -> str:
    rows = ["type       precision  recall  f1     support"]
    for label in LABELS:
        metrics = result.per_class[label]
        rows.append(
            f"{label:<10} "
            f"{metrics['precision']:.3f}      "
            f"{metrics['recall']:.3f}   "
            f"{metrics['f1']:.3f}  "
            f"{int(metrics['support']):7d}"
        )
    return "\n".join(rows)


def format_one_vs_rest_confusion(result: object) -> str:
    rows = []
    for label in LABELS:
        values = result.one_vs_rest_confusion[label]
        rows.extend(
            [
                f"{label} vs REST",
                "                 pred label  pred rest",
                f"true label       {values['tp']:10d} {values['fn']:10d}",
                f"true rest        {values['fp']:10d} {values['tn']:10d}",
            ]
        )
    return "\n".join(rows)


def format_model_ranking(results: dict[str, object], selected: str, colors: bool = False) -> str:
    rows = [
        color_text("Model ranking", "bold", colors),
        "rank  model           accuracy  precision  recall  macro_f1",
    ]
    best_accuracy = max(result.accuracy for result in results.values())
    best_precision = max(macro_metric(result, "precision") for result in results.values())
    best_recall = max(macro_metric(result, "recall") for result in results.values())
    best_f1 = max(result.macro_f1 for result in results.values())

    for index, (name, result) in enumerate(ranked_results(results), start=1):
        marker = color_text(" selected", "green", colors) if name == selected else ""
        precision = macro_metric(result, "precision")
        recall = macro_metric(result, "recall")
        rows.append(
            f"{index:>4}  {name:<14} "
            f"{color_best_metric(result.accuracy, best_accuracy, colors)}     "
            f"{color_best_metric(precision, best_precision, colors)}      "
            f"{color_best_metric(recall, best_recall, colors)}   "
            f"{color_best_metric(result.macro_f1, best_f1, colors)}{marker}"
        )
    return "\n".join(rows)


def format_class_performance(
    result: object,
    title: str = "Selected model class performance",
    colors: bool = False,
) -> str:
    rows = [
        color_text(title, "bold", colors),
        "class      precision  recall  f1     support",
    ]
    for label in LABELS:
        metrics = result.per_class[label]
        rows.append(
            f"{label:<10} "
            f"{color_data_metric(metrics['precision'], colors)}      "
            f"{color_data_metric(metrics['recall'], colors)}   "
            f"{color_data_metric(metrics['f1'], colors)}  "
            f"{int(metrics['support']):7d}"
        )
    return "\n".join(rows)


def misclassification_rows(result: object) -> list[tuple[str, str, int]]:
    rows = []
    for true_index, true_label in enumerate(LABELS):
        for pred_index, pred_label in enumerate(LABELS):
            if true_index == pred_index:
                continue
            count = int(result.confusion[true_index][pred_index])
            if count:
                rows.append((true_label, pred_label, count))
    return sorted(rows, key=lambda item: item[2], reverse=True)


def format_misclassifications(result: object, limit: int = 5, colors: bool = False) -> str:
    rows = [color_text("Most common misclassifications", "bold", colors)]
    mistakes = misclassification_rows(result)[:limit]
    if not mistakes:
        rows.append(color_text("No cross-class mistakes found.", "green", colors))
        return "\n".join(rows)

    rows.append("true class  predicted class  cases")
    for true_label, pred_label, count in mistakes:
        rows.append(f"{true_label:<10} {pred_label:<15} {color_count(count, colors)}")
    return "\n".join(rows)


def format_feature_importance(
    importances: Iterable[tuple[str, float]],
    limit: int,
    colors: bool = False,
) -> str:
    rows = [color_text("Top feature importance", "bold", colors)]
    for feature, value in list(importances)[:limit]:
        rows.append(f"{feature:<32} {color_text(f'{value:.4f}', 'cyan', colors)}")
    return "\n".join(rows)


def format_terminal_summary(
    results: dict[str, object],
    selected: str,
    importances: list[tuple[str, float]],
    metadata: ReportMetadata,
    top_features: int,
    colors: bool,
) -> str:
    sections = [
        color_text("Plagiarism model evaluation", "bold", colors),
        "=" * 28,
        f"Rows: {metadata.rows_count}",
        f"Features: {metadata.feature_count} ({metadata.feature_set})",
        f"Folds: {metadata.folds}",
        "",
        format_model_ranking(results, selected, colors=colors),
        "",
        format_class_performance(results[selected], colors=colors),
        "",
        format_misclassifications(results[selected], colors=colors),
    ]
    if importances:
        sections.extend(["", format_feature_importance(importances, top_features, colors=colors)])
    return "\n".join(sections)


def format_terminal_details(results: dict[str, object], colors: bool) -> str:
    sections = [
        color_text("Detailed model evaluation", "bold", colors),
        "=" * 25,
    ]
    for name, result in ranked_results(results):
        sections.extend(
            [
                "",
                f"{name:<12} accuracy={result.accuracy:.3f} macro_f1={result.macro_f1:.3f}",
                format_per_class(result),
                "",
                format_confusion(result.confusion),
                "",
                format_one_vs_rest_confusion(result),
            ]
        )
    return "\n".join(sections)


def html_attrs(**attrs: str) -> str:
    return "".join(f' {name}="{html.escape(value, quote=True)}"' for name, value in attrs.items() if value)


def html_cell(value: object, tag: str = "td", class_name: str = "") -> str:
    return f"<{tag}{html_attrs(**{'class': class_name})}>{html.escape(str(value))}</{tag}>"


def html_metric(value: float, class_name: str = "") -> str:
    classes = " ".join(item for item in ("metric", class_name) if item)
    return html_cell(f"{value:.3f}", class_name=classes)


def html_model_ranking(results: dict[str, object], selected: str) -> str:
    best_accuracy = max(result.accuracy for result in results.values())
    best_precision = max(macro_metric(result, "precision") for result in results.values())
    best_recall = max(macro_metric(result, "recall") for result in results.values())
    best_f1 = max(result.macro_f1 for result in results.values())
    rows = [
        "<table>",
        "<thead><tr>"
        + "".join(
            html_cell(header, "th")
            for header in ["Rank", "Model", "Accuracy", "Precision", "Recall", "Macro F1", "Status"]
        )
        + "</tr></thead>",
        "<tbody>",
    ]
    for index, (name, result) in enumerate(ranked_results(results), start=1):
        precision = macro_metric(result, "precision")
        recall = macro_metric(result, "recall")
        rows.append(
            "<tr>"
            + html_cell(index)
            + html_cell(name, class_name="model-name")
            + html_metric(result.accuracy, "best" if result.accuracy == best_accuracy else "")
            + html_metric(precision, "best" if precision == best_precision else "")
            + html_metric(recall, "best" if recall == best_recall else "")
            + html_metric(result.macro_f1, "best" if result.macro_f1 == best_f1 else "")
            + html_cell("selected" if name == selected else "", class_name="selected")
            + "</tr>"
        )
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def html_class_performance(result: object) -> str:
    rows = [
        "<table>",
        "<thead><tr>"
        + "".join(html_cell(header, "th") for header in ["Class", "Precision", "Recall", "F1", "Support"])
        + "</tr></thead>",
        "<tbody>",
    ]
    for label in LABELS:
        metrics = result.per_class[label]
        rows.append(
            "<tr>"
            + html_cell(label, class_name="model-name")
            + html_metric(metrics["precision"], "neutral")
            + html_metric(metrics["recall"], "neutral")
            + html_metric(metrics["f1"], "neutral")
            + html_cell(int(metrics["support"]))
            + "</tr>"
        )
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def html_misclassifications(result: object, limit: int) -> str:
    mistakes = misclassification_rows(result)[:limit]
    if not mistakes:
        return '<p class="empty">No cross-class mistakes found.</p>'

    rows = [
        "<table>",
        "<thead><tr>"
        + "".join(html_cell(header, "th") for header in ["True class", "Predicted class", "Cases"])
        + "</tr></thead>",
        "<tbody>",
    ]
    for true_label, pred_label, count in mistakes:
        class_name = "mistake-high" if count >= 5 else "mistake-low"
        rows.append(
            "<tr>"
            + html_cell(true_label, class_name="model-name")
            + html_cell(pred_label)
            + html_cell(count, class_name=class_name)
            + "</tr>"
        )
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def html_confusion_matrix(result: object) -> str:
    rows = [
        "<table>",
        "<thead><tr><th>True \\ Pred</th>" + "".join(html_cell(label, "th") for label in LABELS) + "</tr></thead>",
        "<tbody>",
    ]
    for true_label, values in zip(LABELS, result.confusion):
        row = [html_cell(true_label, "th")]
        row.extend(html_cell(int(value)) for value in values)
        rows.append("<tr>" + "".join(row) + "</tr>")
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def html_one_vs_rest(result: object) -> str:
    rows = []
    for label in LABELS:
        values = result.one_vs_rest_confusion[label]
        rows.extend(
            [
                f"<h4>{html.escape(label)} vs REST</h4>",
                '<table class="small-table">',
                "<thead><tr><th></th><th>Pred label</th><th>Pred rest</th></tr></thead>",
                "<tbody>",
                "<tr><th>True label</th>" + html_cell(values["tp"]) + html_cell(values["fn"]) + "</tr>",
                "<tr><th>True rest</th>" + html_cell(values["fp"]) + html_cell(values["tn"]) + "</tr>",
                "</tbody></table>",
            ]
        )
    return "\n".join(rows)


def html_feature_importance(importances: list[tuple[str, float]]) -> str:
    if not importances:
        return '<p class="empty">No feature importance available for this model.</p>'

    max_value = max(value for _, value in importances)
    rows = [
        "<table>",
        "<thead><tr><th>Feature</th><th>Importance</th><th>Weight</th></tr></thead>",
        "<tbody>",
    ]
    for feature, value in importances:
        width = 0 if max_value == 0 else round((value / max_value) * 100, 1)
        rows.append(
            "<tr>"
            + html_cell(feature, class_name="model-name")
            + html_metric(value, "neutral")
            + f'<td><div class="bar-track"><div class="bar-fill" style="width: {width}%"></div></div></td>'
            + "</tr>"
        )
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def html_model_section(name: str, result: object) -> str:
    return f"""
    <section class="panel">
      <h2>{html.escape(name)}</h2>
      <div class="metric-grid">
        <div><span>Accuracy</span><strong>{result.accuracy:.3f}</strong></div>
        <div><span>Macro precision</span><strong>{macro_metric(result, "precision"):.3f}</strong></div>
        <div><span>Macro recall</span><strong>{macro_metric(result, "recall"):.3f}</strong></div>
        <div><span>Macro F1</span><strong>{result.macro_f1:.3f}</strong></div>
      </div>
      <h3>Class performance</h3>
      {html_class_performance(result)}
      <h3>Most common misclassifications</h3>
      {html_misclassifications(result, limit=len(LABELS) * (len(LABELS) - 1))}
      <h3>Confusion matrix</h3>
      {html_confusion_matrix(result)}
      <details>
        <summary>One-vs-rest confusion tables</summary>
        {html_one_vs_rest(result)}
      </details>
    </section>
    """


def format_html_report(
    results: dict[str, object],
    selected: str,
    importances: list[tuple[str, float]],
    metadata: ReportMetadata,
) -> str:
    selected_result = results[selected]
    model_sections = "\n".join(html_model_section(name, result) for name, result in ranked_results(results))
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Plagiarism Model Evaluation</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #667085;
      --border: #d8dee8;
      --green: #18864b;
      --cyan: #087d8f;
      --yellow: #a46400;
      --red: #bd2d2d;
    }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.45;
    }}
    main {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 32px 20px 48px;
    }}
    h1, h2, h3, h4 {{ margin: 0; }}
    h1 {{ font-size: 30px; }}
    h2 {{ font-size: 22px; margin-bottom: 16px; }}
    h3 {{ font-size: 16px; margin: 24px 0 10px; color: var(--muted); }}
    h4 {{ font-size: 14px; margin: 18px 0 8px; }}
    .summary {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 12px;
      margin: 24px 0;
    }}
    .summary div, .metric-grid div {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
    }}
    .summary span, .metric-grid span {{
      display: block;
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    .summary strong, .metric-grid strong {{
      display: block;
      margin-top: 4px;
      font-size: 22px;
    }}
    .panel {{
      background: var(--panel);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin-top: 18px;
      overflow-x: auto;
    }}
    .metric-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
      gap: 10px;
      margin-bottom: 8px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }}
    th, td {{
      border-bottom: 1px solid var(--border);
      padding: 8px 10px;
      text-align: right;
      white-space: nowrap;
    }}
    th:first-child, td:first-child, .model-name {{ text-align: left; }}
    thead th {{
      background: #eef2f6;
      color: #344054;
      font-weight: 700;
    }}
    .metric {{ font-variant-numeric: tabular-nums; }}
    .best {{ color: var(--green); font-weight: 800; }}
    .neutral {{ color: var(--cyan); font-weight: 700; }}
    .selected {{ color: var(--green); font-weight: 800; text-align: left; }}
    .mistake-high {{ color: var(--red); font-weight: 800; }}
    .mistake-low {{ color: var(--yellow); font-weight: 800; }}
    .bar-track {{
      height: 10px;
      min-width: 160px;
      background: #e6ebf1;
      border-radius: 999px;
      overflow: hidden;
    }}
    .bar-fill {{
      height: 100%;
      background: var(--cyan);
    }}
    details {{ margin-top: 20px; }}
    summary {{ cursor: pointer; color: var(--muted); font-weight: 700; }}
    .small-table {{ margin-bottom: 10px; max-width: 420px; }}
    .empty {{ color: var(--green); font-weight: 700; }}
  </style>
</head>
<body>
  <main>
    <h1>Plagiarism model evaluation</h1>
    <section class="summary">
      <div><span>Rows</span><strong>{metadata.rows_count}</strong></div>
      <div><span>Features</span><strong>{metadata.feature_count} ({html.escape(metadata.feature_set)})</strong></div>
      <div><span>Folds</span><strong>{metadata.folds}</strong></div>
      <div><span>Selected model</span><strong>{html.escape(selected)}</strong></div>
    </section>

    <section class="panel">
      <h2>Model ranking</h2>
      {html_model_ranking(results, selected)}
    </section>

    <section class="panel">
      <h2>Selected model class performance</h2>
      <div class="metric-grid">
        <div><span>Accuracy</span><strong>{selected_result.accuracy:.3f}</strong></div>
        <div><span>Macro precision</span><strong>{macro_metric(selected_result, "precision"):.3f}</strong></div>
        <div><span>Macro recall</span><strong>{macro_metric(selected_result, "recall"):.3f}</strong></div>
        <div><span>Macro F1</span><strong>{selected_result.macro_f1:.3f}</strong></div>
      </div>
      {html_class_performance(selected_result)}
      <h3>Most common misclassifications</h3>
      {html_misclassifications(selected_result, limit=5)}
    </section>

    <section class="panel">
      <h2>Feature importance</h2>
      {html_feature_importance(importances)}
    </section>

    {model_sections}
  </main>
</body>
</html>
"""
