DOCKER(1)							      Docker User Manuals							     DOCKER(1)

NAME
       docker-swarm-join - Join a swarm as a node and/or manager

SYNOPSIS
       docker swarm join [OPTIONS] HOST:PORT

DESCRIPTION
       Join a swarm as a node and/or manager

OPTIONS
       --advertise-addr=""	Advertised address (format: "[:port]")

       --availability="active"	    Availability of the node ("active", "pause", "drain")

       --data-path-addr=""	Address or interface to use for data path traffic (format: "")

       -h, --help[=false]      help for join

       --listen-addr=0.0.0.0:2377      Listen address (format: "[:port]")

       --token=""      Token for entry into the swarm

SEE ALSO
       docker-swarm(1)

Docker Community							   Mar 2025								     DOCKER(1)
