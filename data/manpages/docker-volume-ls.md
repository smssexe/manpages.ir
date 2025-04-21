DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-volume-ls - List volumes

SYNOPSIS
       docker volume ls [OPTIONS]

DESCRIPTION
       Lists  all the volumes Docker manages. You can filter using the -f or --filter flag. The filtering format is a key=value pair. To specify more than one
       filter,	pass multiple flags (for example, --filter "foo=bar" --filter "bif=baz")

       The currently supported filters are:

       • dangling (boolean - true or false, 1 or 0)

       • driver (a volume driver's name)

       • label (label=<key> or label=<key>=<value>)

       • name (a volume's name)

OPTIONS
       --cluster[=false]      Display only cluster volumes, and use cluster volume list formatting

       -f, --filter=	  Provide filter values (e.g. "dangling=true")

       --format=""	Format output using a custom template: 'table':		   Print output in table format with  column  headers  (default)  'table  TEM‐
       PLATE':	  Print output in table format using the given Go template 'json':	       Print in JSON format 'TEMPLATE':		Print output using the
       given Go template.  Refer to https://docs.docker.com/go/formatting/ for more information about formatting output with templates

       -h, --help[=false]      help for ls

       -q, --quiet[=false]	Only display volume names

SEE ALSO
       docker-volume(1)

Docker Community							   Mar 2025								     DOCKER(1)
