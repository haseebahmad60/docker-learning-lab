# Docker Week 1 Capstone

A small Flask API packaged with Docker and run beside PostgreSQL using Docker Compose. This capstone brings together the image, port, volume, network, environment, and Compose concepts practiced earlier in the week.

## Stack

- Python 3.12
- Flask
- Docker and Docker Compose
- PostgreSQL 17

## Files

```text
|-- app.py           # Flask API
|-- Dockerfile       # Application image
|-- compose.yaml     # Flask and PostgreSQL services
|-- requirements.txt # Python dependency
|-- .env.example     # Disposable local database settings
|-- notes.md         # Learning notes
`-- README.md
```

## Run it

Create the local environment file, then build and start the services:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

Open `http://localhost:5000`. The endpoint returns a JSON message, the container hostname, and the current time.

Useful inspection commands:

```powershell
docker compose ps
docker compose logs
docker compose exec app bash
docker compose exec db psql -U postgres
docker compose down
```

## What I learned

- Building and running a Flask image
- Starting related services through one Compose file
- Compose networking and service discovery
- Named volumes for PostgreSQL data
- Keeping local configuration out of version control

## Limitation

The database service is running, but the Flask application does not yet connect to it. This capstone demonstrates orchestration; database integration is the next step.
