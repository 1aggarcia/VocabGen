# disable private member access warning
# pylint: disable=W0212

import unittest
from bs4 import BeautifulSoup

from . import wordreference
from ..vocabcard import Language, VocabCard, VocabCardQuery
from ..test_data import EXAMPLE_PAGE


TEST_PAGE = BeautifulSoup(EXAMPLE_PAGE, "html.parser")


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


class TestWordReference(unittest.TestCase):
    def test_format_wordreference_url(self):
        result = wordreference._format_wordreference_url(
            VocabCardQuery(Language.ES, Language.IT, "palabra")
        )
        self.assertEqual(result, "https://www.wordreference.com/esit/palabra")

    def test_parse_wordreference_page_correct_inputs(self):
        result = wordreference._parse_wordreference_page(TEST_PAGE, EXAMPLE_QUERY)
        self.assertEqual(result.source_lang, EXAMPLE_CARD.source_lang)
        self.assertEqual(result.target_lang, EXAMPLE_CARD.target_lang)
        self.assertEqual(result.word, EXAMPLE_CARD.word)

    def test_parse_wordreference_page_correct_translation(self):
        result = wordreference._parse_wordreference_page(TEST_PAGE, EXAMPLE_QUERY)
        self.assertEqual(result.translation, EXAMPLE_CARD.translation)

    def test_parse_wordreference_page_correct_example_sentence(self):
        result = wordreference._parse_wordreference_page(TEST_PAGE, EXAMPLE_QUERY)
        self.assertEqual(result.example_sentence, EXAMPLE_CARD.example_sentence)


if __name__ == "__main__":
    unittest.main()
