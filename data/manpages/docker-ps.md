DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-ps - List containers

SYNOPSIS
       docker ps [OPTIONS]

DESCRIPTION
       Alias for docker container ls.

OPTIONS
       -a, --all[=false]      Show all containers (default shows just running)

       -f, --filter=	  Filter output based on conditions provided

       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for ps

       -n, --last=-1	  Show n last created containers (includes all states)

       -l, --latest[=false]	 Show the latest created container (includes all states)

       --no-trunc[=false]      Don't truncate output

       -q, --quiet[=false]	Only display container IDs

       -s, --size[=false]      Display total file sizes

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
