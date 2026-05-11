"""Lightweight semantic-ish metrics without external model dependencies."""

from __future__ import annotations

import ast

from .common import normalized_levenshtein_similarity, python_tokens
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


def extract_semantic_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "semantic_normalized_ast": normalized_semantic_similarity(code_a, code_b),
    }
