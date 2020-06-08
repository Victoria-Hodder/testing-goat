# Purpose

I am using the very brilliant ["Obey The Testing Goat"](https://www.obeythetestinggoat.com) by H. Percival in order to practice TDD full stack Python/Django development.

# Setup

I assume Python 3.x or higher is installed.

# Tech used

```
Python 3.6.0
Django 1.11.13
```

# Features

A user can create a to-do list

# Getting it to run

For this project I am using pyenv (you can read about this here: https://github.com/pyenv/pyenv). For example (using linux terminal)

# set up a new environment
$ pyenv virtualenv 3.8.1 exampleenv 

# activate environment
$ pyenv activate exampleenv

In order to install all nececsary libraries please:

`$ pip install -r requirements.txt`

Now run the app by using following command:

`$ python manage.py runserver`

The app should now run on your local server. To test the different endpoints, please go to http://127.0.0.1:8000/

# Testing

The project makes use of unittesting.

# Documentation

For the Django Documentation: https://docs.djangoproject.com/en/2.2/

For Python Documentation: https://docs.python.org/3/