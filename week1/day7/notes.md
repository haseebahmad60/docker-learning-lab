# Docker Week 1 Revision Notes

## Docker Architecture

- Docker Desktop provides the interface.
- Docker Engine builds and runs containers.
- Docker Hub stores ready-made images.

---

## Images vs Containers

Image:
- Blueprint
- Read-only template
- Can create many containers

Container:
- Running instance of an image
- Temporary unless data is stored in volumes

---

## Dockerfile Instructions

FROM
- Selects the base image.

WORKDIR
- Sets the working directory.

COPY
- Copies files into the image.

RUN
- Executes commands while building the image.

EXPOSE
- Documents the application's port.

CMD
- Runs when the container starts.

---

## Storage

### Bind Mount

- Shares files between your computer and the container.
- Best for development.

Example:

```bash
-v .:/app
```

### Named Volume

- Stores persistent data outside containers.
- Best for databases.

Example:

```yaml
volumes:
  - postgres-data:/var/lib/postgresql/data
```

---

## Networking

Compose creates a private network.

Containers communicate using service names.

Example:

```text
app -----> db
```

Do **not** use `localhost` between containers.

---

## Docker Compose

```bash
docker compose up
```

Starts services.

```bash
docker compose up --build
```

Rebuilds images and starts services.

```bash
docker compose down
```

Stops and removes containers and the Compose network.

```bash
docker compose ps
```

Lists running services.

```bash
docker compose logs
```

Shows container logs.

---

## Commands to Remember

```bash
docker build -t app .
docker images
docker run app
docker ps
docker ps -a
docker stop <container>
docker rm <container>
docker logs <container>
docker exec -it <container> bash

docker network ls
docker network inspect <network>

docker volume ls

docker compose up
docker compose up --build
docker compose down
docker compose ps
docker compose logs
docker compose exec app bash
docker compose exec db psql -U postgres
```

---

## Key Takeaways

- Docker solves "works on my machine" problems.
- Images are blueprints.
- Containers are running applications.
- Dockerfiles build images.
- Compose manages multiple containers.
- Bind mounts are for development.
- Named volumes preserve database data.
- Containers communicate through Docker networks.