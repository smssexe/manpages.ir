DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-history - Show the history of an image

SYNOPSIS
       docker history [OPTIONS] IMAGE

DESCRIPTION
       Alias for docker image history.

OPTIONS
       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for history

       -H, --human[=true]      Print sizes and dates in human readable format

       --no-trunc[=false]      Don't truncate output

       --platform=""	  Show history for the given platform. Formatted as "os[/arch[/variant]]" (e.g., "linux/amd64")

       -q, --quiet[=false]	Only show image IDs

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
