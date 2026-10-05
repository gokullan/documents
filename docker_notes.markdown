# Docker

-   Containers
    -   Docker is a tool used to manage containers
    -   Used to run applications in isolated environments on a computer
    -   A 'box' that contains everything our application needs to run
    -   Much lighter than VMs since containers *share* the host's operating system
    -   Runnable instances of images (see below), (i.e.), an isolated process that runs the application as outlined in the image.

-   Images
    -   Blueprints for containers (like a storehouse). They include
        -   Runtime environment
        -   Application code
        -   Dependencies
        -   Config and commands
    -   **READ-ONLY**
    -   Has a separate file-system
    -   Layers (Order matters!)
        -   Parent image
            -   Lightweight OS (?) and runtime environment (eg - node?)
            -   This is a Docker image by itself.
            -   For example, running the NodeJS image (downloaded from
                DockerHub) would give us a Linux environment with node installed
                in it
        -   Source code
        -   Dependencies

## Docker vs. VM
- This can otherwise be reframed as "Docker-engine vs. Hypervisor"
- VMs have a dedicated OS and the Hypervisor enables the VM to use the resources of the host in the manner required by that OS
- Docker-engine interfaces directly with the kernel, (i.e.), there is no new OS-layer in-between the Engine and the kernel<sup>+</sup>
- Emulator vs. Hypervisor
  - Emulator is a *software* that is used to replicate a hardware-architecture that is completely different from the host
  - Hypervisor is also a software, but uses hardware-assisted technologies (on-chip) to help *isolate and execute* instructions of a different OS that uses the same chip-architecture
    - See more on "trap and emulate"
- WSL2: Since Docker is linux-based, running it on Windows requires a Linux VM in the first place!
- QEMU: Acts as both an emulator and a hypervisor "sidekick"

<sup>+</sup> Technically, the Docker Engine does not sit between the container and the kernel. Instead, the containers themselves interface directly with the host kernel. The Docker Engine is simply the management tool (the orchestrator) that configures the Linux namespaces and cgroups. Once the containerized process starts, the Docker Engine steps out of the way, and the process talks directly to the host kernel just like any other native software.

## Dockerfile
-   Set of instructions (adding layers to parent image) to create Docker image
```dockerfile
# parent image
# pulled locally or from hub
FROM node:17-alpine

# all image-paths specified here will be relative to this:
WORKDIR /app

# copy source code 
# COPY <source-code-path relative to this Dockerfile> <path in image>
COPY . .

# install dependencies
RUN npm install

# specify port number (for Docker Desktop port-mapping)
EXPOSE 4000

# runtime commands
CMD ["node", "app.js"]
```
-   To build the image, use `docker build -t my-image-name <path-to-Dockerfile>`
-   Add `--rm` to remove the container after stopping it

## [Layer caching](https://docs.docker.com/build/cache/)
-   Every line in the Dockerfile progressively add a layer to the image 
-   The snapshot of the image at each layer is cached so that it can be built
    easily the next time
-   Below is an efficient way to build NodeJS containers easily if there are
    modifications to the source code (but not the dependencies)
```dockerfile
# ...
COPY package.json .

RUN npm install

COPY . .

# ...
```

## Volumes
- Persisting data when using Docker-containers can be done in 2 ways => volume-mount and bind-mount
- Bind-mount is used to map directories used by the constainer to those on the user's file-system; here ownership of the directory is with the user, not Docker 
  - `docker run -v /absolute/path/to/host/directory:/container/directory image` (`-v` => `--mount type=bind,src=...,dst=...`; `dst` is the always the container-path)
- Volume-mount also does the same; but here the ownership is with Docker and is "hidden" from the user (these files expected to be accessed only via docker-commands); this is much faster that bind-mount
  - `docker run ... -v /container/directory/folder ... image` (`-v` => `--mount type=volume,src=...,dst=...`)
  - This is again of 2 types: anonymous volume (above) and named-volume

## `docker compose`
-   Below is an example of `docker-compose.yaml`
```yaml
version: "24.0.5"
services:
  api:
   build: ./dockerfilePath
   container_name: "container1"
   ports:
    - '4000:4000'
   volumes:
    - ./api:/app
    - /app/node_modules
```
-   `docker compose up` will create the images and containers
-   `docker compose down` will delete the containers (but not the images and
    volumes)
-   Add `-rmi all -v` to delete images and volumes as well

## Commands
-   `docker container stats`
-   `docker images ls` OR `docker images`
-   `docker rmi image-name` to remove images
-   `docker ps` to list active processes (running containers?)
-   `docker build -t my-image-name ./Dockerfile_path` to build image 
-   `docker run --name my-container-name -p 4000:3000 -d image-name` to create a
    container that exposes its port 3000 and maps it to the host's port 4000
-   `docker stop container-name`
-   `docker rm container-name`
-   `docker system prune`
-   `docker exec -it container-name` /bin/bash
    -   It is sometimes `/bin/sh`
    -   [Reference](https://stackoverflow.com/questions/26153686/how-do-i-run-a-command-on-an-already-existing-docker-container)
 
## Doubts
-   Can an application developed for Windows be run on a container in Linux?
-   How does mouting volumes work (Why do `COPY`?`)?
-   How to enter container terminal?
-   `--expose` vs `-p` vs `EXPOSE` on Dockerfile
    -   [Reference](https://stackoverflow.com/questions/40801772/what-is-the-difference-between-ports-and-expose-in-docker-compose)
-   Docker with NodeJS and Postgres -
    [1](https://kundan-9343.medium.com/node-js-rest-api-setup-with-docker-compose-express-and-postgres-d53fb0c77da7),
    [2](https://dev.to/chandrapantachhetri/docker-postgres-node-typescript-setup-47db)
