undump.bt(8)							    System Manager's Manual							  undump.bt(8)

NAME
       undump.bt - Catch UNIX domain socket packages. Uses bpftrace/eBPF.

SYNOPSIS
       undump.bt

DESCRIPTION
       undump.bt tracked reception of UNIX domain sockets.

       This program is also a basic example of bpftrace and kprobes.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bpftrace.

EXAMPLES
       Trace reception of UNIX domain sockets:
	      # undump.bt

FIELDS
       TIME   A timestamp on the output, in "HH:MM:SS" format.

       COMM   The process COMM.

       PID    The process ID.

       SIZE   The size of the received packet, in bytes.

       DATA   Display received packets in hex or string.

OVERHEAD
       The overhead of this program mainly comes from the data packets received by the terminal output.

SOURCE
       This is from bpftrace.

	      https://github.com/iovisor/bpftrace

       Also look in the bpftrace distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

       This is a bpftrace version of the bcc examples/tracing of the same name.	 The bcc tool may provide more options and customizations.

	      https://github.com/iovisor/bcc

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Rong Tao

SEE ALSO
       opensnoop.bt(8)

USER COMMANDS								  2022-06-03								  undump.bt(8)
