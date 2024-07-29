#!/bin/bash

rm db.sqlite3
rm -rf ./digestapi/migrations
python manage.py migrate
python manage.py makemigrations digestapi
python manage.py migrate digestapi
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata categories
python manage.py loaddata books
python manage.py loaddata book_categories
python manage.py loaddata reviews

