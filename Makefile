.PHONY: help clean build_image test lint format check_style dev

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

clean:
	rm ./logs ./report ./htmlcov

help:
	echo "help"