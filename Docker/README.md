# Docker Commands

A list of basic Docker commands.

| Command | Description |
| ----- | ----- |
| docker run [--interactive --tty] `image name` | Get a Docker image locally or pull it from Docker Hub and run a container. `--interactive --tty`: run an interactive terminal inside the spawned container. |
| docker stop `container names` | Stop one or more running containers. |
| docker build [-t="`docker repo`"] . | Build an image from a Dockerfile. `-t` sets a name and optionally a tag in the ‘name:tag’ format. |
| docker image ls | List all images available. |
| docker container ls [--all] | List all running containers (default). With `--all` also lists containers that are not running. |
| docker rm `name` / docker container rm `name` | Remove one or more **containers** by their names. |
| docker rmi `name or ID` / docker image rm `name or ID` | Remove one or more **images** by their names or IDs. |
| docker login --username=`username` --password="`password`" | Log in to a Docker registry (Docker Hub). |
| docker tag `image name`:`tag` `url` | Associate the image with a given version tag with a particular url repository. |
| docker push `docker repo` | Push an image or a repository to a registry (e.g. DockerHub, Amazon ECR, etc.) |

## Docker Swarm

A list of useful commands to orquestrate containers with Docker Swarm.

| Command | Description |
| ----- | ----- |
| docker service create --replicas `number` [--name `service id`] [--update-delay `interval`] [--update-parallelism `number`] `image:version` | Deploy a Docker image to the swarm. `--update-delay` configures the rolling update policy. `--update-parallelism` configure the maximum number of service tasks simultaneously updated. |
| docker service inspect --pretty `service id` | Inspect a service. |
| docker service update --image `image:version` `service id` | Update the container image. |
| docker service ps `service id` | Display the rolling update. |

## Dockerfile Syntax

The basic syntax rules of a Dockerfile.

| Element | Description |
| ----- | ----- |
| Backslash (`\`) | escape character (spanning multiple lines). |
| Backtick (`) | escape character (spanning multiple lines). |
| FROM | Base image from which new image will be created. |
| COPY | Copy folders or files to container filesystem. |
| ADD | Similar to COPY; can also pull items from a URL. |
| WORKDIR | Sets the working directory. |
| CMD | Runs a command when container is launched. |
| RUN | Runs commands whose results become a part of the image. |
