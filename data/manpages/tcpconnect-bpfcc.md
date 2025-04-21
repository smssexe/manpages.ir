tcpconnect(8)							    System Manager's Manual							 tcpconnect(8)

NAME
       tcpconnect - Trace TCP active connections (connect()). Uses Linux eBPF/bcc.

SYNOPSIS
       tcpconnect [-h] [-c] [-t] [-p PID] [-P PORT] [-4 | -6] [-L] [-u UID] [-U] [--cgroupmap MAPPATH] [--mntnsmap MAPPATH] [-d]

DESCRIPTION
       This tool traces active TCP connections (eg, via a connect() syscall; accept() are passive connections). This can be useful for general troubleshooting
       to see what connections are initiated by the local server.

       All connection attempts are traced, even if they ultimately fail.

       This  works by tracing the kernel tcp_v4_connect() and tcp_v6_connect() functions using dynamic tracing, and will need updating to match any changes to
       these functions.

       When provided with the -d or --dns option, this tool will also correlate connect calls with the most recent DNS query that matches  the	IP  connected.
       This feature works by tracing the kernel udp_recvmsg() function to collect DNS responses.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

       If  using  the  -d  or  --dns option, you must have the dnslib and cachetools python packages installed.	 You can install them with pip3 or with apt on
       Ubuntu 18.04+ using the python3-dnslib and python3-cachetools packages.

OPTIONS
       -h     Print usage message.

       -t     Include a timestamp column.

       -c     Count connects per src ip and dest ip/port.

       -p PID Trace this process ID only (filtered in-kernel).

       -P PORT
	      Comma-separated list of destination ports to trace (filtered in-kernel).

       -4     Trace IPv4 family only.

       -6     Trace IPv6 family only.

       -L     Include a LPORT column.

       -U     Include a UID column.

       -u UID Trace this UID only (filtered in-kernel).

       --cgroupmap MAPPATH
	      Trace cgroups in this BPF map only (filtered in-kernel).

       --mntnsmap  MAPPATH
	      Trace mount namespaces in this BPF map only (filtered in-kernel).

       -d     Shows the most recent DNS query for the IP address in the connect call.  This is likely related to the  TCP  connection  details	in  the	 other
	      columns,	but  is	 not  guaranteed.   This  feature  works by tracing the udp_recvmsg kernel function and tracking DNS responses received by the
	      server.  It only supports UDP DNS packets up to 512 bytes in length.  The python code keeps a cache of 10k DNS responses in  memory  for	up  24
	      hours.

	      If the time difference in milliseconds between when the system received a DNS response and when a connect syscall was traced using an IP in that
	      DNS response is greater than 100ms, this tool will report this delta after the query.  These deltas should be relatively short for most applica‐
	      tions.   A  long delay between the response and connect could be either anomalous activity or indicate a misattribution between the DNS name re‐
	      quested and the IP that the connect syscall is using.

	      The -d option may not be used with the count feature (option -c)

EXAMPLES
       Trace all active TCP connections:
	      # tcpconnect

       Trace all TCP connects, and include timestamps:
	      # tcpconnect -t

       Trace all TCP connects, and include most recent matching DNS query for each connected IP
	      # tcpconnect -d

       Trace PID 181 only:
	      # tcpconnect -p 181

       Trace ports 80 and 81 only:
	      # tcpconnect -P 80,81

       Trace IPv4 family only:
	      # tcpconnect -4

       Trace IPv6 family only:
	      # tcpconnect -6

       Trace all TCP connects, and include LPORT:
	      # tcpconnect -L

       Trace all TCP connects, and include UID:
	      # tcpconnect -U

       Trace UID 1000 only:
	      # tcpconnect -u 1000

       Count connects per src ip and dest ip/port:
	      # tcpconnect -c

       Trace a set of cgroups only (see special_filtering.md from bcc sources for more details):
	      # tcpconnect --cgroupmap /sys/fs/bpf/test01

       Trace a set of mount namespaces only (see special_filtering.md from bcc sources for more details):
	      # tcpconnect --mntnsmap /sys/fs/bpf/mnt_ns_set

FIELDS
       TIME(s)
	      Time of the call, in seconds.

       UID    User ID

       PID    Process ID

       COMM   Process name

       IP     IP address family (4 or 6)

       SADDR  Source IP address.

       LPORT  Source port

       DADDR  Destination IP address.

       DPORT  Destination port

       CONNECTS
	      Accumulated active connections since start.

       QUERY  Shows the most recent DNS query for the IP address in the connect call.  This is likely related to the  TCP  connection  details	in  the	 other
	      columns, but is not guaranteed.

OVERHEAD
       This  traces  the  kernel tcp_v[46]_connect functions and prints output for each event. As the rate of this is generally expected to be low (< 1000/s),
       the overhead is also expected to be negligible. If you have an application that is calling a high rate of connect()s, such as a proxy server, then test
       and understand this overhead before use.

       If you are using the -d option to track DNS requests, this tool will trace the udp_recvmsg function and generate an event for any packets from UDP port
       53.  This event contains up to 512 bytes of the UDP packet payload.  Typical applications do not extensively use UDP, so the  performance  overhead  of
       tracing udp_recvmsg is expected to be negligible,   However, if you have an application that receives many UDP packets, then you should test and under‐
       stand  the  overhead  of	 tracing every received UDP message.  Furthermore, performance overhead of running this tool on a DNS server is expected to be
       higher than average because all DNS response packets will be copied to userspace.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg

SEE ALSO
       tcptracer(8), tcpaccept(8), funccount(8), tcpdump(8)

USER COMMANDS								  2020-02-20								 tcpconnect(8)
