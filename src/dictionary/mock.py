"""
Mock flashcard generator for testing
"""

from ..vocabcard import Language, VocabCard

def generate_flashcard(source_lang: Language, target_lang: Language, word: str) -> VocabCard:
    return VocabCard(
        word=word,
        source_lang=source_lang,
        target_lang=target_lang,
        translation="translation",
        ipa_transcription="/ipa/",
        example_sentence="the quick brown fox jumps over the lazy dog"
    )
