#!/bin/bash

source ./.venv/bin/activate

msgfmt docs_maker_messages/en/LC_MESSAGES/messages.po -o docs_maker_messages/en/LC_MESSAGES/messages.mo
msgfmt docs_maker_messages/ru/LC_MESSAGES/messages.po -o docs_maker_messages/ru/LC_MESSAGES/messages.mo

pyside6-rcc docs_maker_gui/resources/resources.qrc -o docs_maker_gui/resources/resources.py
pyside6-uic docs_maker_gui/ui/docs-maker-main-window.ui -o docs_maker_gui/ui/docs_maker_main_window.py
pyside6-uic docs_maker_gui/ui/db-indicator.ui -o docs_maker_gui/ui/db_indicator.py

sed -i 's/import resources_rc/import docs_maker_gui.resources.resources/g' docs_maker_gui/ui/docs_maker_main_window.py

#python3 -m docs_maker_gui

deactivate
