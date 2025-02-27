.PHONY: create-superuser migrations setup setup-backend setup-frontend run-backend run-frontend run test help lint

create-superuser:
	cd backend && \
	. .venv/bin/activate && \
	python manage.py createsuperuser

migrations:
	cd backend && \
	. .venv/bin/activate && \
	python manage.py makemigrations && \
	python manage.py migrate

setup: setup-backend setup-frontend
	python3.12 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -r requirements-dev.txt && \
	pre-commit install

setup-backend:
	cd backend && \
	python3.12 -m venv .venv && \
	. .venv/bin/activate && \
	pip install -r requirements-dev.txt

setup-frontend:
	cd frontend && \
	npm install

run-backend:
	cd backend && \
	. .venv/bin/activate && \
	python manage.py runserver

run-frontend:
	cd frontend && npm start

test:
	cd backend && \
	. .venv/bin/activate && \
	python -m unittest discover tests
	cd frontend && \
	npm run test-nowatch

lint:
	. .venv/bin/activate && \
	pre-commit run --all-files

help:
	@echo "Available targets:"
	@echo "  create-superuser ....... Create a superuser for the backend"
	@echo "  migrations ............. Make and apply database migrations"
	@echo "  setup .................. Create a virtual environment and install dependencies"
	@echo "  setup-backend .......... Setup the backend environment"
	@echo "  setup-frontend ......... Setup the frontend environment"
	@echo "  run-backend ............ Run the backend server"
	@echo "  run-frontend ........... Run the frontend server"
	@echo "  test ................... Activate the virtual environment and run unit tests"
	@echo "  help ................... Show this help message"
	@echo "  lint ................... Run all linters via pre-commit"
