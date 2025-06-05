# Python Exercice

## Create a network

```bash
docker network create my-network || true
```

## Run a PostgreSQL Server

```bash
docker run -d \
  --name pg \
  --network my-network \
  -p 5432:5432 \
  -e POSTGRES_DB=dbname \
  -e POSTGRES_USER=dbuser \
  -e POSTGRES_PASSWORD=*** \
  postgres:17-alpine
```

## Run this project as server

```bash
docker run -d \
  --name unicorn-server \
  --network my-network \
  -p 8000:8000 \
  ghcr.io/kinafz/python:latest
```

## Run this test project as client

```bash
docker run \
  --name monitor-container \
  --network my-network \
  -e DB_USER=dbuser \
  -e DB_PASSWORD=*** \
  -e DB_HOST=pg \
  -e DB_PORT=5432 \
  -e DB_NAME=dbname \
  -e API_URL=http://unicorn-server:8000 \
  -e APPS=app1,app2,app3 \
  -e API_TOKEN=*** 
```