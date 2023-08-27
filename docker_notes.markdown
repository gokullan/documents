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
-   Used to map a directory in a container to a host directory
-   `docker run -v /absolute/path/to/host/directory:/container/directory image`
-   To prevent mapping of any folder to the host, create an anonymous volume
    `docker run ... -v /container/directory/folder ... image`

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

## Doubts
-   Can an application developed for Windows be run on a container in Linux?
-   How does mouting volumes work (Why do `COPY`?`)?
-   How to enter container terminal?
