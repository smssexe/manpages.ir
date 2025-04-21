Route classifier in tc(8)						     Linux						     Route classifier in tc(8)

NAME
       route - route traffic control filter

SYNOPSIS
       tc filter ... route [ from REALM | fromif TAG ] [ to REALM ] [ classid CLASSID ] [ action ACTION_SPEC ]

DESCRIPTION
       Match  packets based on routing table entries. This filter centers around the possibility to assign a realm to routing table entries. For any packet to
       be classified by this filter, a routing table lookup is performed and the returned realm is used to decide on whether the packet is a match or not.

OPTIONS
       action ACTION_SPEC
	      Apply an action from the generic actions framework on matching packets.

       classid CLASSID
	      Push matching packets into the class identified by CLASSID.

       from REALM
       fromif TAG
	      Perform source route lookups.  TAG is the name of an interface which must be present on the system at the time of tc invocation.

       to REALM
	      Match if normal (i.e., destination) routing returns the given REALM.

EXAMPLES
       Consider the subnet 192.168.2.0/24 being attached to eth0:

	      ip route add 192.168.2.0/24 dev eth0 realm 2

       The following route filter will then match packets from that subnet:

	      tc filter add ... route from 2 classid 1:2

       and pass packets on to class 1:2.

NOTES
       Due  to	implementation	details,  realm	 values	 must  be  in  a  range	 from  0  to  255,  inclusive.	Alternatively,	a  verbose  name  defined   in
       /etc/iproute2/rt_realms may be given instead.

SEE ALSO
       tc(8), ip-route(8)

iproute2								  21 Oct 2015						     Route classifier in tc(8)
