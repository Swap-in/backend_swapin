# API DJango - Swap.in - Documentación

This provides an specification file for the Swapin Api

> Description and use of the API - Swap.in - Final Project Platzi Master

[![django version](https://img.shields.io/badge/django%20versions-1.11%20%7C%202.0%20%7C%202.1-blue)](https://www.djangoproject.com/) [![github release version](https://img.shields.io/github/v/release/c3-zally/api-python.svg?include_prereleases)](https://github.com/c3-zally/api-python/releases/latest)  [![license](https://img.shields.io/github/license/c3-zally/api-python.svg)](https://github.com/c3-zally/api-python/blob/master/LICENSE)  [![PRs welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg)](https://github.com/c3-zally/api-python/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)

## Starting 🚀

<!-- _These instructions will allow you to get a copy of the project running on your local machine for development and testing purposes._ -->


## Pre-requirements 📋
You need install and use:
```
Python3
pip3
```

## Installation 🔧
Install the requirements and execute the env and install the requirements.
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Local execution
```
python3 manage.py migrate
python3 manage.py runserver
```

## Deployment 📦

CD automatic with Heroku: https://swapin.herokuapp.com/

| ENDPOINT | DESCRIPTION |
| ------------- | ------------- |
| home/ | Cooming soon  |
| users/signup/  | Cooming soon  |
| users/login/ | Cooming soon  |
| users/verify/ | Cooming soon  |
| users/list_clothes/<int:id>/  | Cooming soon  |
| clothes/like/  | that is responsible for creating the like, the notification and return whether or not it was a match |
| clothes/notification_user/<int:id>/  | that is responsible for obtaining notifications by user, when it is a match it returns true or false, if it is true it returns the phone number to be able to teach the match  |
| clothes/notification_clothe/<int:id>/  | that is responsible for bringing the list of notifications for clothing  |
| clothes/notification_read/  | that is responsible for saving the notification is read  |
| clothes/get_categories/  | that is responsible for returning the list of clothing categories  |
| clothes/search_clothes/<int:id_category>/<int:id_user>/  | that is responsible for returning the result of the clothes by category  |



## Licencia 📄

Este proyecto está bajo la Licencia (MIT) - mira el archivo [LICENSE.md](LICENSE.md) para detalles



