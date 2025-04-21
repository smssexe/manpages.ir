DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-context-update - Update a context

SYNOPSIS
       docker context update [OPTIONS] CONTEXT

DESCRIPTION
       Update a context

       Docker endpoint config:

       NAME		    DESCRIPTION from		    Copy named context's Docker endpoint configuration host		   Docker endpoint on which to
       connect ca		   Trust certs signed only by this CA cert		  Path to TLS certificate file key		    Path  to  TLS  key
       file skip-tls-verify	Skip TLS certificate validation

       Example:

       $ docker context update my-context --description "some description" --docker "host=tcp://myserver:2376,ca=~/ca-file,cert=~/cert-file,key=~/key-file"

OPTIONS
       --description=""	     Description of the context

       --docker=[]	set the docker endpoint

       -h, --help[=false]      help for update

SEE ALSO
       docker-context(1)

Docker Community							   Mar 2025								     DOCKER(1)
