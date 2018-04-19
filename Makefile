.PHONY: install lint test venv run build

lint:
	flake8

install:
	pip install -r requirements.txt

test:
	python notto/manage.py test notto --settings=notto.settings.development

venv:
	python3 -m venv nottoenv

source:
	. nottoenv/bin/activate

makemigrations:
	python notto/manage.py makemigrations nottoapp

migrate:
	python notto/manage.py migrate --run-syncdb

run:
	python notto/manage.py makemigrations --settings=notto.settings.development
	python notto/manage.py migrate --settings=notto.settings.development
	python notto/manage.py runserver --settings=notto.settings.development

run-production:
	python notto/manage.py makemigrations --settings=notto.settings.production
	python notto/manage.py migrate --settings=notto.settings.production
	python notto/manage.py runserver --settings=notto.settings.production

build:
	$(MAKE) venv
	$(MAKE) source
	$(MAKE) install
	$(MAKE) makemigrations
	$(MAKE) migrate
	$(MAKE) run
