# Docker Week 1 Capstone

## Overview

A simple Flask API running alongside PostgreSQL using Docker Compose.

## Technologies Used

- Docker
- Docker Compose
- Python 3.12
- Flask
- PostgreSQL 17

## Folder Structure

```
docker-capstone/
├── app.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── .env
├── README.md
└── notes.md
```

## How to Run

```bash
docker compose up --build
```

Visit:

```
http://localhost:5000
```

## Useful Commands

```bash
docker compose up --build
docker compose down
docker compose ps
docker compose logs
docker compose exec app bash
docker compose exec db psql -U postgres
```

## What I Learned

- Docker Images
- Containers
- Dockerfiles
- Volumes
- Networks
- Docker Compose
- Multi-container applications