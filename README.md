# Usage

## Windows

1. Clone this repo
1. `python -m venv nottoenv`
1. `nottoenv\Scripts\activate`
1. `pip install -r requirements.txt`

## Linux/MacOS

1. Clone this repo
1. `python3 -m venv nottoenv`
1. `source nottoenv/bin/activate`
1. `pip install -r requirements.txt`
1. `python notto/manage.py makemigrations nottoapp`
1. `python notto/manage.py migrate`
1. `python notto/manage.py runserver`

> The app will be available at http://127.0.0.1:8000
