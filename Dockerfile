FROM python:3.8-alpine AS builder
WORKDIR /app
COPY . /app
RUN pip install -I pipenv==2022.10.25

FROM builder AS development
RUN pipenv install --dev
EXPOSE 4444

FROM builder AS production
RUN pipenv install
