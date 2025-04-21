biopattern(8)							    System Manager's Manual							 biopattern(8)

NAME
       biopattern - Identify random/sequential disk access patterns.

SYNOPSIS
       biopattern [-h] [-d DISK] [interval] [count]

DESCRIPTION
       This  traces  block  device  I/O (disk I/O), and prints ratio of random/sequential I/O for each disk or the specified disk either on Ctrl-C, or after a
       given interval in seconds.

       This works by tracing kernel tracepoint block:block_rq_complete.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Show help message and exit.

       -d     Trace this disk only.

       interval
	      Print output every interval seconds, if any.

       count  Number of interval summaries.

EXAMPLES
       Trace access patterns of all disks, and print a summary on Ctrl-C:
	      # biopattern

       Trace disk sdb only:
	      # biopattern -d sdb

       Print 1 second summaries, 10 times:
	      # biopattern 1 10

FIELDS
       TIME   Time of the output, in HH:MM:SS format.

       DISK   Disk device name.

       %RND   Ratio of random I/O.

       %SEQ   Ratio of sequential I/O.

       COUNT  Number of I/O during the interval.

       KBYTES Total Kbytes for these I/O, during the interval.

OVERHEAD
       Since block device I/O usually has a relatively low frequency (< 10,000/s), the overhead for this tool is expected to be low or	negligible.  For  high
       IOPS storage systems, test and quantify before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Rocky Xing

SEE ALSO
       biosnoop(8), biolatency(8), iostat(1)

USER COMMANDS								  2022-02-21								 biopattern(8)
