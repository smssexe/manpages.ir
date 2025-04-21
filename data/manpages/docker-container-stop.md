DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-container-stop - Stop one or more running containers

SYNOPSIS
       docker container stop [OPTIONS] CONTAINER [CONTAINER...]

DESCRIPTION
       Stop a container (Send SIGTERM, and then SIGKILL after grace period)

OPTIONS
       -h, --help[=false]      help for stop

       -s, --signal=""	    Signal to send to the container

       -t, --timeout=0	    Seconds to wait before killing the container

SEE ALSO
       docker-container(1)

Docker Community							   Mar 2025								     DOCKER(1)
