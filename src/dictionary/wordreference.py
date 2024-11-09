"""
WordReference dictionary for generating flashcards
"""

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet

from ..vocabcard import Language, VocabCard, VocabCardQuery
from ..test_data import EXAMPLE_PAGE


WORD_REFERENCE_DOMAIN = "https://www.wordreference.com"


def generate_flashcard(
    source_lang: Language,
    target_lang: Language,
    word: str
) -> VocabCard:
    # consider scraping a large sum of words at once instead of on the spot
    query = VocabCardQuery(source_lang, target_lang, word)
    url = _format_wordreference_url(query)
    try:
        webpage = requests.get(url, timeout=10)
    except requests.exceptions.Timeout:
        # TODO: handle timeout
        print("unhandled timeout")
        exit(1)

    return _parse_wordreference_page(BeautifulSoup(webpage.content, "html.parser"), query)


def _format_wordreference_url(query: VocabCardQuery) -> str:
    lang_route = query.source_lang.wordreference_code + query.target_lang.wordreference_code
    return f"{WORD_REFERENCE_DOMAIN}/{lang_route}/{query.word}"


def _parse_wordreference_page(webpage: BeautifulSoup, query: VocabCardQuery) -> VocabCard:
    # TODO: handle errors, translation not existing

    translations: ResultSet = webpage.find_all("td", { "class": "ToWrd" })
    # using .next to get only the first text element and not all text
    first_translation = translations[1].next

    examples: ResultSet = webpage.find_all("td", { "class": "ToEx" })
    first_example = examples[0].text

    return VocabCard(
        source_lang=query.source_lang,
        target_lang=query.target_lang,
        word=query.word,
        translation=first_translation,
        example_sentence=first_example,
        ipa_transcription="N/A"
    )
