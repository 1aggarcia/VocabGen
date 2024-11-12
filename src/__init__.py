"""
Anki only takes commands from this file
"""

from aqt import mw, gui_hooks
from aqt.editor import Editor
from aqt.webview import WebContent
from aqt import utils
from aqt.qt import qconnect
from PyQt6.QtGui import QAction

from .vocabcard import Language
from .dictionary import generate_flashcard


def main():
    # QAction constructor below causes segmentation fault
    # comment these lines out to run unit tests
    action = QAction("test dictionary directly", mw)
    qconnect(action.triggered, on_test_dictionary)
    mw.form.menuTools.addAction(action)

    # setup web content
    gui_hooks.webview_will_set_content.append(on_webview_will_set_content)


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

def on_card_add(cards):
    print(f"card added {cards}")


# TODO: only change UI for editor

def on_webview_will_set_content(web_content: WebContent, context):
    print("ON_WEBVIEW_WILL_SET_CONTENT")
    print(type(web_content))
    print(type(context))
    print(context)

    if not isinstance(context, Editor):
        return
    editor: Editor = context

    try:
        web_content.body = "<h1>START OF CONTENT</h1>" \
            + web_content.body \
            + "<h1>END OF CONTENT</h1>"
    except Exception as e:
        utils.show_critical(str(e))


main()
