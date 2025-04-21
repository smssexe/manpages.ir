IP-NEXTHOP(8)								     Linux								 IP-NEXTHOP(8)

NAME
       ip-nexthop - nexthop object management

SYNOPSIS
       ip [ ip-OPTIONS ] nexthop  { COMMAND | help }

       ip nexthop { show | flush } SELECTOR

       ip nexthop { add | replace } id ID NH

       ip nexthop { get | del } id ID

       ip nexthop bucket list BUCKET_SELECTOR

       ip nexthop bucket get id ID index INDEX

       SELECTOR := [ id ID ] [ dev DEV ] [ vrf NAME ] [ master DEV ] [ groups ] [ fdb ]

       BUCKET_SELECTOR := SELECTOR  | [ nhid ID ]

       NH := { blackhole | [ via ADDRESS ] [ dev DEV ] [ onlink ] [ encap ENCAP ] [ fdb ] | group GROUP [ fdb ] [ type TYPE [ TYPE_ARGS ] ] }

       ENCAP := [ ENCAP_MPLS ]

       ENCAP_MPLS := mpls [ LABEL ] [ ttl TTL ]

       GROUP := id[,weight[/...]

       TYPE := { mpath | resilient }

       TYPE_ARGS := [ RESILIENT_ARGS ]

       RESILIENT_ARGS := [ buckets BUCKETS ] [ idle_timer IDLE ] [ unbalanced_timer UNBALANCED ]

DESCRIPTION
       ip nexthop is used to manipulate entries in the kernel's nexthop tables.

       ip nexthop add id ID
	      add new nexthop entry

       ip nexthop replace id ID
	      change the configuration of a nexthop or add new one

	      via [ FAMILY ] ADDRESS
		     the address of the nexthop router, in the address family FAMILY.  Address family must match address family of nexthop instance.

	      dev NAME
		     is the output device.

	      onlink pretend that the nexthop is directly attached to this link, even if it does not match any interface prefix.

	      encap ENCAPTYPE ENCAPHDR
		     attach tunnel encapsulation attributes to this route.

		     ENCAPTYPE is a string specifying the supported encapsulation type. Namely:

			     mpls - encapsulation type MPLS

		     ENCAPHDR is a set of encapsulation attributes specific to the ENCAPTYPE.

			     mpls
			       MPLSLABEL - mpls label stack with labels separated by /

			       ttl TTL - TTL to use for MPLS header or 0 to inherit from IP header

	      group GROUP [ type TYPE [ TYPE_ARGS ] ]
		     create a nexthop group. Group specification is id with an optional weight (id,weight) and a '/' as a separator between entries.

		     TYPE is a string specifying the nexthop group type. Namely:

			     mpath - Multipath nexthop group backed by the hash-threshold algorithm. The default when the type is unspecified.

			     resilient - Resilient nexthop group. Group is resilient to addition and deletion of nexthops.

		     TYPE_ARGS is a set of attributes specific to the TYPE.

			     resilient
			       buckets BUCKETS - Number of nexthop buckets. Cannot be changed for an existing group

			       idle_timer  IDLE	 - Time in seconds in which a nexthop bucket does not see traffic and is therefore considered idle. Default is
			       120 seconds

			       unbalanced_timer UNBALANCED - Time in seconds in which a nexthop group is unbalanced and is  therefore  considered  unbalanced.
			       The  kernel  will  try to rebalance unbalanced groups, which might result in some flows being reset. A value of 0 means that no
			       rebalancing will take place. Default is 0 seconds

	      blackhole
		     create a blackhole nexthop

	      fdb    nexthop and nexthop groups for use with layer-2 fdb entries.  A fdb nexthop group can only have fdb nexthops.  Example: Used to represent
		     a vxlan remote vtep ip. layer-2 vxlan fdb entry pointing to an ecmp nexthop group containing multiple remote vtep ips.

       ip nexthop delete id ID
	      delete nexthop with given id.

       ip nexthop show
	      show the contents of the nexthop table or the nexthops selected by some criteria.

	      dev DEV
		     show the nexthops using the given device.

	      vrf NAME
		     show the nexthops using devices associated with the vrf name

	      master DEV
		     show the nexthops using devices enslaved to given master device

	      groups show only nexthop groups

	      fdb    show only fdb nexthops and nexthop groups

       ip nexthop flush
	      flushes nexthops selected by some criteria. Criteria options are the same as show.

       ip nexthop get id ID
	      get a single nexthop by id

       ip nexthop bucket show
	      show the contents of the nexthop bucket table or the nexthop buckets selected by some criteria.

	      id ID
		     show the nexthop buckets that belong to a nexthop group with a given id

	      nhid ID
		     show the nexthop buckets that hold a nexthop with a given id

	      dev DEV
		     show the nexthop buckets using the given device

	      vrf NAME
		     show the nexthop buckets using devices associated with the vrf name

	      master DEV
		     show the nexthop buckets using devices enslaved to given master device

       ip nexthop bucket get id ID index INDEX
	      get a single nexthop bucket by nexthop group id and bucket index

EXAMPLES
       ip nexthop ls
	   Show all nexthop entries in the kernel.

       ip nexthop add id 1 via 192.168.1.1 dev eth0
	   Adds an IPv4 nexthop with id 1 using the gateway 192.168.1.1 out device eth0.

       ip nexthop add id 2 encap mpls 200/300 via 10.1.1.1 dev eth0
	   Adds an IPv4 nexthop with mpls encapsulation attributes attached to it.

       ip nexthop add id 3 group 1/2
	   Adds a nexthop with id 3. The nexthop is a group using nexthops with ids 1 and 2 at equal weight.

       ip nexthop add id 4 group 1,5/2,11
	   Adds a nexthop with id 4. The nexthop is a group using nexthops with ids 1 and 2 with nexthop 1 at weight 5 and nexthop 2 at weight 11.

       ip nexthop add id 5 via 192.168.1.2 fdb
	   Adds a fdb nexthop with id 5.

       ip nexthop add id 7 group 5/6 fdb
	   Adds a fdb nexthop group with id 7. A fdb nexthop group can only have fdb nexthops.

       ip nexthop add id 10 group 1/2 type resilient buckets 32
	   Add a resilient nexthop group with id 10 and 32 nexthop buckets.

SEE ALSO
       ip(8)

AUTHOR
       Original Manpage by David Ahern <dsahern@kernel.org>

iproute2								  30 May 2019								 IP-NEXTHOP(8)
