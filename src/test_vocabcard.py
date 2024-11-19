import unittest
from .vocabcard import Language, VocabCard

class TestVocabCard(unittest.TestCase):
    def test_language_wordreference_code(self):
        self.assertEqual(Language.EN.wordreference_code, "en")
        self.assertEqual(Language.ES.wordreference_code, "es")
        self.assertEqual(Language.IT.wordreference_code, "it")

    def test_str_basic(self):
        test_card = VocabCard(
            source_lang=Language.EN,
            target_lang=Language.IT,
            word="ring",
            translation="anello",
            example_sentence="Yvonne ha realizzato un bell'anello d'argento.",
            ipa_transcription="N/A"
        )
        expected = (
            "<h1>anello</h1>"
            + "<i>N/A</i>"
            + "<p>Yvonne ha realizzato un bell'anello d'argento.</p>"
        )
        self.assertEqual(str(test_card), expected)
