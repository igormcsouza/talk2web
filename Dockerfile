# Build stage
FROM python:3.11.8 AS builder

COPY dependencies.sh /opt/dependencies.sh
RUN chmod +x /opt/dependencies.sh
RUN sh /opt/dependencies.sh

RUN pip install poetry

WORKDIR /home/app

COPY pyproject.toml poetry.lock README.md /home/app/
RUN poetry config virtualenvs.create false && poetry install --only main \
    && poetry cache clear pypi --all

# Runtime stage
FROM python:3.11.8-slim

WORKDIR /home/app

COPY --from=builder /usr/local /usr/local

COPY . /home/app

EXPOSE 8501

CMD ["poetry", "run", "task", "start"]
