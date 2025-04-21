Simple action in tc(8)							     Linux							Simple action in tc(8)

NAME
       simple - basic example action

SYNOPSIS
       tc ... action simple [ sdata STRING ] [ index INDEX ] [ CONTROL ]

       CONTROL := { reclassify | pipe | drop | continue | ok }

DESCRIPTION
       This is a pedagogical example rather than an actually useful action. Upon every access, it prints the given STRING which may be of arbitrary length.

OPTIONS
       sdata STRING
	      The actual string to print.

       index INDEX
	      Optional action index value.

       CONTROL
	      Indicate how tc should proceed after executing the action. For a description of the possible CONTROL values, see tc-actions(8).

EXAMPLES
       The following example makes the kernel yell "Incoming ICMP!" every time it sees an incoming ICMP on eth0. Steps are:

       1)  Add an ingress qdisc point to eth0

       2)  Start a chain on ingress of eth0 that first matches ICMP then invokes the simple action to shout.

       3)  display stats and show that no packet has been seen by the action

       4)  Send one ping packet to google (expect to receive a response back)

       5)  grep the logs to see the logged message

       6)  display stats again and observe increment by 1

	     hadi@noma1:$ tc qdisc add dev eth0 ingress
	     hadi@noma1:$tc filter add dev eth0 parent ffff: protocol ip prio 5 \
		 u32 match ip protocol 1 0xff flowid 1:1 action simple sdata "Incoming ICMP"

	     hadi@noma1:$ sudo tc -s filter ls	dev eth0 parent ffff:
	      filter protocol ip pref 5 u32
	      filter protocol ip pref 5 u32 fh 800: ht divisor 1
	      filter protocol ip pref 5 u32 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1
		match 00010000/00ff0000 at 8
		action order 1: Simple <Incoming ICMP>
		 index 4 ref 1 bind 1 installed 29 sec used 29 sec
		 Action statistics:
		     Sent 0 bytes 0 pkt (dropped 0, overlimits 0 requeues 0)
		     backlog 0b 0p requeues 0

	     hadi@noma1$ ping -c 1 www.google.ca
	     PING www.google.ca (74.125.225.120) 56(84) bytes of data.
	     64 bytes from ord08s08-in-f24.1e100.net (74.125.225.120): icmp_req=1 ttl=53 time=31.3 ms

	     --- www.google.ca ping statistics ---
	     1 packets transmitted, 1 received, 0% packet loss, time 0ms
	     rtt min/avg/max/mdev = 31.316/31.316/31.316/0.000 ms

	     hadi@noma1$ dmesg | grep simple
	     [135354.473951] simple: Incoming ICMP_1

	     hadi@noma1$ sudo tc/tc -s filter ls  dev eth0 parent ffff:
	     filter protocol ip pref 5 u32
	     filter protocol ip pref 5 u32 fh 800: ht divisor 1
	     filter protocol ip pref 5 u32 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1
	       match 00010000/00ff0000 at 8
		action order 1: Simple <Incoming ICMP>
		 index 4 ref 1 bind 1 installed 206 sec used 67 sec
		Action statistics:
		Sent 84 bytes 1 pkt (dropped 0, overlimits 0 requeues 0)
		backlog 0b 0p requeues 0

SEE ALSO
       tc(8) tc-actions(8)

iproute2								  12 Jan 2015							Simple action in tc(8)
