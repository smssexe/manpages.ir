funcinterval(8)							    System Manager's Manual						       funcinterval(8)

NAME
       funcinterval - Time interval between the same function, tracepoint as a histogram.

SYNOPSIS
       funcinterval [-h] [-p PID] [-i INTERVAL] [-d DURATION] [-T] [-u] [-m] [-v] pattern

DESCRIPTION
       This tool times interval between the same function as a histogram.

       eBPF/bcc	 is very suitable for platform performance tuning.  By funclatency, we can profile specific functions to know how latency this function costs.
       However, sometimes performance drop is not about the latency of function but the interval between function calls.  funcinterval is born for  this  pur‐
       pose.

       This tool uses in-kernel eBPF maps for storing timestamps and the histogram, for efficiency.

       WARNING:	 This  uses  dynamic  tracing  of  (what  can  be  many) functions, an activity that has had issues on some kernel versions (risk of panics or
       freezes). Test, and know what you are doing, before use.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       pattern Function name.  -h Print usage message.

       -p PID Trace this process ID only.

       -i INTERVAL
	      Print output every interval seconds.

       -d DURATION
	      Total duration of trace, in seconds.

       -T     Include timestamps on output.

       -u     Output histogram in microseconds.

       -m     Output histogram in milliseconds.

       -v     Print the BPF program (for debugging purposes).

EXAMPLES
       Time the interval of do_sys_open() kernel function as a histogram:
	      # funcinterval do_sys_open

       Time the interval of xhci_ring_ep_doorbell(), in microseconds:
	      # funcinterval -u xhci_ring_ep_doorbell

       Time the interval of do_nanosleep(), in milliseconds
	      # funcinterval -m do_nanosleep

       Output every 5 seconds, with timestamps:
	      # funcinterval -mTi 5 vfs_read

       Time process 181 only:
	      # funcinterval -p 181 vfs_read

       Time the interval of mm_vmscan_direct_reclaim_begin tracepoint:
	      # funcinterval t:vmscan:mm_vmscan_direct_reclaim_begin

       Time the interval of c:malloc used by top every 3 seconds:
	      # funcinterval -p `pidof -s top` -i 3 c:malloc

       Time /usr/local/bin/python main function:
	      # funcinterval /usr/local/bin/python:main

FIELDS
       necs   Nanosecond range

       usecs  Microsecond range

       msecs  Millisecond range

       count  How many calls fell into this range

       distribution
	      An ASCII bar chart to visualize the distribution (count column)

OVERHEAD
       This traces kernel functions and maintains in-kernel timestamps and a histogram, which are asynchronously copied to user-space. While  this  method  is
       very  efficient,	 the  rate of kernel functions can also be very high (>1M/sec), at which point the overhead is expected to be measurable. Measure in a
       test environment and understand overheads before use. You can also use funccount to measure the rate of kernel functions over a short duration, to  set
       some expectations before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Edward Wu

SEE ALSO
       funclatency(8) funccount(8)

USER COMMANDS								  2020-05-27							       funcinterval(8)
