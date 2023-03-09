start-argilla:
	cd argilla \
	docker compose up -d

build-ingestion-api-docker:
	cd ingestion-api \
	make docker-build-local

start-ingestion-api:
	cd ingestion-api \
	make docker-run-local
