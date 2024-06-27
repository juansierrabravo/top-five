black:
	python3 -m black .

createsuperuser:
	python3 manage.py createsuperuser

pip_freeze:
	python3 -m pip freeze

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

runserver:
	python3 manage.py runserver

shell:
	python3 manage.py shell

test:
	python3 manage.py test

pip:
	python3 -m pip install $(library)