DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-stack-services - List the services in the stack

SYNOPSIS
       docker stack services [OPTIONS] STACK

DESCRIPTION
       List the services in the stack

OPTIONS
       -f, --filter=	  Filter output based on conditions provided

       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for services

       -q, --quiet[=false]	Only display IDs

SEE ALSO
       docker-stack(1)

Docker Community							   Mar 2025								     DOCKER(1)
