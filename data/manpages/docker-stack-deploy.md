DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-stack-deploy - Deploy a new stack or update an existing stack

SYNOPSIS
       docker stack deploy [OPTIONS] STACK

DESCRIPTION
       Deploy a new stack or update an existing stack

OPTIONS
       -c, --compose-file=[]	  Path to a Compose file, or "-" to read from stdin

       -d, --detach[=true]	Exit immediately instead of waiting for the stack services to converge

       -h, --help[=false]      help for deploy

       --prune[=false]	    Prune services that are no longer referenced

       -q, --quiet[=false]	Suppress progress output

       --resolve-image="always"	     Query the registry to resolve image digest and supported platforms ("always", "changed", "never")

       --with-registry-auth[=false]	 Send registry authentication details to Swarm agents

SEE ALSO
       docker-stack(1)

Docker Community							   Mar 2025								     DOCKER(1)
