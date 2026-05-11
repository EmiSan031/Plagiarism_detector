"""Shared helpers for code similarity metrics."""

from __future__ import annotations

import io
import keyword
import math
import tokenize
from collections import Counter
from typing import Iterable


def clamp01(value: float) -> float:
    """Keep a score inside the [0, 1] interval."""
    if math.isnan(value) or math.isinf(value):
        return 0.0
    return max(0.0, min(1.0, value))


def safe_ratio(a: float, b: float) -> float:
    if b == 0:
        return 1.0 if a == 0 else 0.0
    return a / b


def numeric_similarity(a: float, b: float) -> float:
    """Similarity for scalar values where equal values should score 1."""
    denominator = max(abs(a), abs(b), 1.0)
    return clamp01(1.0 - abs(a - b) / denominator)


def cosine_from_counters(counter_a: Counter, counter_b: Counter) -> float:
    keys = set(counter_a) | set(counter_b)
    if not keys:
        return 1.0

    dot = sum(counter_a[key] * counter_b[key] for key in keys)
    norm_a = math.sqrt(sum(counter_a[key] ** 2 for key in keys))
    norm_b = math.sqrt(sum(counter_b[key] ** 2 for key in keys))
    if norm_a == 0 or norm_b == 0:
        return 1.0 if norm_a == norm_b else 0.0
    return clamp01(dot / (norm_a * norm_b))


def jaccard_similarity(items_a: Iterable[str], items_b: Iterable[str]) -> float:
    set_a = set(items_a)
    set_b = set(items_b)
    if not set_a and not set_b:
        return 1.0
    return len(set_a & set_b) / len(set_a | set_b)


def normalized_levenshtein_similarity(seq_a: list[str], seq_b: list[str]) -> float:
    """Levenshtein similarity for token sequences."""
    if not seq_a and not seq_b:
        return 1.0
    if not seq_a or not seq_b:
        return 0.0

    previous = list(range(len(seq_b) + 1))
    for i, token_a in enumerate(seq_a, start=1):
        current = [i]
        for j, token_b in enumerate(seq_b, start=1):
            substitution_cost = 0 if token_a == token_b else 1
            current.append(
                min(
                    previous[j] + 1,
                    current[j - 1] + 1,
                    previous[j - 1] + substitution_cost,
                )
            )
        previous = current

    distance = previous[-1]
    return clamp01(1.0 - distance / max(len(seq_a), len(seq_b)))


def python_tokens(code: str, normalize_identifiers: bool = False) -> list[str]:
    """Tokenize Python code while ignoring whitespace, comments and encoding data."""
    ignored = {
        tokenize.ENCODING,
        tokenize.NL,
        tokenize.NEWLINE,
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.ENDMARKER,
        tokenize.COMMENT,
    }
    tokens: list[str] = []
    try:
        token_stream = tokenize.generate_tokens(io.StringIO(code).readline)
        for token in token_stream:
            if token.type in ignored:
                continue
            value = token.string
            if normalize_identifiers and token.type == tokenize.NAME:
                value = value if keyword.iskeyword(value) else "IDENTIFIER"
            elif normalize_identifiers and token.type == tokenize.NUMBER:
                value = "NUMBER"
            elif normalize_identifiers and token.type == tokenize.STRING:
                value = "STRING"
            tokens.append(value)
    except tokenize.TokenError:
        return []
    return tokens
