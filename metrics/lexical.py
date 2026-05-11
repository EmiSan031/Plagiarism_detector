"""Lexical similarity metrics based on Python tokens."""

from __future__ import annotations

from collections import Counter

from .common import (
    cosine_from_counters,
    jaccard_similarity,
    normalized_levenshtein_similarity,
    python_tokens,
)


def lexical_token_jaccard(code_a: str, code_b: str) -> float:
    return jaccard_similarity(
        python_tokens(code_a, normalize_identifiers=True),
        python_tokens(code_b, normalize_identifiers=True),
    )


def lexical_token_cosine(code_a: str, code_b: str) -> float:
    return cosine_from_counters(
        Counter(python_tokens(code_a, normalize_identifiers=True)),
        Counter(python_tokens(code_b, normalize_identifiers=True)),
    )


def lexical_edit_similarity(code_a: str, code_b: str) -> float:
    return normalized_levenshtein_similarity(
        python_tokens(code_a, normalize_identifiers=True),
        python_tokens(code_b, normalize_identifiers=True),
    )


def extract_lexical_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "lexical_jaccard": lexical_token_jaccard(code_a, code_b),
        "lexical_cosine": lexical_token_cosine(code_a, code_b),
        "lexical_edit": lexical_edit_similarity(code_a, code_b),
    }
