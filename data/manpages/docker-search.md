DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-search - Search Docker Hub for images

SYNOPSIS
       docker search [OPTIONS] TERM

DESCRIPTION
       Search  Docker Hub for images that match the specified TERM. The table of images returned displays the name, description (truncated by default), number
       of stars awarded, whether the image is official, and whether it is automated.

Filter
       Filter output based on these conditions:
	  - stars=
	  - is-automated=(true|false) (deprecated)
	  - is-official=(true|false)

EXAMPLES
Search Docker Hub for ranked images
       Search a registry for the term 'fedora' and only display those images ranked 3 or higher:

       $ docker search --filter=stars=3 fedora
       NAME	 DESCRIPTION			    STARS     OFFICIAL
       fedora	 Official Docker builds of Fedora   1150      [OK]

OPTIONS
       -f, --filter=	  Filter output based on conditions provided

       --format=""	Pretty-print search using a Go template

       -h, --help[=false]      help for search

       --limit=0      Max number of search results

       --no-trunc[=false]      Don't truncate output

SEE ALSO
       docker(1)

Docker Community							   Mar 2025								     DOCKER(1)
