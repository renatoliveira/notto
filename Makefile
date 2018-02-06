.PHONY: install lint test venv run build

lint:
	flake8

install:
	pip install -r requirements.txt

test:
	python notto/manage.py test notto

venv:
	python3 -m venv nottoenv

source:
	. nottoenv/bin/activate

makemigrations:
	python notto/manage.py makemigrations nottoapp

migrate:
	python notto/manage.py migrate

run:
	python notto/manage.py runserver

build:
	$(MAKE) venv
	$(MAKE) source
	$(MAKE) install
	$(MAKE) makemigrations
	$(MAKE) migrate
	$(MAKE) run
