DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-system-df - Show docker disk usage

SYNOPSIS
       docker system df [OPTIONS]

DESCRIPTION
       Show docker disk usage

OPTIONS
       --format=""	 Format	 output	 using	a  custom template: 'table':		Print output in table format with column headers (default) 'table TEM‐
       PLATE':	 Print output in table format using the given Go template 'json':	      Print in JSON format 'TEMPLATE':	       Print output using  the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for df

       -v, --verbose[=false]	  Show detailed information on space usage

SEE ALSO
       docker-system(1)

Docker Community							   Mar 2025								     DOCKER(1)
