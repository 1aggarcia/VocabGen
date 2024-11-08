"""
public API to access the dictionary
"""

from typing import Callable
from ..vocabcard import Language, VocabCard
from . import mock


# poor man's strategy pattern in Python
generate_flashcard: Callable[[Language, Language, str], VocabCard] = (
    mock.generate_flashcard
)
