"""Structural metrics for control flow shape and approximate complexity."""

from __future__ import annotations

import ast
from collections import Counter

from .common import cosine_from_counters, numeric_similarity
from .syntactic import parse_ast

CONTROL_NODES = (
    ast.If,
    ast.For,
    ast.AsyncFor,
    ast.While,
    ast.Try,
    ast.With,
    ast.AsyncWith,
    ast.Match,
)


def structural_profile(code: str) -> Counter:
    tree = parse_ast(code)
    if tree is None:
        return Counter()

    profile: Counter = Counter()
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            profile["if"] += 1
        elif isinstance(node, (ast.For, ast.AsyncFor)):
            profile["for"] += 1
        elif isinstance(node, ast.While):
            profile["while"] += 1
        elif isinstance(node, ast.Try):
            profile["try"] += 1
            profile["except"] += len(node.handlers)
        elif isinstance(node, (ast.With, ast.AsyncWith)):
            profile["with"] += 1
        elif isinstance(node, ast.BoolOp):
            profile["bool_op"] += max(1, len(node.values) - 1)
        elif isinstance(node, ast.FunctionDef):
            profile["function"] += 1
        elif isinstance(node, ast.ClassDef):
            profile["class"] += 1
        elif isinstance(node, ast.Return):
            profile["return"] += 1
    return profile


def cyclomatic_complexity(code: str) -> int:
    profile = structural_profile(code)
    decision_points = (
        profile["if"]
        + profile["for"]
        + profile["while"]
        + profile["except"]
        + profile["bool_op"]
    )
    return 1 + decision_points


def max_control_nesting(code: str) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0

    def visit(node: ast.AST, current_depth: int) -> int:
        next_depth = current_depth + 1 if isinstance(node, CONTROL_NODES) else current_depth
        child_depths = [visit(child, next_depth) for child in ast.iter_child_nodes(node)]
        return max([next_depth, *child_depths])

    return visit(tree, 0)


def count_nodes(code: str, node_type: type[ast.AST]) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0
    return sum(1 for node in ast.walk(tree) if isinstance(node, node_type))


def count_statements(code: str) -> int:
    return count_nodes(code, ast.stmt)


def count_functions(code: str) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0
    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )


def count_returns(code: str) -> int:
    return count_nodes(code, ast.Return)


def count_calls(code: str) -> int:
    return count_nodes(code, ast.Call)


def count_assignments(code: str) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0
    return sum(
        1
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign))
    )


def count_branches(code: str) -> int:
    return count_nodes(code, ast.If)


def count_loops(code: str) -> int:
    tree = parse_ast(code)
    if tree is None:
        return 0
    return sum(1 for node in ast.walk(tree) if isinstance(node, (ast.For, ast.AsyncFor, ast.While)))


def control_profile_similarity(code_a: str, code_b: str) -> float:
    return cosine_from_counters(structural_profile(code_a), structural_profile(code_b))


def cyclomatic_complexity_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(cyclomatic_complexity(code_a), cyclomatic_complexity(code_b))


def nesting_depth_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(max_control_nesting(code_a), max_control_nesting(code_b))


def statement_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_statements(code_a), count_statements(code_b))


def function_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_functions(code_a), count_functions(code_b))


def return_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_returns(code_a), count_returns(code_b))


def call_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_calls(code_a), count_calls(code_b))


def assignment_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_assignments(code_a), count_assignments(code_b))


def branch_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_branches(code_a), count_branches(code_b))


def loop_count_similarity(code_a: str, code_b: str) -> float:
    return numeric_similarity(count_loops(code_a), count_loops(code_b))


def extract_structural_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "control_profile": control_profile_similarity(code_a, code_b),
        "cyclomatic": cyclomatic_complexity_similarity(code_a, code_b),
        "nesting_depth": nesting_depth_similarity(code_a, code_b),
        "statement_count": statement_count_similarity(code_a, code_b),
        "function_count": function_count_similarity(code_a, code_b),
        "return_count": return_count_similarity(code_a, code_b),
        "call_count": call_count_similarity(code_a, code_b),
        "assignment_count": assignment_count_similarity(code_a, code_b),
        "branch_count": branch_count_similarity(code_a, code_b),
        "loop_count": loop_count_similarity(code_a, code_b),
    }
