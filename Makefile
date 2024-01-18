.PHONY: setup fix_lock dev lint format build_image test test_with_ci clean help

setup:
	poetry check
	poetry check --lock
	poetry install --sync

fix_lock:
	poetry lock

dev:
	poetry run uvicorn robot33.main:app	--reload --port=8888

lint:
	poetry run ruff check ./robot33 ./tests

format:
	poetry run ruff format ./robot33 ./tests
	poetry run ruff --fix ./robot33 ./tests

build_image:
	docker build -t robot33 . --name robot33

test:
	poetry run pytest --html=report/report.html --cov=./robot33 ./tests/ --cov-report=html --cov-report=term

test_with_ci:
	poetry run pytest --cov=./robot33 ./tests/ --cov-report=xml

clean:
	rm ./logs ./report ./htmlcov

help:
	@echo "setup: install dependencies"
	@echo "fix_lock: fix lock file"
	@echo "dev: run uvicorn server"
	@echo "lint: lint check"
	@echo "format: format code"
	@echo "build_image: build docker image"
	@echo "test: run test"
	@echo "test_with_ci: run test with ci"
	@echo "clean: clean logs, report and htmlcov"
	
