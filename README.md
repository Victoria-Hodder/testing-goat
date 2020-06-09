# Purpose

I am using the very brilliant ["Obey The Testing Goat"](https://www.obeythetestinggoat.com) by H. Percival in order to practice Test-driven, full-stack Python/Django development.

# Setup

I assume Python 3.x or higher is installed.

# Tech used

```
Python 3.6.0
Django 1.11.13
selenium 3.141.0
nginx 1.14.0 
gunicorn 20.0.4
```

# Features

A user can create a to-do list.

# Getting it to run

For this project I am using pyenv (you can read about this here: https://github.com/pyenv/pyenv). For example (using linux terminal)

# set up a new environment
`$ pyenv virtualenv 3.8.1 exampleenv `

# activate environment
`$ pyenv activate exampleenv`

In order to install all nececsary libraries please:

`$ pip install -r requirements.txt`

Now run the app by using following command:

`$ python manage.py runserver`

The app should now run on your local server. To test the different endpoints, please go to http://127.0.0.1:8000/

# Testing

The project makes use of unittesting and functional tests.

# Documentation

Django: https://docs.djangoproject.com/en/2.2/

Python: https://docs.python.org/3/

Nginx: https://nginx.org/en/docs/

Gunicorn: https://docs.gunicorn.org/en/stable/ 

# Limitations

- There is not yet a feature to delete items
- Currently I am having to skip test: `test_layout_and_styling` due to possible geckodriver issues