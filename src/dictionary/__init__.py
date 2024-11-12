"""
public API to access the dictionary
"""

from typing import Callable, Optional
from ..vocabcard import Language, VocabCard
from . import mock, wordreference


# poor man's strategy pattern in Python
generate_flashcard: Callable[[Language, Language, str], Optional[VocabCard]] = (
    wordreference.generate_flashcard
)
