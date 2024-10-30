## [Guide to modules](https://addon-docs.ankiweb.net/the-anki-module.html)

- add-ons require an `__init__.py` file, and are read from a top level `addons21` folder.
- UI updates are syncronus, processing should be done seperately
- dont modify the database directly, use provided APIs

## Modules
- `anki` - bridge between client code and app
- `mw` - main window object
    - `mw.col` currently open collection
- `aqt` - Anki Qt, based on PyQt. GUI functionality for Anki
