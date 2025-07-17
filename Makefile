test:
	poetry run pytest --cov=acangatu tests/ --cov-report term-missing

build:
	poetry build
