# java server monitor [!["Push docker" workflow image](https://github.com/Smarter-Servers/server-monitor/actions/workflows/push-docker-image.yml/badge.svg)](https://github.com/Smarter-Servers/server-monitor/actions/workflows/push-docker-image.yml)
Monitor a java server with ease.

### Technologies used
  - Docker
  - Poetry
  - Python (3.9)

### Docker
```bash
docker build -t <image-name> .
```

Run the docker container with
```bash
docker run <image-name> -h <host> -p <port>
```
The server will default to a host value of `127.0.0.1` and port value of `25565` if none are provided.

See additional options [here](https://docs.docker.com/engine/reference/run/#docker-run-reference).

View the [docker registry for the project](https://hub.docker.com/r/smarterservers/minecraft-java-server-monitor).

## Exit codes
  - `0`: No players are connected
  - `1`: Some players are connected