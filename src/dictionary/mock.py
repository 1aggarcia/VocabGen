"""
Mock flashcard generator for testing
"""

from typing import Optional
from ..vocabcard import Language, VocabCard

def generate_flashcard(
        source_lang: Language,
        target_lang: Language,
        word: str
    ) -> Optional[VocabCard]:
    return VocabCard(
        word=word,
        lang=source_lang,
        translation_lang=target_lang,
        translation="translation",
        ipa_transcription="/ipa/",
        example_sentence="the quick brown fox jumps over the lazy dog"
    )
