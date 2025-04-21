iptables action in tc(8)						     Linux						      iptables action in tc(8)

NAME
       xt - tc iptables action

SYNOPSIS
       tc ... action xt -j TARGET [ TARGET_OPTS ]

DESCRIPTION
       The xt action allows one to call arbitrary iptables targets for packets matching the filter this action is attached to.

OPTIONS
       -j TARGET [ TARGET_OPTS ]
	      Perform a jump to the given iptables target, optionally passing any target specific options in TARGET_OPTS.

EXAMPLES
       The following will attach a u32 filter to the ingress qdisc matching ICMP replies and using the xt action to make the kernel yell 'PONG' each time:

	      tc qdisc add dev eth0 ingress
	      tc filter add dev eth0 parent ffff: proto ip u32 \
		   match ip protocol 1 0xff \
		   match ip icmp_type 0 0xff \
		   action xt -j LOG --log-prefix PONG

SEE ALSO
       tc(8), tc-u32(8), iptables-extensions(8)

iproute2								  3 Mar 2016						      iptables action in tc(8)
