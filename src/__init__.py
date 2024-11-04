"""
Anki only takes commands from this file
"""
# TODO: change venv version to 3.9

from aqt import mw, gui_hooks
assert mw is not None
from aqt.webview import WebContent
from aqt.utils import showInfo
from aqt.qt import qconnect
from aqt.qt import QAction

from .vocabcard import Language
from .dictionary import generate_flashcard


def main():
    # setup test action
    action = QAction("test action", mw)
    qconnect(action.triggered, test_action)
    mw.form.menuTools.addAction(action)

    # setup web content
    gui_hooks.webview_will_set_content.append(on_webview_will_set_content)


def test_action():
    print("getting card from dictionary...")
    card = generate_flashcard(Language.ES, Language.IT, "nevar")
    print(card)
    showInfo(str(card))


def on_card_add(cards):
    print(f"card added {cards}")


# TODO: only change UI for editor
def on_webview_will_set_content(web_content: WebContent, context):
    print("")
    print(type(web_content))
    print(type(context))
    print(context)
    web_content.body  = "<i>demo add-on in use</i>" + web_content.body


main()
