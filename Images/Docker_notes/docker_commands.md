# Docker shell commands
linklist:
[docker run commands](#docker_run)
[docker log files](#specify-log-files)
## Docker infos and service commands
### *Watch out. If user is not in docker group, add 'sudo' to every command*

```console
# shows docker info and device info
docker info
``` 

```console
# ends docker service
sudo systemctl stop docker
``` 

```console
# starts docker service
sudo systemctl start docker
``` 

```console
# starts docker service
sudo systemctl start docker
``` 

```console
# shows info of running containers: e.g. CPU usage, Mem usage
docker stats
``` 

```console
# lists every image on device 
docker images
# or
docker image ls
``` 

```console
# list running containers. Shows container ids
docker ps
``` 

```console
# stops running container
docker stop <container-id>
``` 

```console
# removes container
docker rm <container_id>
``` 

```console
# removes all exited containers
docker rm $(docker ps -a -q  -f status=exited)
``` 

```console
# removes all exited containers
docker rm $(docker ps -a -q  -f status=exited)
``` 

```console
# delete image 
docker image rm nginx
``` 

```console
# removes all stopped containers
docker container prune
# or: remove all images that are created more than 5 minutes ago
# other filters are possible
docker container prune --filter "until=5m"
``` 

```console
# shows log of cointainer
docker logs <cointainer-id> 
``` 

## <a name="docker_run"></a>Docker run examples
```console
# opens an interactive shell in busybox
docker run -it busybox sh

# FLAGS
# set a name for the container to start
--name michelsBox
# detached: runs the container in background and prints container id
-d
# -interactive -tty (pseudo)
-it 

# EXAMPLE
docker run -dit --name michelsbox busybox sh
``` 

```console
# restart options
docker run -dit –restart on-failure busybox sh

# FLAGS
# restart on failure/crash, [maximum number of retries]
--restart=on-failure[:max-retries]
# restart always, unless stopped manually
--restart=unless-stopped
# container starts always: on crash, on system boot, if stopped
--restart=always 

# EXAMPLE
docker run -dit --restart=unless-stopped busybox sh
``` 

```console
# EXAMPLE
# run nginx server and host website
docker run -p 80:80 -m=4m--restart unless-stopped -ti -d -v /home/user/Documents/coding/Docker/nginx_test:/usr/share/nginx/html nginx


# FLAGS
# run nginx server on ports 5000:80 
# (port forwarding: 80 inside, e.g. 5000 to localhost)
-p 5000:80 
-p 80:80 # more common
# hosting a website. Mount a volume like this 
# -v <local folder path>:<nginx home>
-v local/folder/path:/usr/share/nginx/html
# limit usage of RAM
# [b=byte, k=kb, m=Megabyte, g=Gigabyte]
-m 4m
# limit the CPU usage. Number is float
--cpus="0.5"
``` 

## Docker attach

```console
# connect to running container. 
# exit without stopping container
# CTRL-P + CTRL-Q
docker attach <container-id>
```

```console
#  execute container, use bash, in new tty-shell → -ti
docker exec -ti <container-id> bash
```

## Specify Log files 

```console
# path to log files
docker inspect -f {{.LogPath}} <container-id>
``` 

```console
# EXAMPLE
docker run --log-driver json-file --log-opt max-size=100m -p 80:80 -ti -d -v /local/folder/path:/nginx/home/path nginx

# FLAGS 
# specify json as the log file format
--log-driver json-file 
# max file size
--log-opt max-size=100m
# max file number
--log-opt max-file=100
``` 









