"""Machine-learning helpers for plagiarism type detection."""

from .plagiarism_model import (
    FEATURE_SETS,
    HierarchicalCloneClassifier,
    SpecialistEnsemble,
    build_classifier,
    evaluate_models,
    feature_importance,
    load_training_data,
    train_final_model,
)

__all__ = [
    "FEATURE_SETS",
    "HierarchicalCloneClassifier",
    "SpecialistEnsemble",
    "build_classifier",
    "evaluate_models",
    "feature_importance",
    "load_training_data",
    "train_final_model",
]
