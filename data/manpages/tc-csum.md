Checksum action in tc(8)						     Linux						      Checksum action in tc(8)

NAME
       csum - checksum update action

SYNOPSIS
       tc ... action csum UPDATE

       UPDATE := TARGET [ UPDATE ]

       TARGET := { ip4h | icmp | igmp | tcp | udp | udplite | sctp | SWEETS }

       SWEETS := { and | or | + }

DESCRIPTION
       The  csum action triggers checksum recalculation of specified packet headers. It is commonly used to fix incorrect checksums after the pedit action has
       modified the packet content.

OPTIONS
       TARGET Specify which headers to update: IPv4 header (ip4h), ICMP header (icmp), IGMP header (igmp), TCP header (tcp), UDP header (udp), UDPLite	header
	      (udplite) or SCTP header (sctp).

       SWEETS These are merely syntactic sugar and ignored internally.

EXAMPLES
       The following performs stateless NAT for incoming packets from 192.0.2.100 to new destination 198.51.100.1. Assuming these are UDP packets, both IP and
       UDP checksums have to be recalculated:

	      # tc qdisc add dev eth0 ingress handle ffff:
	      # tc filter add dev eth0 prio 1 protocol ip parent ffff: \
		   u32 match ip src 192.0.2.100/32 flowid :1 \
		   action pedit munge ip dst set 198.51.100.1 pipe \
		   csum ip and udp

SEE ALSO
       tc(8), tc-pedit(8)

iproute2								  11 Jan 2015						      Checksum action in tc(8)
