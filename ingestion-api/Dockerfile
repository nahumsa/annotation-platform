FROM python:3.10

COPY Pipfile* ./

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

COPY src /src/

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]