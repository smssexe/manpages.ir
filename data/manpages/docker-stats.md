DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-stats - Display a live stream of container(s) resource usage statistics

SYNOPSIS
       docker stats [OPTIONS] [CONTAINER...]

DESCRIPTION
       Alias for docker container stats.

OPTIONS
       -a, --all[=false]      Show all containers (default shows just running)

       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for stats

       --no-stream[=false]	Disable streaming stats and only pull the first result

       --no-trunc[=false]      Do not truncate output

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
