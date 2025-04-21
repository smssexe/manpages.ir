biolatency(8)							    System Manager's Manual							 biolatency(8)

NAME
       biolatency - Summarize block device I/O latency as a histogram.

SYNOPSIS
       biolatency [-h] [-F] [-T] [-Q] [-m] [-D] [-F] [-e] [-j] [-d DISK] [interval [count]]

DESCRIPTION
       biolatency  traces block device I/O (disk I/O), and records the distribution of I/O latency (time). This is printed as a histogram either on Ctrl-C, or
       after a given interval in seconds.

       The latency of disk I/O operations is measured from when requests are issued to the device up to completion. A -Q option can be used  to	 include  time
       queued in the kernel.

       This tool uses in-kernel eBPF maps for storing timestamps and the histogram, for efficiency.

       This works by tracing various kernel blk_*() functions using dynamic tracing, and will need updating to match any changes to these functions.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h Print usage message.

       -T     Include timestamps on output.

       -m     Output histogram in milliseconds.

       -D     Print a histogram per disk device.

       -F     Print a histogram per set of I/O flags.

       -j     Print a histogram dictionary

       -e     Show extension summary(total, average)

       -d DISK
	      Trace this disk only

       interval
	      Output interval, in seconds.

       count  Number of outputs.

EXAMPLES
       Summarize block device I/O latency as a histogram:
	      # biolatency

       Print 1 second summaries, 10 times:
	      # biolatency 1 10

       Print 1 second summaries, using milliseconds as units for the histogram, and
	      include timestamps on output: # biolatency -mT 1

       Include OS queued time in I/O time:
	      # biolatency -Q

       Show a latency histogram for each disk device separately:
	      # biolatency -D

       Show a latency histogram in a dictionary format:
	      # biolatency -j

       Also show extension summary(total, average):
	      # biolatency -e

FIELDS
       usecs  Microsecond range

       msecs  Millisecond range

       count  How many I/O fell into this range

       distribution
	      An ASCII bar chart to visualize the distribution (count column)

OVERHEAD
       This traces kernel functions and maintains in-kernel timestamps and a histogram, which are asynchronously copied to user-space. This method is very ef‐
       ficient,	 and the overhead for most storage I/O rates (< 10k IOPS) should be negligible.	 If you have a higher IOPS storage environment, test and quan‐
       tify the overhead before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg, Rocky Xing

SEE ALSO
       biosnoop(8)

USER COMMANDS								  2020-12-30								 biolatency(8)
