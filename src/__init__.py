"""
Anki only takes commands from this file
"""
# TODO: change venv version to 3.9

from aqt import mw, gui_hooks
from aqt.webview import WebContent
from aqt.utils import showInfo
from aqt.qt import qconnect
from aqt.qt import QAction

from . import vocabcard

assert mw is not None


def main():
    # setup test action
    action = QAction("test action", mw)
    qconnect(action.triggered, test_action)
    mw.form.menuTools.addAction(action)

    # setup card add
    # gui_hooks.add_cards_did_init.append(on_card_add)

    # setup web content
    gui_hooks.webview_will_set_content.append(on_webview_will_set_content)


def test_action():
    card_count = mw.col.cardCount()
    showInfo(f"card_count: {card_count}")


def on_card_add(cards):
    print(f"card added {cards}")
    card = vocabcard.generate_flashcard("palabra", vocabcard.Language.ES, vocabcard.Language.IT)
    showInfo(str(card))


# TODO: only change UI for editor
def on_webview_will_set_content(web_content: WebContent, context):
    print("")
    print(type(web_content))
    print(type(context))
    print(context)
    web_content.body  = "<i>demo add-on in use</i>" + web_content.body


main()
