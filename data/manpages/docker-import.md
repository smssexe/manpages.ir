DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-import - Import the contents from a tarball to create a filesystem image

SYNOPSIS
       docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]

DESCRIPTION
       Alias for docker image import.

OPTIONS
       -c, --change=	  Apply Dockerfile instruction to the created image

       -h, --help[=false]      help for import

       -m, --message=""	     Set commit message for imported image

       --platform=""	  Set platform if server is multi-platform capable

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
