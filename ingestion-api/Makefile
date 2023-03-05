APP_NAME = "ingestion-api"
VERSION  = 0.1

.PHONY: tests

docker-build-local:
	docker build -t i${APP_NAME}ngestion-api:${VERSION} .

docker-run-local:
	docker run -p 8080:8080  ${APP_NAME}:${VERSION}

tests:
	pipenv run pytest

fmt:
	pipenv run isort src/ tests/
	pipenv run black src/ tests/

check_style:
	pipenv run isort --check --diff src/ tests/
	pipenv run black --check --diff src/ tests/
	pipenv run pylint --fail-under=7.0 src/ tests/