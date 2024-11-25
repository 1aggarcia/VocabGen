import unittest
from .vocabcard import Language, VocabCard

class TestLanguage(unittest.TestCase):
    # these test cases seem really dumb but
    # I had actual bugs caused by these methods

    def test_wordreference_code(self):
        self.assertEqual(Language.EN.wordreference_code, "en")
        self.assertEqual(Language.ES.wordreference_code, "es")
        self.assertEqual(Language.IT.wordreference_code, "it")
        self.assertEqual(Language.FR.wordreference_code, "fr")

    def test_lookup_returns_member_when_key_exists(self):
        self.assertEqual(Language.lookup(Language.EN.value), Language.EN)
        self.assertEqual(Language.lookup(Language.ES.value), Language.ES)
        self.assertEqual(Language.lookup(Language.IT.value), Language.IT)
        self.assertEqual(Language.lookup(Language.FR.value), Language.FR)

    def test_lookup_returns_none_when_key_does_not_exist(self):
        self.assertIsNone(Language.lookup("this lanuguage does not exist"))
        self.assertIsNone(Language.lookup("dummy lanuage"))


class TestVocabCard(unittest.TestCase):
    def test_str_returns_html(self):
        test_card = VocabCard(
            word="anello",
            lang=Language.IT,
            translation="ring",
            translation_lang=Language.EN,
            example_sentence="Yvonne ha realizzato un bell'anello d'argento.",
            ipa_transcription="N/A"
        )
        expected = (
            "<h2>anello</h2>"
            + "<p>N/A</p>"
            + "<i>(it) Yvonne ha realizzato un bell'anello d'argento.</i>"
        )
        self.assertEqual(str(test_card), expected)
