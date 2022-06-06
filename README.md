# OCR_P12

## Getting Started

Setup project environment with [venv](https://docs.python.org/fr/3/library/venv.html) and [pip](https://pip.pypa.io).

```bash
$ python3 -m venv env
$ source ./env/bin/activate
$ pip3 install -r ./requirements.txt

$ python3 manage.py makemigrations
$ python3 manage.py migrate

$ python3 manage.py flush # (if necessary)
$ python3 manage.py loaddata fixtures/*
$ python3 manage.py runserver
```