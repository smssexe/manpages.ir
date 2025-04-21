DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-images - List images

SYNOPSIS
       docker images [OPTIONS] [REPOSITORY[:TAG]]

DESCRIPTION
       Alias for docker image ls.

OPTIONS
       -a, --all[=false]      Show all images (default hides intermediate images)

       --digests[=false]      Show digests

       -f, --filter=	  Filter output based on conditions provided

       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for images

       --no-trunc[=false]      Don't truncate output

       -q, --quiet[=false]	Only show image IDs

       --tree[=false]	   List multi-platform images as a tree (EXPERIMENTAL)

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
