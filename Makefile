black:
	./venv/bin/python -m black .

createsuperuser:
	./venv/bin/python manage.py createsuperuser

pip_freeze:
	./venv/bin/python -m pip freeze

makemigrations:
	./venv/bin/python manage.py makemigrations

migrate:
	./venv/bin/python manage.py migrate

runserver:
	./venv/bin/python manage.py runserver

shell:
	./venv/bin/python manage.py shell

test:
	./venv/bin/python manage.py test

pip:
	./venv/bin/python -m pip install $(library)

startapp:
	./venv/bin/python manage.py startapp $(name) $(path)