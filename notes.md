## [Guide to modules](https://addon-docs.ankiweb.net/the-anki-module.html)
- [Guide to hooks](https://github.com/ankitects/anki/blob/main/qt/tools/genhooks_gui.py)

- add-ons require an `__init__.py` file, and are read from a top level `addons21` folder.
- UI updates are syncronus, processing should be done seperately
- dont modify the database directly, use provided APIs

## Modules
- `anki` - bridge between client code and app
- `mw` - main window object
    - `mw.col` currently open collection
- `aqt` - Anki Qt, based on PyQt. GUI functionality for Anki


## Hooks
The recommended way to connect code to Anki
`aqt.gui_hooks` allows you to hook on to GUI events
- hooks ref:
    - https://github.com/ankitects/anki/blob/main/pylib/tools/genhooks.py
    - https://github.com/ankitects/anki/blob/main/qt/tools/genhooks_gui.py


## Random
- to grant permission to execute a bash script: `chmod +x $filename`