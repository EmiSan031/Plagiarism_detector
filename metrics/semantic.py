"""Lightweight semantic-ish metrics without external model dependencies."""

from __future__ import annotations

import ast
import hashlib
import math
import os
from collections import Counter

from .common import (
    clamp01,
    cosine_from_counters,
    jaccard_similarity,
    normalized_levenshtein_similarity,
    python_tokens,
)
from .syntactic import parse_ast

EMBEDDING_DIMENSIONS = 256
_SENTENCE_TRANSFORMER = None
_SENTENCE_TRANSFORMER_MODEL_NAME = None

CALL_CONCEPTS = {
    "sum": "aggregate_sum",
    "len": "sequence_length",
    "max": "aggregate_max",
    "min": "aggregate_min",
    "sorted": "ordering",
    "sort": "ordering",
    "append": "sequence_build",
    "extend": "sequence_build",
    "index": "search_position",
    "range": "iteration_range",
    "enumerate": "iteration_indexed",
    "zip": "parallel_iteration",
    "set": "unique_collection",
    "dict": "mapping_collection",
    "fromkeys": "unique_preserve_order",
    "lower": "text_normalize",
    "replace": "text_normalize",
    "split": "text_split",
    "join": "text_join",
    "abs": "numeric_absolute",
    "round": "numeric_round",
    "all": "logic_all",
    "any": "logic_any",
    "filter": "selection_filter",
}


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


def split_identifier(name: str) -> list[str]:
    words: list[str] = []
    current = ""
    for char in name.replace("_", " "):
        if char.isspace():
            if current:
                words.append(current.lower())
                current = ""
        elif char.isupper() and current:
            words.append(current.lower())
            current = char
        else:
            current += char
    if current:
        words.append(current.lower())
    return words


def ast_semantic_terms(code: str) -> list[str]:
    """Build a semantic-ish document from AST intent, not exact formatting."""
    tree = parse_ast(code)
    if tree is None:
        return python_tokens(code, normalize_identifiers=True)

    terms: list[str] = []
    for node in ast.walk(tree):
        node_name = type(node).__name__
        terms.append(f"node:{node_name}")

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            terms.extend(f"name:{word}" for word in split_identifier(node.name))
        elif isinstance(node, ast.Name):
            terms.append("identifier")
            terms.extend(f"name:{word}" for word in split_identifier(node.id))
        elif isinstance(node, ast.arg):
            terms.append("argument")
            terms.extend(f"name:{word}" for word in split_identifier(node.arg))
        elif isinstance(node, ast.Call):
            call = call_name(node)
            if call:
                terms.append(f"call:{call}")
                terms.append(f"concept:{CALL_CONCEPTS.get(call, call)}")
        elif isinstance(node, ast.BinOp):
            terms.append(f"operator:{type(node.op).__name__}")
        elif isinstance(node, ast.BoolOp):
            terms.append(f"operator:{type(node.op).__name__}")
        elif isinstance(node, ast.Compare):
            for operator in node.ops:
                terms.append(f"operator:{type(operator).__name__}")
        elif isinstance(node, ast.Constant):
            terms.append(f"literal:{type(node.value).__name__}")

    return terms


def call_name(node: ast.Call) -> str | None:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return None


def hashed_embedding(terms: list[str], dimensions: int = EMBEDDING_DIMENSIONS) -> list[float]:
    vector = [0.0] * dimensions
    if not terms:
        return vector

    for term, count in Counter(terms).items():
        digest = hashlib.blake2b(term.encode("utf-8"), digest_size=8).digest()
        bucket = int.from_bytes(digest[:4], "big") % dimensions
        sign = 1.0 if digest[4] % 2 == 0 else -1.0
        vector[bucket] += sign * (1.0 + math.log(count))

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]


def cosine_from_vectors(vector_a: list[float], vector_b: list[float]) -> float:
    if not vector_a and not vector_b:
        return 1.0
    if not vector_a or not vector_b:
        return 0.0
    dot = sum(a * b for a, b in zip(vector_a, vector_b))
    norm_a = math.sqrt(sum(value * value for value in vector_a))
    norm_b = math.sqrt(sum(value * value for value in vector_b))
    if norm_a == 0 or norm_b == 0:
        return 1.0 if norm_a == norm_b else 0.0
    return clamp01((dot / (norm_a * norm_b) + 1.0) / 2.0)


def load_sentence_transformer():
    """Load an optional external embedding model only when explicitly configured."""
    global _SENTENCE_TRANSFORMER, _SENTENCE_TRANSFORMER_MODEL_NAME

    model_name = os.getenv("CODE_EMBEDDING_MODEL")
    if not model_name:
        return None
    if _SENTENCE_TRANSFORMER is not None and _SENTENCE_TRANSFORMER_MODEL_NAME == model_name:
        return _SENTENCE_TRANSFORMER

    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        return None

    _SENTENCE_TRANSFORMER = SentenceTransformer(model_name)
    _SENTENCE_TRANSFORMER_MODEL_NAME = model_name
    return _SENTENCE_TRANSFORMER


def code_embedding_similarity(code_a: str, code_b: str) -> float:
    """Compare code using an optional neural embedding or a local semantic hash embedding."""
    model = load_sentence_transformer()
    if model is not None:
        embeddings = model.encode([code_a, code_b], normalize_embeddings=True)
        return cosine_from_vectors(list(embeddings[0]), list(embeddings[1]))

    return cosine_from_vectors(
        hashed_embedding(ast_semantic_terms(code_a)),
        hashed_embedding(ast_semantic_terms(code_b)),
    )


def extract_semantic_metrics(code_a: str, code_b: str) -> dict[str, float]:
    return {
        "code_embedding_similarity": code_embedding_similarity(code_a, code_b),
        "semantic_normalized_ast": normalized_semantic_similarity(code_a, code_b),
        "semantic_call_names": call_name_similarity(code_a, code_b),
        "semantic_operators": operator_profile_similarity(code_a, code_b),
        "semantic_return_shapes": return_shape_similarity(code_a, code_b),
        "semantic_comprehensions": comprehension_similarity(code_a, code_b),
    }
