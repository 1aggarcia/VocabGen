from enum import Enum
from dataclasses import dataclass
from typing import Optional


class Language(Enum):
    """
    All supported languages
    """
    # these language codes are taken from https://www.wordreference.com,
    # so it should support them all
    EN = "English"
    ES = "Spanish"
    IT = "Italian"
    FR = "French"
    PT = "Portugese"
    DE = "German"
    NL = "Dutch"
    RU = "Russian"
    PL = "Polish"
    RO = "Romanian"
    CZ = "Czech"
    GR = "Greek"
    TK = "Turkish"
    ZH = "Chinese"
    JA = "Japanese"
    KO = "Korean"
    AR = "Arabic"
    IS = "Icelandic"

    @property
    def wordreference_code(self):
        # wordreference uses lowercase codes
        return self.name.lower()

    @staticmethod
    def lookup(value: str) -> Optional['Language']:
        """
        Returns the enum member by its value, or `None` if no such member exists.

        Wrapper for `Language(value)` that does not throw an error.
        """
        try:
            return Language(value)
        except ValueError:
            return None

    def __repr__(self):
        return self.name


@dataclass(frozen=True)
class VocabCardQuery:
    source_lang: Language
    target_lang: Language
    word: str


@dataclass(frozen=True)
class VocabCard:
    source_lang: Language
    target_lang: Language
    word: str
    translation: str
    example_sentence: str
    ipa_transcription: str

    def __str__(self):
        return (
            f"<h1>{self.translation}</h1>"
            f"<i>{self.ipa_transcription}</i>"
            f"<p>{self.example_sentence}</p>"
        )
