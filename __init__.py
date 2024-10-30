from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction, qconnect

# TODO: dont crash the program if an assertion fails
assert mw is not None


def buildspace_test_action() -> None:
    card_count = mw.col.cardCount()
    showInfo(f"card_count = {card_count}")

action = QAction("buildspace test", mw)
qconnect(action.triggered, buildspace_test_action)


mw.form.menuTools.addAction(action)
