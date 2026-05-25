"""Lightweight semantic-ish metrics without external model dependencies."""

from __future__ import annotations

import ast
from collections import Counter

from .common import cosine_from_counters, jaccard_similarity, normalized_levenshtein_similarity, python_tokens
from .syntactic import parse_ast


class IdentifierNormalizer(ast.NodeTransformer):
    """Normalize names and literal values to compare program intent more fairly."""

    def visit_Name(self, node: ast.Name) -> ast.AST:
        return ast.copy_location(ast.Name(id="VAR", ctx=node.ctx), node)

    def visit_arg(self, node: ast.arg) -> ast.arg:
        node.arg = "ARG"
        return node

    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        if isinstance(node.value, str):
            value = "STR"
        elif isinstance(node.value, (int, float, complex)):
            value = 0
        else:
            value = node.value
        return ast.copy_location(ast.Constant(value=value), node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        node.name = "FUNC"
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.AST:
        node.name = "CLASS"
        self.generic_visit(node)
        return node


def normalized_ast_source(code: str) -> str:
    tree = parse_ast(code)
    if tree is None:
        return " ".join(python_tokens(code, normalize_identifiers=True))
    normalizer = IdentifierNormalizer()
    normalized = normalizer.visit(tree)
    ast.fix_missing_locations(normalized)
    return ast.dump(normalized, include_attributes=False)


def normalized_semantic_similarity(code_a: str, code_b: str) -> float:
    return normalized_levenshtein_similarity(
        normalized_ast_source(code_a).split(),
        normalized_ast_source(code_b).split(),
    )


def call_names(code: str) -> list[str]:
    tree = parse_ast(code)
    if tree is None:
        return []
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                names.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                names.append(node.func.attr)
            else:
                names.append(type(node.func).__name__)
    return names


def operator_profile(code: str) -> Counter:
    tree = parse_ast(code)
    if tree is None:
        return Counter()
    profile: Counter = Counter()
    for node in ast.walk(tree):
        if isinstance(node, ast.BinOp):
            profile[type(node.op).__name__] += 1
        elif isinstance(node, ast.BoolOp):
            profile[type(node.op).__name__] += 1
        elif isinstance(node, ast.Compare):
            for operator in node.ops:
                profile[type(operator).__name__] += 1
        elif isinstance(node, ast.UnaryOp):
            profile[type(node.op).__name__] += 1
    return profile


def return_expression_shapes(code: str) -> list[str]:
    tree = parse_ast(code)
    if tree is None:
        return []
    shapes = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Return) and node.value is not None:
            shapes.append(type(node.value).__name__)
    return shapes


def comprehension_profile(code: str) -> Counter:
    tree = parse_ast(code)
    if tree is None:
        return Counter()
    profile: Counter = Counter()
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            profile["list_comp"] += 1
        elif isinstance(node, ast.SetComp):
            profile["set_comp"] += 1
        elif isinstance(node, ast.DictComp):
            profile["dict_comp"] += 1
        elif isinstance(node, ast.GeneratorExp):
            profile["generator"] += 1
    return profile


def call_name_similarity(code_a: str, code_b: str) -> float:
    return jaccard_similarity(call_names(code_a), call_names(code_b))


def operator_profile_similarity(code_a: str, code_b: str) -> float:
    return cosine_from_counters(operator_profile(code_a), operator_profile(code_b))


def return_shape_similarity(code_a: str, code_b: str) -> float:
    return normalized_levenshtein_similarity(
        return_expression_shapes(code_a),
        return_expression_shapes(code_b),
    )


def comprehension_similarity(code_a: str, code_b: str) -> float:
    return cosine_from_counters(comprehension_profile(code_a), comprehension_profile(code_b))


def extract_semantic_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "semantic_normalized_ast": normalized_semantic_similarity(code_a, code_b),
        "semantic_call_names": call_name_similarity(code_a, code_b),
        "semantic_operators": operator_profile_similarity(code_a, code_b),
        "semantic_return_shapes": return_shape_similarity(code_a, code_b),
        "semantic_comprehensions": comprehension_similarity(code_a, code_b),
    }
