DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-volume-inspect - Display detailed information on one or more volumes

SYNOPSIS
       docker volume inspect [OPTIONS] VOLUME [VOLUME...]

DESCRIPTION
       Returns information about one or more volumes. By default, this command renders all results in a JSON array. You can specify an alternate format to ex‐
       ecute a given template is executed for each result. Go's https://pkg.go.dev/text/template package describes all the details of the format.

OPTIONS
       -f,  --format=""	      Format output using a custom template: 'json':		 Print in JSON format 'TEMPLATE':	  Print output using the given
       Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for inspect

SEE ALSO
       docker-volume(1)

Docker Community							   Mar 2025								     DOCKER(1)
