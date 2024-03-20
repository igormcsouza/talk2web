FROM python:3.11.8-slim

COPY dependencies.sh /opt/dependencies.sh
RUN chmod +x /opt/dependencies.sh
RUN sh /opt/dependencies.sh

RUN pip install poetry

WORKDIR /home/app

COPY . /home/app

RUN poetry config virtualenvs.create false && poetry install --only main

EXPOSE 8501

CMD ["poetry", "run", "task", "start"]
