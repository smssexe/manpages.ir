DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-service-ls - List services

SYNOPSIS
       docker service ls [OPTIONS]

DESCRIPTION
       List services

OPTIONS
       -f, --filter=	  Filter output based on conditions provided

       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for ls

       -q, --quiet[=false]	Only display IDs

SEE ALSO
       docker-service(1)

Docker Community							   Mar 2025								     DOCKER(1)
