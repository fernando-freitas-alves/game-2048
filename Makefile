.PHONY: setup run test help lint

setup:
	python3.10 -m venv .venv
	.venv/bin/pip install -r requirements-dev.txt

run:
	.venv/bin/python -m game_2048.main

test:
	.venv/bin/python -m unittest discover tests

help:
	@echo "Available targets:"
	@echo "  setup - Create a virtual environment and install dependencies"
	@echo "  run   - Activate the virtual environment and run the game"
	@echo "  test  - Activate the virtual environment and run unit tests"
	@echo "  help  - Show this help message"
	@echo "  lint  - Run all linters via pre-commit"

lint:
	. .venv/bin/activate && \
	 pre-commit run --all-files
