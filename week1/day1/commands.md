# Docker Commands - Day 1

## Check Docker installation

```bash
docker --version
```

Displays the installed Docker version.

---

## Download the Hello World image

```bash
docker pull hello-world
```

Downloads the image from Docker Hub.

---

## List downloaded images

```bash
docker images
```

Shows all Docker images stored locally.

---

## Run Hello World

```bash
docker run hello-world
```

Creates and starts a container from the hello-world image.

---

## Show running containers

```bash
docker ps
```

Lists only currently running containers.

---

## Show all containers

```bash
docker ps -a
```

Lists both running and stopped containers.

---

## Remove a stopped container

```bash
docker rm <container-id>
```

Deletes the selected container.

---

## Start an interactive Ubuntu container

```bash
docker run -it ubuntu bash
```

Creates a new Ubuntu container and opens a Bash terminal.

---

## Display current directory

```bash
pwd
```

Shows the current working directory inside Ubuntu.

---

## List files

```bash
ls
```

Displays files and folders.

---

## Show Ubuntu version

```bash
cat /etc/os-release
```

Displays information about the Ubuntu operating system.

---

## Update package lists

```bash
apt update
```

Refreshes Ubuntu's package repository information.

---

## Exit Ubuntu

```bash
exit
```

Closes the Bash shell and stops the container.