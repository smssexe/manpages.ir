DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-exec - Execute a command in a running container

SYNOPSIS
       docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

DESCRIPTION
       Alias for docker container exec.

OPTIONS
       -d, --detach[=false]	 Detached mode: run command in the background

       --detach-keys=""	     Override the key sequence for detaching a container

       -e, --env=      Set environment variables

       --env-file=	Read in a file of environment variables

       -h, --help[=false]      help for exec

       -i, --interactive[=false]      Keep STDIN open even if not attached

       --privileged[=false]	 Give extended privileges to the command

       -t, --tty[=false]      Allocate a pseudo-TTY

       -u, --user=""	  Username or UID (format: "[:]")

       -w, --workdir=""	     Working directory inside the container

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
