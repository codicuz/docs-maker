#!/bin/bash

pyside6-rcc docs_maker_pyside6/resources/resources.qrc -o docs_maker_pyside6/resources/resources.py
pyside6-uic docs_maker_pyside6/ui/docs-maker-main-window.ui -o docs_maker_pyside6/ui/docs_maker_main_window.py

sed -i 's/import resources_rc/import docs_maker_pyside6.resources.resources/g' docs_maker_pyside6/ui/docs_maker_main_window.py

python3 -m docs_maker_pyside6
