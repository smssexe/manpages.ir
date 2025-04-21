Mirror/redirect action in tc(8)						     Linux					       Mirror/redirect action in tc(8)

NAME
       mirred - mirror/redirect action

SYNOPSIS
       tc ... action mirred DIRECTION ACTION [ index INDEX ] dev DEVICENAME

       DIRECTION := { ingress | egress }

       ACTION := { mirror | redirect }

DESCRIPTION
       The  mirred  action  allows  packet mirroring (copying) or redirecting (stealing) the packet it receives. Mirroring is what is sometimes referred to as
       Switch Port Analyzer (SPAN) and is commonly used to analyze and/or debug flows.

OPTIONS
       ingress
       egress Specify the direction in which the packet shall appear on the destination interface.

       mirror
       redirect
	      Define whether the packet should be copied (mirror) or moved (redirect) to the destination interface.

       index INDEX
	      Assign a unique ID to this action instead of letting the kernel choose one automatically.	 INDEX is a 32bit unsigned integer greater than zero.

       dev DEVICENAME
	      Specify the network interface to redirect or mirror to.

EXAMPLES
       Limit ingress bandwidth on eth0 to 1mbit/s, redirect exceeding traffic to lo for debugging purposes:

	      # tc qdisc add dev eth0 handle ffff: ingress
	      # tc filter add dev eth0 parent ffff: u32 \
		   match u32 0 0 \
		   action police rate 1mbit burst 100k conform-exceed pipe \
		   action mirred egress redirect dev lo

       Mirror all incoming ICMP packets on eth0 to a dummy interface for examination with e.g. tcpdump:

	      # ip link add dummy0 type dummy
	      # ip link set dummy0 up
	      # tc qdisc add dev eth0 handle ffff: ingress
	      # tc filter add dev eth0 parent ffff: protocol ip \
		   u32 match ip protocol 1 0xff \
		   action mirred egress mirror dev dummy0

       Using an ifb interface, it is possible to send ingress traffic through an instance of sfq:

	      # modprobe ifb
	      # ip link set ifb0 up
	      # tc qdisc add dev ifb0 root sfq
	      # tc qdisc add dev eth0 handle ffff: ingress
	      # tc filter add dev eth0 parent ffff: u32 \
		   match u32 0 0 \
		   action mirred egress redirect dev ifb0

SEE ALSO
       tc(8), tc-u32(8)

iproute2								  11 Jan 2015					       Mirror/redirect action in tc(8)
