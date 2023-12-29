.PHONY: setup dev check_style format lint build_image test test_with_ci clean help

setup:
	poetry install

dev:
	poetry run uvicorn robot33.main:app	--reload --port=8888

check_style:
	poetry run black ./robot33 ./tests --check

format:
	poetry run black ./robot33 ./tests

lint:
	poetry run flake8 ./robot33 ./tests

build_image:
	docker build -t robot33 .

test:
	poetry run pytest --html=report/report.html --cov=./robot33 ./tests/ --cov-report=html --cov-report=term

test_with_ci:
	poetry run pytest --cov=./robot33 ./tests/ --cov-report=xml

clean:
	rm ./logs ./report ./htmlcov

help:
	@echo "setup: install dependencies"
	@echo "dev: run uvicorn server"
	@echo "check_style: check code style"
	@echo "format: format code style"
	@echo "lint: lint code"
	@echo "build_image: build docker image"
	@echo "test: run test"
	@echo "clean: clean logs, report and htmlcov"
	
