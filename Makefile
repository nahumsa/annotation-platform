start-argilla:
	cd argilla/ ; \
	docker compose up -d

build-ingestion-api-docker:
	cd ingestion-api ; \
	make docker-build-local

start-ingestion-api:
	cd ingestion-api ; \
	make docker-run-local

build-serving-api-docker:
	cd serving-api ; \
	make docker-build-local

start-serving-api:
	cd serving-api ; \
	make docker-run-local

start-annotation-platform:
	docker compose up -d