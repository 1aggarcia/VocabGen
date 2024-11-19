"""
WordReference dictionary for generating flashcards
"""

from typing import Optional

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet

from ..vocabcard import Language, VocabCard, VocabCardQuery


WORD_REFERENCE_DOMAIN = "https://www.wordreference.com"
TIMEOUT_SECONDS = 5


def generate_flashcard(
        source_lang: Language,
        target_lang: Language,
        word: str
    ) -> Optional[VocabCard]:
    # consider scraping a large sum of words at once instead of on the spot
    query = VocabCardQuery(source_lang, target_lang, word)
    url = _format_wordreference_url(query)
    try:
        print(f"querying {url}")
        webpage = requests.get(url, timeout=TIMEOUT_SECONDS)
    except requests.exceptions.Timeout as e:
        print("Timeout occurred when reaching wordreference:", e)
        return None

    return _parse_wordreference_page(BeautifulSoup(webpage.content, "html.parser"), query)


def _format_wordreference_url(query: VocabCardQuery) -> str:
    lang_route = query.source_lang.wordreference_code + query.target_lang.wordreference_code
    return f"{WORD_REFERENCE_DOMAIN}/{lang_route}/{query.word}"


def _parse_wordreference_page(
        webpage: BeautifulSoup,
        query: VocabCardQuery
    ) -> Optional[VocabCard]:
    translations: ResultSet = webpage.find_all("td", { "class": "ToWrd" })
    if len(translations) < 2:
        print(f"No entry found in webpage for query: {query}")
        return None

    # using .next to get only the first text element and not all text
    first_translation = translations[1].next

    examples: ResultSet = webpage.find_all("td", { "class": "ToEx" })
    does_example_exist = len(examples) > 0
    if not does_example_exist:
        print(f"No example sentences found for query: {query}")

    first_example = examples[0].text if does_example_exist else "N/A"

    return VocabCard(
        source_lang=query.source_lang,
        target_lang=query.target_lang,
        word=query.word,
        translation=first_translation,
        example_sentence=first_example,
        ipa_transcription="N/A"
    )
