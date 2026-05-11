"""Aggregate all metric families into one feature vector."""

from __future__ import annotations

from .lexical import extract_lexical_metrics
from .semantic import extract_semantic_metrics
from .structural import extract_structural_metrics
from .stochastic import extract_stochastic_metrics
from .syntactic import extract_syntactic_metrics

DEFAULT_FAMILY_WEIGHTS = {
    "lexical": 0.20,
    "syntactic": 0.25,
    "structural": 0.20,
    "stochastic": 0.20,
    "semantic": 0.15,
}


def average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def extract_all_metrics(code_a: str, code_b: str) -> dict[str, float]:
    lexical = extract_lexical_metrics(code_a, code_b)
    syntactic = extract_syntactic_metrics(code_a, code_b)
    structural = extract_structural_metrics(code_a, code_b)
    stochastic = extract_stochastic_metrics(code_a, code_b)
    semantic = extract_semantic_metrics(code_a, code_b)

    family_scores = {
        "score_lexical": average(list(lexical.values())),
        "score_syntactic": average(list(syntactic.values())),
        "score_structural": average(list(structural.values())),
        "score_stochastic": average(list(stochastic.values())),
        "score_semantic": average(list(semantic.values())),
    }

    hybrid_score = (
        DEFAULT_FAMILY_WEIGHTS["lexical"] * family_scores["score_lexical"]
        + DEFAULT_FAMILY_WEIGHTS["syntactic"] * family_scores["score_syntactic"]
        + DEFAULT_FAMILY_WEIGHTS["structural"] * family_scores["score_structural"]
        + DEFAULT_FAMILY_WEIGHTS["stochastic"] * family_scores["score_stochastic"]
        + DEFAULT_FAMILY_WEIGHTS["semantic"] * family_scores["score_semantic"]
    )

    return {
        **lexical,
        **syntactic,
        **structural,
        **stochastic,
        **semantic,
        **family_scores,
        "hybrid_score": hybrid_score,
    }
