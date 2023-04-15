<h1 align="center">Annotation platform for data-centric NLP</h1>
<p align="center">
<a href="https://github.com/nahumsa/annotation-platform/actions"><img alt="Actions Status" src="https://github.com/nahumsa/annotation-platform/workflows/annotation-platform/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/PyCQA/pylint"><img alt="pylint" src="https://img.shields.io/badge/linting-pylint-yellowgreen"></a>
</p>

The Annotation Platform is an open-source project aimed at providing a scalable and flexible annotation platform using Argilla as the annotation layer. The core idea of the project is to provide a simple and intuitive user interface for annotating on any dataset efficiently.

The platform has two APIs, one for the ingestion layer, and another for the serving layer, to simplify the integration process with other applications. The ingestion API is used to upload data and annotations to the platform, while the serving API is used to retrieve annotations for processed data.

The goal of the Annotation Platform is to make it highly scalable and easy to maintain. Please note that this is still in development, and there may be some limitations or issues as we continue to refine in following versions.

The rough sketch for v1 is in the following figure:

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="docs/v1/Annotation%20platform%20v1.drawio.png"></a>
</p>

# [Ingestion API](ingestion-api/)

This API is designed to simplify the process of posting text to the Argilla server, and is built using the powerful [FastAPI](https://fastapi.tiangolo.com/) framework. Our API also includes a user-friendly HTML interface, making it easy to post text and get started with our annotation platform.

# [Serving API](serving-api/)

This API is designed to provide a fast and efficient way to access the results of our annotation platform, and is built using the powerful [FastAPI](https://fastapi.tiangolo.com/) framework.

# Argilla

I chose to use argilla because I really believe in the project and would like to see if I find any limitations, there are other project such as [Doccano](https://github.com/doccano/doccano) that could be an interesting tool to use. I found that one limitation (until version [1.6.0](https://github.com/argilla-io/argilla/releases/tag/v1.6.0)) is that you would need to use an yaml file to define users and it was pretty cumbersome. However, it was fixed in [v1.6.0](https://github.com/argilla-io/argilla/releases/tag/v1.6.0) by adding a way to store users in a database with an API provided by argilla.


# Running the project
You can run the project using Make and Docker, or just take a look on the makefiles to run the commands. To start the whole platform you can use:

```bash
make start-annotation-platform

```

## Ingestion API
If you want to start the ingestion api server, you can run:

```bash
make build-ingestion-api-docker
make start-ingestion-api
```

## Serving API
If you want to start the serving api server, you can run:

```bash
make build-serving-api-docker
make start-serving-api
```

## Argilla
If you want to start the argilla server, you can run:

```bash
make start-argilla
```
