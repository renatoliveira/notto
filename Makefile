.PHONY: install lint test venv run build

lint:
	flake8

install:
	pip3 install -r requirements.txt

test:
	python notto/manage.py test notto --settings=notto.settings.development

venv:
	python3 -m venv nottoenv

source:
	. nottoenv/bin/activate

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
	$(MAKE) run
