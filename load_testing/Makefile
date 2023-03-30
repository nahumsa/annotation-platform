APP_NAME = "load-testing"
VERSION  = 0.1

.PHONY: tests

load_test_ingestion_api:
	locust -f locustfile.py IngestionAPIUser

load_test_serving_api:
	locust -f locustfile.py ServingAPIUser

load_test_all:
	locust

fmt:
	pipenv run isort src/ tests/
	pipenv run black src/ tests/

check_style:
	pipenv run isort --check --diff src/ tests/
	pipenv run black --check --diff src/ tests/
	pipenv run pylint --fail-under=7.0 src/ tests/