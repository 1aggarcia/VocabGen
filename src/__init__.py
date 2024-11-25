"""
Anki only takes commands from this file
"""

from sys import stderr

from aqt.main import AnkiQt
from aqt import mw as mw_maybe_missing
from aqt import utils, qt

from .vocabcard import Language
from .flashcards.window import open_editor
from .dictionary import generate_flashcard


def main(mw: AnkiQt):
    # QAction constructor below causes segmentation fault
    # comment these lines out to run unit tests
    action = qt.QAction("Enter New Vocab Word", mw)
    qt.qconnect(action.triggered, lambda: open_editor(mw))
    mw.form.menuTools.addAction(action)


def on_test_dictionary():
    query_word = utils.getOnlyText("Enter a word to translate to Italian")
    italian_card = generate_flashcard(Language.EN, Language.IT, query_word)
    if italian_card is None:
        utils.show_warning(f"Failed to generate a flashcard for '{query_word}'")
        return

    utils.show_info(
        "word: " + italian_card.word
        + "\n\ntranslation: " + italian_card.translation
        + "\n\nexample_sentence: " + italian_card.example_sentence
        + "\n\nipa_transcription: " + italian_card.ipa_transcription
    )


if mw_maybe_missing is not None:
    main(mw_maybe_missing)
else:
    print("ERROR: Anki main window is missing. Quitting add-on.", file=stderr)
