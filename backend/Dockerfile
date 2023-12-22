## Use the official Python image as a base image
#FROM python:3.11-slim
#
## Set the working directory to /app
#WORKDIR /bank
#
## Copy the poetry.lock and pyproject.toml files into the container
#COPY poetry.lock pyproject.toml ./
#
## Install Poetry and project dependencies
#RUN pip install poetry && poetry install --no-root
#
## Copy the entire project directory into the container
#COPY . .
#
## Expose port 8000 for the Flask application
#EXPOSE 5000
#
## Command to run the application using Poetry
#CMD ["poetry", "run", "python", "bank"]


FROM python:3.11.3-slim-buster as prod


RUN pip install poetry==1.4.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install --only main

# Copying actuall application
COPY . /app/src/
RUN poetry install --only main

RUN poetry run flask --app bank/__main__.py db upgrade head


CMD ["/usr/local/bin/python", "-m", "bank"]

FROM prod as dev

RUN poetry install