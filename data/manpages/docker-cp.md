DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-cp - Copy files/folders between a container and the local filesystem

SYNOPSIS
       docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-      docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH

DESCRIPTION
       Alias for docker container cp.

OPTIONS
       -a, --archive[=false]	  Archive mode (copy all uid/gid information)

       -L, --follow-link[=false]      Always follow symbol link in SRC_PATH

       -h, --help[=false]      help for cp

       -q, --quiet[=false]	Suppress progress output during copy. Progress output is automatically suppressed if no terminal is attached

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
