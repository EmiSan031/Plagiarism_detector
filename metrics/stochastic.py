"""Stochastic metrics inspired by the Markov-chain notebook."""

from __future__ import annotations

import io
import keyword
import math
import tokenize
from collections import Counter

from .common import clamp01, numeric_similarity

ALPHABET = ("STMT", "CTRL", "FUNC", "LOGIC", "MATH", "OP")
SMOOTHING = 0.01

CONTROL_KEYWORDS = {"if", "else", "elif", "while", "for", "try", "except", "finally", "with", "match", "case"}
FUNC_KEYWORDS = {"def", "class", "return", "yield", "global", "nonlocal", "lambda", "import", "from"}
LOGIC_OPERATORS = {"==", "!=", "<", ">", "<=", ">=", "and", "or", "not", "in", "is"}
MATH_OPERATORS = {"+", "-", "*", "/", "%", "**", "//", "+=", "-=", "*=", "/=", "%=", "//=", "**="}


def semantic_token(token_type: int, token_string: str) -> str | None:
    if token_type == tokenize.NAME:
        if token_string in CONTROL_KEYWORDS:
            return "CTRL"
        if token_string in FUNC_KEYWORDS:
            return "FUNC"
        if token_string in LOGIC_OPERATORS or keyword.iskeyword(token_string):
            return "LOGIC"
        return "STMT"
    if token_type == tokenize.OP:
        if token_string in LOGIC_OPERATORS:
            return "LOGIC"
        if token_string in MATH_OPERATORS:
            return "MATH"
        return "OP"
    if token_type in {tokenize.NUMBER, tokenize.STRING}:
        return "STMT"
    return None


def semantic_tokenize(code: str) -> list[str]:
    tokens: list[str] = []
    try:
        token_stream = tokenize.generate_tokens(io.StringIO(code).readline)
        for token in token_stream:
            label = semantic_token(token.type, token.string)
            if label:
                tokens.append(label)
    except tokenize.TokenError:
        return []
    return tokens


def transition_matrix(tokens: list[str], alphabet: tuple[str, ...] = ALPHABET) -> list[list[float]]:
    index = {state: pos for pos, state in enumerate(alphabet)}
    size = len(alphabet)
    matrix = [[SMOOTHING for _ in range(size)] for _ in range(size)]

    for current_state, next_state in zip(tokens, tokens[1:]):
        if current_state in index and next_state in index:
            matrix[index[current_state]][index[next_state]] += 1.0

    normalized: list[list[float]] = []
    for row in matrix:
        row_sum = sum(row)
        normalized.append([value / row_sum for value in row])
    return normalized


def state_weights(tokens: list[str], alphabet: tuple[str, ...] = ALPHABET) -> list[float]:
    counts = Counter(tokens)
    total = sum(counts[state] for state in alphabet)
    if total == 0:
        return [1.0 / len(alphabet) for _ in alphabet]
    return [counts[state] / total for state in alphabet]


def shannon_entropy(tokens: list[str]) -> float:
    if not tokens:
        return 0.0
    counts = Counter(tokens)
    total = len(tokens)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())


def kl_divergence(p: list[float], q: list[float]) -> float:
    total = 0.0
    for p_i, q_i in zip(p, q):
        if p_i > 0 and q_i > 0:
            total += p_i * math.log2(p_i / q_i)
    return total


def weighted_markov_kl(tokens_a: list[str], tokens_b: list[str]) -> float:
    matrix_a = transition_matrix(tokens_a)
    matrix_b = transition_matrix(tokens_b)
    weights = state_weights(tokens_a)
    return sum(weight * kl_divergence(row_a, row_b) for weight, row_a, row_b in zip(weights, matrix_a, matrix_b))


def js_divergence(p: list[float], q: list[float]) -> float:
    midpoint = [(p_i + q_i) / 2 for p_i, q_i in zip(p, q)]
    return 0.5 * kl_divergence(p, midpoint) + 0.5 * kl_divergence(q, midpoint)


def weighted_markov_js(tokens_a: list[str], tokens_b: list[str]) -> float:
    matrix_a = transition_matrix(tokens_a)
    matrix_b = transition_matrix(tokens_b)
    weights_a = state_weights(tokens_a)
    weights_b = state_weights(tokens_b)
    weights = [(a + b) / 2 for a, b in zip(weights_a, weights_b)]
    return sum(weight * js_divergence(row_a, row_b) for weight, row_a, row_b in zip(weights, matrix_a, matrix_b))


def divergence_to_similarity(divergence: float) -> float:
    return clamp01(1.0 / (1.0 + divergence))


def markov_kl_similarity(code_a: str, code_b: str) -> float:
    return divergence_to_similarity(weighted_markov_kl(semantic_tokenize(code_a), semantic_tokenize(code_b)))


def markov_js_similarity(code_a: str, code_b: str) -> float:
    return divergence_to_similarity(weighted_markov_js(semantic_tokenize(code_a), semantic_tokenize(code_b)))


def entropy_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(
        shannon_entropy(semantic_tokenize(code_a)),
        shannon_entropy(semantic_tokenize(code_b)),
    )


def extract_stochastic_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "markov_kl": markov_kl_similarity(code_a, code_b),
        "markov_js": markov_js_similarity(code_a, code_b),
        "entropy": entropy_similarity(code_a, code_b),
    }
