# Notto

[![Build Status](https://travis-ci.org/renatoliveira/notto.svg?branch=master)](https://travis-ci.org/renatoliveira/notto)

![alt text](https://notto.io/static/img/logo.png)

Notto.io is a simple online text editor that enables anyone to save and edit notes using rich text.

<b>Simply access [Notto](https://notto.io/) and start typing!</b>

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Windows

1. Clone this repo
1. `python -m venv nottoenv`
1. `nottoenv\Scripts\activate`
1. `pip install -r requirements.txt`
1. `python notto\manage.py runserver` or `make build` if you have `make` (installed with MinGW or Cygwin) on your PC.

### Linux/MacOS

1. Clone this repo
1. make build

#### In case you find something wrong...

Sometimes, you might get no errors when running the app for the first time, but find a "no table named nottoapp_note" error,or something like that. If you do so, then use the command `python manage.py migrate --sync-db`. You should see in the console "Synchronizing apps without migrations" and see "Creating table nottoapp_note" below.

> The app will be available at http://127.0.0.1:8000

## Built With
* [Django](https://docs.djangoproject.com/en/2.0/) - The web framework used
* [Quilljs](https://quilljs.com/docs/api/) - An API Driven Rich Text Editor

## Contributing
Please read [CONTRIBUTING.md](https://gist.github.com/tiagosoares94/4b6134673c9dfb2eafc3a5bdf39311b1) for details on our code of conduct, and the process for submitting pull requests to us.

## Author
* Renato Oliveira - initial work - [renatoliveira](https://github.com/renatoliveira)

See also the list of [contributors](https://github.com/renatoliveira/notto/graphs/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/renatoliveira/notto/blob/master/LICENSE) file for details.
