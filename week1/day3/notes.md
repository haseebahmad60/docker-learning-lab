# Day 3 Notes: Docker Volumes & Bind Mounts

## Container Filesystem
A container has its own temporary filesystem. Files created inside a container do not appear on the host unless we use a bind mount or volume.

## Bind Mount
A bind mount connects a folder from the host machine to a folder inside the container.

Example:
docker run --rm -v ${PWD}:/app counter-app

Use bind mounts during development because code changes on the host appear immediately inside the container.

## Named Volume
A named volume is storage managed by Docker.

Example:
docker volume create counter-data
docker run --rm -v counter-data:/app counter-app

Use named volumes for persistent data such as databases, uploaded files, and app data.

## Difference
Bind mount = host folder shared with container.
Named volume = Docker-managed storage.

## Useful Commands
docker volume ls
docker volume create counter-data
docker volume inspect counter-data
docker volume rm counter-data
docker system df