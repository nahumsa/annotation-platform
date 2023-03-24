APP_NAME = "serving-api"
VERSION  = 0.1

.PHONY: tests

docker-build-local:
	docker build -t ${APP_NAME}:${VERSION} .

docker-run-local:
	docker run --add-host=host.docker.internal:host-gateway -d -p 8080:8080 ${APP_NAME}:${VERSION}

connect-to-argilla-network:
	docker network connect argilla_argilla ${APP_NAME}

tests:
	pipenv run pytest

fmt:
	pipenv run isort src/ tests/
	pipenv run black src/ tests/

check_style:
	pipenv run isort --check --diff src/ tests/
	pipenv run black --check --diff src/ tests/
	pipenv run pylint --fail-under=7.0 src/ tests/