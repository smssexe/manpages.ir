tcpretrans.bt(8)						    System Manager's Manual						      tcpretrans.bt(8)

NAME
       tcpretrans.bt - Trace or count TCP retransmits. Uses Linux bpftrace/eBPF

SYNOPSIS
       tcpretrans.bt

DESCRIPTION
       This  traces TCP retransmits, showing address, port, and TCP state information, and sometimes the PID (although usually not, since retransmits are usu‐
       ally sent by the kernel on timeouts). To keep overhead very low, only the TCP retransmit functions are traced. This does not trace every	 packet	 (like
       tcpdump(8)  or  a  packet  sniffer). Optionally, it can count retransmits over a user signalled interval to spot potentially dropping network paths the
       flows are traversing.

       This uses dynamic tracing of the kernel tcp_retransmit_skb() and tcp_send_loss_probe() functions, and will need to be updated to match  kernel  changes
       to these functions.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.  CONFIG_BPF and bpftrace.

EXAMPLES
       Trace TCP retransmits:
	      # tcpretrans.bt

       FIELDS

       TIME   Time of the call, in HH:MM:SS format.

       PID    Process ID that was on-CPU. This is less useful than it might sound, as it may usually be 0, for the kernel, for timer-based retransmits.

       LADDR  Local IP address.

       LPORT  Local port.

       RADDR  Remote IP address.

       RPORT  Remote port.

       STATE  TCP session state.

OVERHEAD
       Should be negligible: TCP retransmit events should be low (<1000/s), and the low overhead this tool adds to each event should make the cost negligible.

SOURCE
       This is from bpftrace

	      https://github.com/iovisor/bpftrace

       Also look in the bpftrace distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

       This is a bpftrace version of the bcc tool of the same name. The bcc tool may provide more options and customizations.

	      https://github.com/iovisor/bcc

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg, adapted for bpftrace by Dale Hamel

SEE ALSO
       tcpconnect.bt(8), tcpaccept.bt(8)

USER COMMANDS								  2018-11-24							      tcpretrans.bt(8)
