#!/bin/bash

python docs_maker_web/manage.py makemigrations
python docs_maker_web/manage.py migrate
python docs_maker_web/manage.py runserver

# python docs_maker_web/manage.py createsuperuser