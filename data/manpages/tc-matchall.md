Match-all classifier in tc(8)						     Linux						 Match-all classifier in tc(8)

NAME
       matchall - traffic control filter that matches every packet

SYNOPSIS
       tc filter ... matchall [ skip_sw | skip_hw  ] [ action ACTION_SPEC ] [ classid CLASSID ]

DESCRIPTION
       The matchall filter allows one to classify every packet that flows on the port and run a action on it.

OPTIONS
       action ACTION_SPEC
	      Apply an action from the generic actions framework on matching packets.

       classid CLASSID
	      Push matching packets into the class identified by CLASSID.

       skip_sw
	      Do not process filter by software. If hardware has no offload support for this filter, or TC offload is not enabled for the interface, operation
	      will fail.

       skip_hw
	      Do not process filter by hardware.

EXAMPLES
       To create ingress mirroring from port eth1 to port eth2:

	      tc qdisc	add dev eth1 handle ffff: ingress
	      tc filter add dev eth1 parent ffff:	    \
		      matchall skip_sw			    \
		      action mirred egress mirror	    \
		      dev eth2

       The first command creates an ingress qdisc with handle ffff: on device eth1 where the second command attaches a matchall filters on it that mirrors the
       packets to device eth2.

       To create egress mirroring from port eth1 to port eth2:

	      tc qdisc add dev eth1 handle 1: root prio
	      tc filter add dev eth1 parent 1:		     \
		      matchall skip_sw			     \
		      action mirred egress mirror	     \
		      dev eth2

       The  first command creates an egress qdisc with handle 1: that replaces the root qdisc on device eth1 where the second command attaches a matchall fil‐
       ters on it that mirrors the packets to device eth2.

       To sample one of every 100 packets flowing into interface eth0 to psample group 12:

	      tc qdisc add dev eth0 handle ffff: ingress
	      tc filter add dev eth0 parent ffff: matchall \
		   action sample rate 100 group 12

SEE ALSO
       tc(8),

iproute2								  21 Oct 2015						 Match-all classifier in tc(8)
