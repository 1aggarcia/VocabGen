from anki.models import NotetypeDict
from anki.decks import DeckDict
from anki.collection import Collection

from aqt.main import AnkiQt
from aqt import qt
from aqt.utils import show_critical, show_info

from ..dictionary import generate_flashcard
from ..vocabcard import Language, VocabCard

def open_editor(mw: AnkiQt):
    """
    Shows the flashcard generator window to the user.
    Args:
        mw : Main Anki window
    """
    # dependencies to insert a card
    sample_card = generate_flashcard(Language.ES, Language.IT, "parola")
    if sample_card is None:
        show_critical("Failed to generate flashcard")
        return

    col = mw.col
    if col is None:
        show_critical("ERROR: mw.col is None")
        return

    model = col.models.current()
    fields = model["flds"]
    print(f"model fields: {fields}")

    deck = col.decks.by_name("Italiano")
    if deck is None:
        raise RuntimeError("deck does not exist")

    decks_to_string = "\n".join([
        f"{deck['id']}: {deck['name']}"
        for deck in mw.col.decks.all()
    ])

    # components
    label = qt.QLabel(decks_to_string)

    button_append_text = qt.QPushButton("Append Text")
    button_append_text.clicked.connect(lambda: increment_count(label))

    button_add_card = qt.QPushButton("Add sample card")
    button_add_card.clicked.connect(lambda: add_sample_card(
        col=col,
        model=model,
        deck=deck,
        card=sample_card
    ))

    # layout
    layout = qt.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button_append_text)
    layout.addWidget(button_add_card)

    # window
    window = qt.QDialog(mw)
    window.setWindowTitle("custom window")
    window.resize(400, 300)
    window.setLayout(layout)
    window.exec()


count = 0
def increment_count(label: qt.QLabel):
    global count
    count += 1
    label.setText(label.text() + " " + str(count))


def add_sample_card(*,
        col: Collection ,
        model: NotetypeDict,
        deck: DeckDict,
        card: VocabCard
    ):
    note = col.new_note(model)
    note.fields = [card.word, str(card)]  # this depends heavily on the model

    print(f"new_note: {note}")

    # TODO: check for duplicates first
    col.add_note(note, deck['id'])
    show_info(f"Note for '{card.word}' added to deck '{deck['name']}'")
