.PHONY: setup dev lint fix_lint format build_image test test_with_ci start_depend stop_depend clean help

setup:
	poetry check
	poetry check --lock
	poetry install

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

start_depend:
	cd depends && docker compose up -d --remove-orphans

stop_depend:
	cd depends && docker compose stop

clean:
	rm ./logs ./report ./htmlcov

help:
	@echo "setup: install dependencies"
	@echo "dev: run uvicorn server"
	@echo "lint: lint check"
	@echo "fix_lint: fix lint"
	@echo "format: format code"
	@echo "build_image: build docker image"
	@echo "test: run test"
	@echo "test_with_ci: run test with ci"
	@echo "start_depend_service: start depend service"
	@echo "clean: clean logs, report and htmlcov"
	
