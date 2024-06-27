## Table of Contents

- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Features](#features)
  - [Core Offerings:](#core-offerings)
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
Welcome to this innovative Django project, crafted specifically to sharpen and showcase a myriad of software development skills to potential employers and collaborators. This project serves as a dynamic playground for mastering Test-Driven Development (TDD) and will evolve to encapsulate a broader spectrum of advanced programming concepts. At its core, the application boasts a sophisticated user management system paired with interactive functionalities that allow users to create, modify, and engage with top lists. From registering and logging in to voting on content with likes and dislikes, the platform is designed to highlight popular user-generated content right on the homepage. As the project progresses, expect to see the integration of SOLID principles, Docker, and various design patterns, enhancing both functionality and user interaction. This ongoing enhancement aims to not only demonstrate technical proficiency but also a commitment to continuous learning and improvement in software development.

## Features
### Core Offerings:
- **User Authentication:** Seamless registration, login, and logout experiences.
- **Dynamic Home Page:** Displays popular tops by day, week, and month, with filter options for name and tag.
- **User-Generated Content:** Your stage to create, modify, and showcase top lists that capture your unique perspective.
- **Engagement Tools:** Thrive in our community with a robust like and dislike system to express your opinions and influence trends.

### Future Enhancements
- **Interactive Comments:** Discuss and connect directly on top list pages.
- **Personalized Collections:** Create and manage collections of your favorite tops.
- **Enhanced Profiles:** More tools to personalize your profile and manage your presence.
- **Engagement Beyond the Platform:** From social logins to sharing on networks, we’re expanding ways you can connect and share.
- **Gamify Your Experience:** Earn points, unlock badges, and climb the leaderboard!
- **Moderation and Reporting:** Ensuring a safe and respectful community with tools for moderation and reporting.
- **Social Sharing:** Share your top lists easily across social media platforms.
- **Real-Time Notifications:** Stay updated with instant notifications for likes, comments, new followers, and more.

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
$ cp .env.example .env # Then, open the .env file and change the placeholder <CHANGE-ME> for the real values
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