Perfect! I'll keep the same format we've been using for your Docker notes: **commands first (with usefulness)**, then **theory**. These are the notes I'd expect a junior developer to keep for long-term reference.

---

# 🐳 Docker Day 4 Notes — Networking

## 📌 Commands Learned Today

### List all Docker networks

```bash
docker network ls
```

**Purpose:** Shows all Docker networks on your system.

**When to use:**

* Check existing networks
* Verify a network was created
* Debug networking issues

**Importance:** ⭐⭐⭐⭐⭐ (Very Common)

---

### Inspect a Docker network

```bash
docker network inspect bridge
```

or

```bash

docker network inspect my-network
```

**Purpose:** Shows detailed information about a network.

You'll see:

* Driver
* Subnet
* Gateway
* Connected containers
* Network ID

**Importance:** ⭐⭐⭐⭐⭐ (Very Common for debugging)

---

### Create a custom network

```bash
docker network create my-network
```

**Purpose:** Creates a new user-defined bridge network.

**Use when:**

* Multiple containers need to communicate.
* You want automatic container name resolution.
* You want to isolate one project from another.

**Importance:** ⭐⭐⭐⭐☆

---

### Run a container on a specific network

```bash
docker run -dit --name ubuntu1 --network my-network ubuntu bash
```

**Purpose:** Starts a container already connected to a chosen network.

**Importance:** ⭐⭐⭐⭐☆

---

### Open a shell inside a running container

```bash
docker exec -it ubuntu1 bash
```

**Purpose:** Enter a running container to inspect or debug it.

**Importance:** ⭐⭐⭐⭐⭐ (Used constantly)

---

### Update packages inside Ubuntu

```bash
apt update
```

**Purpose:** Refresh package lists.

**Importance:** ⭐⭐⭐☆☆

---

### Install ping utility

```bash
apt install -y iputils-ping
```

**Purpose:** Install the `ping` command inside the container.

**Importance:** ⭐⭐⭐☆☆

---

### Ping another container

```bash
ping ubuntu2
```

**Purpose:** Test communication between containers.

**Importance:** ⭐⭐⭐⭐☆

---

### Build an image

```bash
docker build -t python-server .
```

**Purpose:** Build a Docker image from the current folder.

**Importance:** ⭐⭐⭐⭐⭐ (Daily use)

---

### Run a container with port mapping

```bash
docker run -p 8000:8000 python-server
```

**Purpose:** Publish a container's port so your host machine can access it.

**Format:**

```text
HOST_PORT:CONTAINER_PORT
```

**Importance:** ⭐⭐⭐⭐⭐ (Essential)

---

### View running containers

```bash
docker ps
```

**Purpose:** Shows currently running containers.

**Importance:** ⭐⭐⭐⭐⭐

---

### Stop a running container

```bash
docker stop <container_name_or_id>
```

**Purpose:** Gracefully stops a container.

**Importance:** ⭐⭐⭐⭐⭐

---

### Remove a container

```bash
docker rm <container_name_or_id>
```

**Purpose:** Deletes a stopped container.

**Importance:** ⭐⭐⭐⭐⭐

---

# 📖 Concepts Learned Today

## 1. Docker Network

A Docker network is a **private virtual network** created by Docker that allows containers to communicate with each other securely.

Think of it like a private LAN inside your computer.

```text
Container A  ←→  Docker Network  ←→  Container B
```

Without a network, containers cannot easily communicate.

---

## 2. Default Bridge Network

Docker automatically creates a network called **bridge**.

If you don't specify a network when running a container, Docker connects it to the default bridge network.

This is suitable for simple applications, but professional projects usually use custom bridge networks.

---

## 3. User-Defined Bridge Network

A custom bridge network is a network you create yourself.

Example:

```bash
docker network create my-network
```

Advantages:

* Automatic DNS (container names work as hostnames)
* Better project isolation
* Easier debugging
* Recommended for multi-container applications

---

## 4. Container Name Resolution

Containers on the same user-defined network can communicate using **container names** instead of IP addresses.

Example:

```text
Backend
   │
   ▼
postgres
```

instead of

```text
172.18.0.4
```

Docker automatically translates the container name into its current IP address.

This is more reliable because container IP addresses can change after restarts.

---

## 5. Why Not Use IP Addresses?

Container IP addresses are temporary.

If a container is recreated, its IP may change.

Container names remain the same, so applications continue working without any configuration changes.

This is why professional applications always communicate using container or service names.

---

## 6. Port Mapping

A container has its own private ports.

Your computer cannot access those ports directly.

Port mapping connects a host port to a container port.

Example:

```bash
docker run -p 8000:8000 python-server
```

Meaning:

```text
Browser
      │
localhost:8000
      │
Host Port 8000
      │
Container Port 8000
```

The two ports do **not** have to be the same.

Example:

```bash
docker run -p 5000:8000 python-server
```

This maps host port `5000` to container port `8000`.

---

## 7. EXPOSE Instruction

```dockerfile
EXPOSE 8000
```

`EXPOSE` **does not publish a port**.

It simply documents which port the application inside the image is expected to listen on.

The port only becomes accessible from your host machine when you use:

```bash
docker run -p HOST_PORT:CONTAINER_PORT
```

---

## 8. Docker Networking in Professional Development

Docker networking is used whenever an application consists of multiple services.

Example:

```text
Browser
     │
Frontend
     │
Backend API
     │
Database
```

Each service usually runs in its own container.

Docker networks allow them to communicate securely without exposing every service to the outside world.

---

## 9. Day 3 Connection (Important)

Today also clarified the difference between **bind mounts** and **volumes**:

### 📂 Bind Mount

* Shares a folder between your computer and the container.
* Best for **development**.
* Code changes appear immediately.
* No rebuild required after editing files.

**Think:** *Live coding.*

---

### 💾 Docker Volume

* Managed by Docker.
* Stores important data outside the container.
* Data survives container deletion.
* Commonly used for databases and persistent application data.

**Think:** *Persistent storage, not a backup.*

---

# ⭐ Key Takeaways

* Docker networks let containers communicate securely.
* Professional applications use **user-defined bridge networks**, not the default bridge.
* Containers should communicate using **names**, not IP addresses.
* Port mapping (`-p`) makes a service inside a container accessible from your computer.
* `EXPOSE` documents a listening port but does not publish it.
* **Bind mounts** are for live code during development.
* **Volumes** keep important data safe even when containers are replaced.
* Tomorrow, **Docker Compose** will automate networks, volumes, and multiple containers with a single configuration file.
