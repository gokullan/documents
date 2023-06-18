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

## Commands
-   `docker container stats`
-   `docker images ls`

## Doubts
-   Can an application developed for Windows be run on a container in Linux?
