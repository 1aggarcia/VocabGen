from enum import Enum
from dataclasses import dataclass


class Language(Enum):
    """
    All supported languages
    """
    EN = "EN"
    ES = "ES"
    IT = "IT"
    FR = "FR"

    @property
    def wordreference_code(self):
        # wordreference uses lowercase codes
        return self.value.lower()


@dataclass
class VocabCardQuery:
    source_lang: Language
    target_lang: Language
    word: str


@dataclass
class VocabCard:
    source_lang: Language
    target_lang: Language
    word: str
    translation: str
    example_sentence: str
    ipa_transcription: str
