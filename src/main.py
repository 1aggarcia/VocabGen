from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction, qconnect


def setup():
    """
    Perform all setup for the add-on. To be called from `__init__.py`.
    """
    action = QAction("buildspace test", mw)
    qconnect(action.triggered, buildspace_test_action)

    mw.form.menuTools.addAction(action)


def buildspace_test_action() -> None:
    card_count = mw.col.cardCount()
    showInfo(f"card_count = {card_count}")
