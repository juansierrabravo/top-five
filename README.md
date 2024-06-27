## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Features](#features)
  - [Basic Features](#basic-features)
  - [Detailed Features](#detailed-features)
  - [Future Enhancements](#future-enhancements)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
- [Running the Project](#running-the-project)
  - [Set environment variables](#set-environment-variables)
  - [Apply Migrations](#apply-migrations)
  - [Create a Superuser](#create-a-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Testing](#testing)
- [Using the Makefile](#using-the-makefile)

## Introduction
This is a Django project configured to use PostgreSQL as the database. The project is being developed for learning purposes, initially focusing on practicing Test-Driven Development (TDD). It includes comprehensive user management and interactive features for creating and managing user-generated content, such as top lists. Users can register, log in, create, edit, and delete top lists, and interact with others' content through likes and dislikes. The home page showcases the most popular tops. Future enhancements will include practicing SOLID principles, integrating Docker, implementing design patterns, and other advanced software development techniques to improve functionality and user engagement.



## Features
### Basic Features
- **User Authentication and Authorization:** Registration, login, and logout functionalities.
- **Home Page:** Displays the most relevant tops based on likes.
- **User-Generated Content:** Users can create, edit, delete, and view their top lists.
- **Like System:** Users can like or dislike tops, and the most liked tops are prominently displayed.

### Detailed Features
- **User Registration:** Users can register with a username and password.
- **Login and Logout:** Users can log in and log out securely.
- **Top Creation:** Users can create up to five top lists, each containing:
  - Name
  - Optional description
  - List of elements with names, images, and optional descriptions
  - Predefined tags
  - Publication date
- **Top Management:** Users can view, edit, and delete their tops, with verification prompts for deletions.
- **Home Page:** Displays popular tops by day, week, and month, with filter options for name and tag.
- **Top Details:** Viewing a top shows the user who posted it, the publication date, title, description, and elements ranked from 5 to 1.
- **Like System:** Users can like or dislike tops, but not both simultaneously, and only once per top.

### Future Enhancements
- Adding cover images to tops
- Commenting on tops
- Viewing a specific user's tops
- Creating collections of tops
- User profile management (editing profile, uploading photos, etc.)
- Subscription system to follow users and receive notifications
- Social login (Google, Facebook)
- Gamification with points and badges
- Moderation and reporting system
- Content validation before publication
- Social sharing options for tops
- Real-time notifications for likes, comments, new followers, etc.
- Celery and Rabbitmq queue

## Requirements
The project is being developed with the following software versions:
- Python 3.12
- PostgreSQL 16

## Installation
### Clone the Repository
```bash
$ git clone https://github.com/juansierrabravo/top-five.git
$ cd top-five
```

### Create a Virtual Environment
```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
$ pip install -r requirements.txt
```

## Running the Project
### Set environment variables
```bash
$ echo """
SECRET_KEY="YOUR_SECRET_KEY"
""">./.env
```
**Note:** to generate a secret key, use the following Python script:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Apply Migrations
Install [PostgreSQL](https://www.postgresql.org/download/) following the instructions for the specific operating system.

```bash
$ python manage.py migrate
```

### Create a Superuser
```bash
$ python manage.py createsuperuser
```

### Run the Development Server
```bash
$ python manage.py runserver
```

Access the project at `http://127.0.0.1:8000/`.

## Testing
Install [Geckodriver](https://github.com/mozilla/geckodriver) to allow Selenium to inteact with the Firefox web browser (this is for the functional tests).

```bash
$ python manage.py test
```

## Using the Makefile

The project includes a Makefile to simplify common development tasks. Here are the available commands:

- **black**: Formats the code using `black`.
```bash
$ make black
```
- **createsuperuser:** Creates a new superuser for the Django admin.
```bash
$ make createsuperuser
```
- **pip_freeze:** Outputs the current environment's installed packages.
```bash
$ make pip_freeze
```
- **makemigrations:** Creates new migrations based on the changes detected in your models.
```bash
$ make makemigrations
```
- **migrate:** Applies the migrations to the database.
```bash
$ make migrate
```
- **runserver:** Starts the Django development server.
```bash
$ make runserver
```
- **shell:** Opens the Django shell.
```bash
$ make shell
```
- **test:** Runs the tests for the Django project.
```bash
$ make test
```
- **pip:** Installs a Python package using pip.
```bash
$ make make library=<library-name> pip
```