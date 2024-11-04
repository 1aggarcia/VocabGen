import unittest
from .vocabcard import Language

class TestVocabCard(unittest.TestCase):
    def test_language_wordreference_code(self):
        self.assertEqual(Language.EN.wordreference_code, "en")
        self.assertEqual(Language.ES.wordreference_code, "es")
        self.assertEqual(Language.IT.wordreference_code, "it")
