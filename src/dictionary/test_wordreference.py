# disable private member access warning
# pylint: disable=W0212

import unittest
from bs4 import BeautifulSoup

from . import wordreference
from ..vocabcard import Language, VocabCard, VocabCardQuery
from .test_data import REAL_PAGE_NEVICARE, REAL_PAGE_WORD_NOT_FOUND, HTML_NO_EXAMPLES


EXAMPLE_CARD = VocabCard(
    lang=Language.ES,
    word="nevar",
    translation_lang=Language.IT,
    translation="nevicare",
    example_sentence="¿Ya está nevando?",
    ipa_transcription="[neˈβar]"
)


EXAMPLE_QUERY = VocabCardQuery(
    translation_lang=EXAMPLE_CARD.translation_lang,
    lang=EXAMPLE_CARD.lang,
    word=EXAMPLE_CARD.word
)


def parse_shorthand(html: str, query: VocabCardQuery):
    return wordreference._parse_wordreference_page(
        BeautifulSoup(html, "html.parser"),
        query
    )


class TestFormatWordReferenceUrl(unittest.TestCase):
    def test_basic(self):
        result = wordreference._format_wordreference_url(
            VocabCardQuery("palabra", Language.ES, Language.IT)
        )
        self.assertEqual(result, "https://www.wordreference.com/esit/palabra")


class TestParseWordreferencePage(unittest.TestCase):
    def test_returns_correct_inputs_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None

        self.assertEqual(result.lang, EXAMPLE_CARD.lang)
        self.assertEqual(result.translation_lang, EXAMPLE_CARD.translation_lang)
        self.assertEqual(result.word, EXAMPLE_CARD.word)

    def test_returns_correct_translation_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.translation, EXAMPLE_CARD.translation)

    def test_returns_correct_example_sentence_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.example_sentence, EXAMPLE_CARD.example_sentence)

    def test_returns_correct_pronunciation_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.ipa_transcription, EXAMPLE_CARD.ipa_transcription)

    def test_returns_none_when_word_not_found(self):
        result = parse_shorthand(REAL_PAGE_WORD_NOT_FOUND, EXAMPLE_QUERY)
        self.assertIsNone(result)

    def test_returns_card_when_no_examples_found(self):
        result = parse_shorthand(HTML_NO_EXAMPLES, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.translation, "palabra")
        self.assertEqual(result.example_sentence, "N/A")
        self.assertEqual(result.ipa_transcription, "N/A")
