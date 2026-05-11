"""AST-based syntactic similarity metrics."""

from __future__ import annotations

import ast
from collections import Counter

from .common import (
    cosine_from_counters,
    jaccard_similarity,
    normalized_levenshtein_similarity,
    numeric_similarity,
)


def parse_ast(code: str) -> ast.AST | None:
    try:
        return ast.parse(code)
    except SyntaxError:
        return None


def ast_node_sequence(code: str) -> list[str]:
    tree = parse_ast(code)
    if tree is None:
        return []
    return [type(node).__name__ for node in ast.walk(tree)]


def ast_max_depth(code: str) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0

    def depth(node: ast.AST) -> int:
        children = list(ast.iter_child_nodes(node))
        if not children:
            return 1
        return 1 + max(depth(child) for child in children)

    return depth(tree)


def ast_node_jaccard(code_a: str, code_b: str) -> float:
    return jaccard_similarity(ast_node_sequence(code_a), ast_node_sequence(code_b))


def ast_node_cosine(code_a: str, code_b: str) -> float:
    return cosine_from_counters(
        Counter(ast_node_sequence(code_a)),
        Counter(ast_node_sequence(code_b)),
    )


def ast_sequence_similarity(code_a: str, code_b: str) -> float:
    return normalized_levenshtein_similarity(
        ast_node_sequence(code_a),
        ast_node_sequence(code_b),
    )


def ast_depth_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(ast_max_depth(code_a), ast_max_depth(code_b))


def extract_syntactic_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "ast_jaccard": ast_node_jaccard(code_a, code_b),
        "ast_cosine": ast_node_cosine(code_a, code_b),
        "ast_sequence": ast_sequence_similarity(code_a, code_b),
        "ast_depth": ast_depth_similarity(code_a, code_b),
    }
