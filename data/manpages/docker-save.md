DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-save - Save one or more images to a tar archive (streamed to STDOUT by default)

SYNOPSIS
       docker save [OPTIONS] IMAGE [IMAGE...]

DESCRIPTION
       Alias for docker image save.

OPTIONS
       -h, --help[=false]      help for save

       -o, --output=""	    Write to a file, instead of STDOUT

       --platform=""	  Save only the given platform variant. Formatted as "os[/arch[/variant]]" (e.g., "linux/amd64")

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
