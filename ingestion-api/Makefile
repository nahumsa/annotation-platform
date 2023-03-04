APP_NAME = "ingestion-api"
VERSION  = 0.1

docker-build-local:
	docker build -t ingestion-api:${VERSION} .

docker-run-local:
	docker run -p 8080:8080  ingestion-api:${VERSION}