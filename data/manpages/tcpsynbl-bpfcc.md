tcpsynbl(8)							    System Manager's Manual							   tcpsynbl(8)

NAME
       tcpsynbl - Show the TCP SYN backlog as a histogram. Uses BCC/eBPF.

SYNOPSIS
       tcpsynbl [-4 | -6]

DESCRIPTION
       This  tool  shows the TCP SYN backlog size during SYN arrival as a histogram.  This lets you see how close your applications are to hitting the backlog
       limit and dropping SYNs (causing performance issues with SYN retransmits), and is a measure of workload saturation. The histogram shown is measured  at
       the time of SYN received, and a separate histogram is shown for each backlog limit.

       This  works  by tracing the tcp_v4_syn_recv_sock() and tcp_v6_syn_recv_sock() kernel functions using dynamic instrumentation. Since these functions may
       change in future kernels, this tool may need maintenance to keep working.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and BCC.

OPTIONS
       -h     Print usage message.

       -4     Trace IPv4 family only.

       -6     Trace IPv6 family only.

EXAMPLES
       Show the TCP SYN backlog as a histogram.
	      # tcpsynbl

       Trace IPv4 family only:
	      # tcpsynbl -4

       Trace IPv6 family only:
	      # tcpsynbl -6

FIELDS
       backlog
	      The backlog size when a SYN was received.

       count  The number of times this backlog size was encountered.

       distribution
	      An ASCII visualization of the count column.

OVERHEAD
       Inbound SYNs should be relatively low compared to packets and other events, so the overhead of this tool is expected to be negligible.

SOURCE
       This originated as a bpftrace tool from the book "BPF Performance Tools", published by Addison Wesley (2019):

	      http://www.brendangregg.com/bpf-performance-tools-book.html

       See the book for more documentation on this tool.

       This version is in the BCC repository:

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg

SEE ALSO
       tcptop(8)

USER COMMANDS								  2019-07-03								   tcpsynbl(8)
