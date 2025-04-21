IP-NETCONF(8)								     Linux								 IP-NETCONF(8)

NAME
       ip-netconf - network configuration monitoring

SYNOPSIS
       ip  [ ip-OPTIONS ] netconf show [ dev NAME ]

DESCRIPTION
       The ip netconf utility can monitor IPv4 and IPv6 parameters (see /proc/sys/net/ipv[4|6]/conf/[all|DEV]/) like forwarding, rp_filter, proxy_neigh, ig‐
       nore_routes_with_linkdown or mc_forwarding status.

       If no interface is specified, the entry all is displayed.

   ip netconf show - display network parameters
       dev NAME
	      the name of the device to display network parameters for.

SEE ALSO
       ip(8)

AUTHOR
       Original Manpage by Nicolas Dichtel <nicolas.dichtel@6wind.com>

iproute2								  13 Dec 2012								 IP-NETCONF(8)
