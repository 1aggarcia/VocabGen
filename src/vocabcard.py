from enum import Enum
from dataclasses import dataclass


class Language(Enum):
    """
    All supported languages
    """
    EN = "EN",
    ES = "ES",
    IT = "IT"


@dataclass
class VocabCard:
    source_lang: Language
    word: str
    target_lang: Language
    translation: str
    example_sentence: str
    ipa_transcription: str


def generate_flashcard(word: str, source_lang: Language, target_lang: Language) -> VocabCard:
    return VocabCard(
        source_lang=source_lang,
        target_lang=target_lang,
        word=word,
        translation="translation",
        example_sentence="the quick brown fox jumps over the lazy dog",
        ipa_transcription="/wɝd/"
    )
