hardirqs(8)							    System Manager's Manual							   hardirqs(8)

NAME
       hardirqs - Measure hard IRQ (hard interrupt) event time. Uses Linux eBPF/bcc.

SYNOPSIS
       hardirqs [-h] [-T] [-N] [-C] [-d] [interval] [outputs]

DESCRIPTION
       This summarizes the time spent servicing hard IRQs (hard interrupts), and can show this time as either totals or histogram distributions. A system-wide
       summary of this time is shown by the %irq column of mpstat(1), and event counts (but not times) are shown by /proc/interrupts.

       This  tool  uses the irq:irq_handler_entry and irq:irq_handler_exit kernel tracepoints, which is a stable tracing mechanism. BPF programs can attach to
       tracepoints from Linux 4.7 only. An older version of this tool is available in tools/old, and uses kprobes instead of tracepoints.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include timestamps on output.

       -N     Output in nanoseconds.

       -C     Count events only.

       -d     Show IRQ time distribution as histograms.

       -c CPU Trace on this CPU only.

EXAMPLES
       Sum hard IRQ event time until Ctrl-C:
	      # hardirqs

       Show hard IRQ event time as histograms:
	      # hardirqs -d

       Print 1 second summaries, 10 times:
	      # hardirqs 1 10

       1 second summaries, printed in nanoseconds, with timestamps:
	      # hardirqs -NT 1

       Sum hard IRQ event time on CPU 1 until Ctrl-C:
	      # hardirqs -c 1

FIELDS
       HARDIRQ
	      The irq action name for this hard IRQ.

       TOTAL_usecs
	      Total time spent in this hard IRQ in microseconds.

       TOTAL_nsecs
	      Total time spent in this hard IRQ in nanoseconds.

       usecs  Range of microseconds for this bucket.

       nsecs  Range of nanoseconds for this bucket.

       count  Number of hard IRQs in this time range.

       distribution
	      ASCII representation of the distribution (the count column).

OVERHEAD
       This traces kernel functions and maintains in-kernel counts, which are asynchronously copied to user-space. While the rate of interrupts be  very  high
       (>1M/sec), this is a relatively efficient way to trace these events, and so the overhead is expected to be small for normal workloads, but could become
       noticeable for heavy workloads. Measure in a test environment before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg, Hengqi Chen, Rocky Xing

SEE ALSO
       softirqs(8)

USER COMMANDS								  2015-10-20								   hardirqs(8)
