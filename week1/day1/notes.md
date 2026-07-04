# Docker Fundamentals - Day 1

## What is Docker?

Docker is a platform that allows developers to package an application along with all of its dependencies, libraries, and configurations into a container. This ensures the application runs consistently on any computer without environment-related issues.

---

## What problem does Docker solve?

Docker solves the common problem of:

> "It works on my machine."

Applications often fail on another computer because of different operating systems, library versions, or missing dependencies. Docker packages everything needed to run the application, making it portable and consistent.

---

## What is a Docker Image?

A Docker image is a read-only template that contains everything needed to run an application.

It includes:

- Application code
- Runtime (Python, Node.js, etc.)
- Libraries
- Dependencies
- Configuration files

An image cannot run by itself.

Think of it like a recipe.

---

## What is a Docker Container?

A container is a running instance of a Docker image.

When an image is executed using `docker run`, Docker creates a container.

Containers are:

- Lightweight
- Isolated
- Fast
- Portable

Think of a container as the finished meal created from a recipe.

---

## Docker Image vs Docker Container

| Image | Container |
|--------|-----------|
| Blueprint or template | Running application |
| Read-only | Can change while running |
| Cannot execute by itself | Executes the application |
| Can create many containers | Created from an image |

---

## Container vs Virtual Machine

### Docker Container

- Shares the host operating system kernel
- Starts in seconds
- Uses less RAM
- Lightweight
- Best for applications

### Virtual Machine

- Includes a complete operating system
- Starts slowly
- Uses more RAM and storage
- Heavier
- Best for running different operating systems

---

## Docker Engine

Docker Engine is the software responsible for creating, running, and managing Docker containers.

When we type Docker commands, the Docker CLI communicates with Docker Engine.

---

## Docker Hub

Docker Hub is Docker's online repository where users can download and share Docker images.

Examples:

- Ubuntu
- Python
- MySQL
- Nginx
- Redis

Command example:

```bash
docker pull ubuntu
```

downloads the Ubuntu image from Docker Hub.

---

## Basic Docker Workflow

1. Download an image

```bash
docker pull ubuntu
```

2. Create and run a container

```bash
docker run ubuntu
```

3. View running containers

```bash
docker ps
```

4. View all containers

```bash
docker ps -a
```

5. Remove a stopped container

```bash
docker rm <container-id>
```

---

## Important Docker Commands

Check Docker version

```bash
docker --version
```

Download an image

```bash
docker pull hello-world
```

List downloaded images

```bash
docker images
```

Run a container

```bash
docker run hello-world
```

Show running containers

```bash
docker ps
```

Show all containers

```bash
docker ps -a
```

Remove a container

```bash
docker rm <container-id>
```

Start an interactive Ubuntu container

```bash
docker run -it ubuntu bash
```

Exit a container

```bash
exit
```

---

## Key Takeaways

- Docker packages applications and dependencies together.
- Images are templates.
- Containers are running images.
- One image can create many containers.
- Docker Hub stores Docker images online.
- Containers are much lighter than virtual machines.