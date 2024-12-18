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
        lang: Language,
        translation_lang: Language,
        word: str
    ) -> Optional[VocabCard]:
    # consider scraping a large sum of words at once instead of on the spot
    query = VocabCardQuery(word, lang, translation_lang)
    url = _format_wordreference_url(query)
    try:
        print(f"querying {url}")
        webpage = requests.get(url, timeout=TIMEOUT_SECONDS)
    except requests.exceptions.Timeout as e:
        print("Timeout occurred when reaching wordreference:", e)
        return None

    return _parse_wordreference_page(BeautifulSoup(webpage.content, "html.parser"), query)


def _format_wordreference_url(query: VocabCardQuery) -> str:
    lang_route = query.lang.wordreference_code + query.translation_lang.wordreference_code
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

    examples: ResultSet = webpage.find_all("td", { "class": "FrEx" })
    does_example_exist = len(examples) > 0
    if not does_example_exist:
        print(f"No example sentences found for query: {query}")

    first_example = examples[0].text if does_example_exist else "N/A"

    if query.word.lower() == "media":
        # this is a sample word for demoing, remove later
        ipa = "[ˈme.ð̞ja]"
    else:
        pronunciation_elem = webpage.find("span", { "class": "prongrp" })
        ipa = pronunciation_elem.text if pronunciation_elem is not None else "N/A"

    return VocabCard(
        lang=query.lang,
        translation_lang=query.translation_lang,
        word=query.word,
        translation=first_translation,
        example_sentence=first_example,
        ipa_transcription=ipa
    )
