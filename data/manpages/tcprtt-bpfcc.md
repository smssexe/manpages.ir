tcprtt(8)							    System Manager's Manual							     tcprtt(8)

NAME
       tcprtt - Trace TCP RTT of established connections. Uses Linux eBPF/bcc.

SYNOPSIS
       tcprtt [-h] [-T] [-D] [-m] [-p LPORT] [-P RPORT] [-a LADDR] [-A RADDR] [-i INTERVAL] [-d DURATION] [-b] [-B] [-e] [-4 | -6]

DESCRIPTION
       This tool traces established connections RTT(round-trip time) to analyze the quality of network. This can be useful for general troubleshooting to dis‐
       tinguish the network latency is from user process or physical network.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include a time column on output (HH:MM:SS).

       -D     Show debug infomation of bpf text.

       -m     Output histogram in milliseconds.

       -i INTERVAL
	      Print output every interval seconds.

       -d DURATION
	      Total duration of trace in seconds.

       -p LPORT
	      Filter for local port.

       -P RPORT
	      Filter for remote port.

       -a LADDR
	      Filter for local address.

       -A RADDR
	      Filter for remote address.

       -b     Show sockets histogram by local address.

       -B     Show sockets histogram by remote address.

       -e     Show extension summary(average).

       -4     Trace IPv4 family only.

       -6     Trace IPv6 family only.

EXAMPLES
       Trace TCP RTT and print 1 second summaries, 10 times:
	      # tcprtt -i 1 -d 10

       Summarize in millisecond, and timestamps:
	      # tcprtt -m -T

       Only trace TCP RTT for remote address 192.168.1.100 and remote port 80:
	      # tcprtt -i 1 -d 10 -A 192.168.1.100 -P 80

       Trace local port and show a breakdown of remote hosts RTT:
	      # tcprtt -i 3 --lport 80 --byraddr

       Trace IPv4 family only:
	      # tcprtt -4

       Trace IPv6 family only:
	      # tcprtt -6

OVERHEAD
       This  traces the kernel tcp_rcv_established function and collects TCP RTT. The rate of this depends on your server application. If it is a web or proxy
       server accepting many tens of thousands of connections per second.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       zhenwei pi

SEE ALSO
       tcptracer(8), tcpconnect(8), funccount(8), tcpdump(8)

USER COMMANDS								  2020-08-23								     tcprtt(8)
