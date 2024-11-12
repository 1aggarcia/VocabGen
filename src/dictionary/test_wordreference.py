# disable private member access warning
# pylint: disable=W0212

import unittest
from bs4 import BeautifulSoup

from . import wordreference
from ..vocabcard import Language, VocabCard, VocabCardQuery
from .test_data import REAL_PAGE_NEVICARE, REAL_PAGE_WORD_NOT_FOUND, HTML_NO_EXAMPLES


EXAMPLE_CARD = VocabCard(
    source_lang=Language.ES,
    target_lang=Language.IT,
    word="nevar",
    translation="nevicare",
    example_sentence="Sta ancora nevicando fuori?",
    ipa_transcription=""
)


EXAMPLE_QUERY = VocabCardQuery(
    source_lang=EXAMPLE_CARD.source_lang,
    target_lang=EXAMPLE_CARD.target_lang,
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
            VocabCardQuery(Language.ES, Language.IT, "palabra")
        )
        self.assertEqual(result, "https://www.wordreference.com/esit/palabra")

class TestParseWordreferencePage(unittest.TestCase):
    def test_returns_correct_inputs_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None

        self.assertEqual(result.source_lang, EXAMPLE_CARD.source_lang)
        self.assertEqual(result.target_lang, EXAMPLE_CARD.target_lang)
        self.assertEqual(result.word, EXAMPLE_CARD.word)

    def test_returns_correct_translation_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.translation, EXAMPLE_CARD.translation)

    def test_returns_correct_example_sentence_when_good_page(self):
        result = parse_shorthand(REAL_PAGE_NEVICARE, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.example_sentence, EXAMPLE_CARD.example_sentence)

    def test_returns_none_when_word_not_found(self):
        result = parse_shorthand(REAL_PAGE_WORD_NOT_FOUND, EXAMPLE_QUERY)
        self.assertIsNone(result)

    def test_returns_card_when_no_examples_found(self):
        result = parse_shorthand(HTML_NO_EXAMPLES, EXAMPLE_QUERY)
        assert result is not None
        self.assertEqual(result.translation, "palabra")
        self.assertEqual(result.example_sentence, "N/A")
