<h1 align="center">Annotation platform for data-centric NLP</h1>
<p align="center">
<a href="https://github.com/nahumsa/annotation-platform/actions"><img alt="Actions Status" src="https://github.com/nahumsa/annotation-platform/workflows/annotation-platform/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336"></a>
<a href="https://github.com/PyCQA/pylint"><img alt="pylint" src="https://img.shields.io/badge/linting-pylint-yellowgreen"></a>
</p>

The Annotation Platform is an open-source project aimed at providing a scalable and flexible annotation platform using Argilla as the annotation layer. The core idea of the project is to provide a simple and intuitive user interface for annotating on any dataset efficiently.

The platform has two APIs, one for the ingestion layer, and another for the serving layer, to simplify the integration process with other applications. The ingestion API is used to upload data and annotations to the platform, while the serving API is used to retrieve annotations for processed data.

The goal of the Annotation Platform is to make it highly scalable and easy to maintain.

The rough sketch for v1 is in the following figure:

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="docs/v1/Annotation%20platform%20v1.drawio.png"></a>
</p>

# [Ingestion API](ingestion-api/)

The ingestion API is written using [FastAPI](https://fastapi.tiangolo.com/) and has a simple HTML interface that works for posting text to the Argilla server.

# Argilla

I chose to use argilla because I really believe in the project and would like to see if I find any limitations, there are other project such as [Doccano](https://github.com/doccano/doccano) that could be an interesting tool to use.


# Running the project
You can run the project using Make and Docker, or just take a look on the makefiles to run the commands.

## Ingestion API
If you want to start the ingestion api server, you can run:

```bash
make build-ingestion-api-docker
make start-ingestion-api
```

## Argilla
If you want to start the argilla server, you can run:

```bash
make start-argilla
```



