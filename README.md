# Docker Learning Lab

A seven-day hands-on introduction to Docker. The repository records the commands, small Python services, Dockerfiles, volumes, networks, and Compose configurations I used while learning container fundamentals.

This is a learning journal rather than a production deployment template.

## Week 1 progression

| Day | Focus | Artifact |
| --- | --- | --- |
| 1 | Images, containers, and core CLI commands | Command and concept notes |
| 2 | Building a custom image | Python app and Dockerfile |
| 3 | Persistent and bind-mounted data | Counter example and notes |
| 4 | Container networking | Networked Python example |
| 5 | Docker Compose | Single-service Compose application |
| 6 | Multiple services and environment files | Flask and PostgreSQL services |
| 7 | Capstone review | Flask API, Compose, PostgreSQL service, and runbook |

## What the lab demonstrates

- Building images from Dockerfiles
- Mapping host and container ports
- Using bind mounts and named volumes
- Creating and inspecting container networks
- Defining services with Docker Compose
- Supplying configuration through environment files
- Running a Flask service alongside PostgreSQL

## Run the capstone

Docker Desktop or another Docker Engine with Compose support is required.

```powershell
git clone https://github.com/haseebahmad60/docker-learning-lab.git
cd docker-learning-lab/week1/day7
Copy-Item .env.example .env
docker compose up --build
```

Open `http://localhost:5000`, then stop the services with:

```powershell
docker compose down
```

The sample credentials are intended only for local learning. Choose different values for any environment that is not disposable.

## Current limitation

The Day 6 and Day 7 Compose files start both Flask and PostgreSQL, but the Flask examples do not yet open a database connection. The next meaningful step is to add a health check and a small persistence flow, then verify it with integration tests.

## Repository hygiene

Real `.env` files are ignored. Each multi-service example includes an `.env.example` containing disposable local placeholders that can be copied before running the stack.

## License

No license has been selected yet.
