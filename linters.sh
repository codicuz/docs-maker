#!/bin/bash

flake8 --ignore E501 docs_maker
flake8 --ignore E501 --exclude docs_maker_main_window.py,resources.py docs_maker_gui
mypy docs_maker
mypy docs_maker_gui
