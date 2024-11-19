from anki.models import NotetypeDict
from anki.decks import DeckDict
from anki.collection import Collection

from aqt.main import AnkiQt
from aqt import qt
from aqt.utils import show_critical, show_info

from ..dictionary import generate_flashcard
from ..vocabcard import Language, VocabCard, VocabCardQuery


def open_editor(mw: AnkiQt):
    """
    Shows the flashcard generator window to the user.
    Args:
        mw : Main Anki window
    """
    col = mw.col
    if col is None:
        show_critical("ERROR: mw.col is None")
        return

    # components
    layout = qt.QVBoxLayout()

    layout.addWidget(qt.QLabel("Deck:"))
    deck_options = qt.QComboBox()
    deck_names = [deck['name'] for deck in col.decks.all()]
    deck_options.addItems(deck_names)
    layout.addWidget(deck_options)

    layout.addWidget(qt.QLabel("Source Lang:"))
    source_options = qt.QComboBox()
    source_options.addItems(lang.value for lang in Language)
    layout.addWidget(source_options)

    layout.addWidget(qt.QLabel("Target Lang:"))
    target_options = qt.QComboBox()
    target_options.addItems(lang.value for lang in Language)
    layout.addWidget(target_options)

    layout.addWidget(qt.QLabel("Word:"))
    word_input = qt.QLineEdit()
    word_input.setPlaceholderText("Enter word to translate")
    layout.addWidget(word_input)

    search_button = qt.QPushButton("Search in dictionary (and add to deck)")
    search_button.clicked.connect(lambda: on_search_clicked(
        col=col,
        deck_input=deck_options.currentText(),
        source_lang_input=source_options.currentText(),
        target_lang_input=target_options.currentText(),
        word_input=word_input.text(),
    ))
    layout.addWidget(search_button)

    # window
    window = qt.QDialog(mw)
    window.setWindowTitle("Dictionary Flashcard Editor")
    window.resize(400, 300)
    window.setLayout(layout)
    window.exec()


def on_search_clicked(*,
        col: Collection,
        deck_input: str,
        source_lang_input: str,
        target_lang_input: str,
        word_input: str
    ):
    deck = col.decks.by_name(deck_input)
    if deck is None:
        return

    source_lang = Language.lookup(source_lang_input)
    target_lang = Language.lookup(target_lang_input)

    if source_lang is None or target_lang is None:
        raise ValueError(f"Language(s) does not exist: {source_lang} | {target_lang}")

    query = VocabCardQuery(
        source_lang=source_lang,
        target_lang=target_lang,
        word=word_input
    )
    print(f"starting query for {str(query)}")

    # blocking call
    result = generate_flashcard(query.source_lang, query.target_lang, query.word)
    if result is None:
        show_critical("Failed to generate flashcard")
        return

    # TODO: show result to user to confirm, instead of adding the card right away
    add_sample_card(
        col=col,
        model=col.models.current(),
        deck=deck,
        card=result
    )
    show_info(f"new card added to {deck['name']}")


def add_sample_card(*,
        col: Collection ,
        model: NotetypeDict,
        deck: DeckDict,
        card: VocabCard
    ):
    if len(model['flds']) != 2:
        raise RuntimeError(f"Model must have two fields: {model}")

    note = col.new_note(model)
    note.fields = [card.word, str(card)]  # this depends heavily on the model

    # TODO: check for duplicates first
    col.add_note(note, deck['id'])
