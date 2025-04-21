dirtop(8)							    System Manager's Manual							     dirtop(8)

NAME
       dirtop - File reads and writes by directory. Top for directories.

SYNOPSIS
       dirtop -d directory1,directory2,... [-h] [-C] [-r MAXROWS] [-s {reads,writes,rbytes,wbytes}] [-p PID] [interval] [count]

DESCRIPTION
       This is top for directories.

       This  traces  file  reads and writes, and prints a per-directory summary every interval (by default, 1 second). By default the summary is sorted on the
       highest read throughput (Kbytes). Sorting order can be changed via -s option.

       This uses in-kernel eBPF maps to store per process summaries for efficiency.

       This script works by tracing the __vfs_read() and __vfs_write() functions using kernel dynamic tracing,	which  instruments  explicit  read  and	 write
       calls.  If files are read or written using another means (eg, via mmap()), then they will not be visible using this tool. Also, this tool will need up‐
       dating to match any code changes to those vfs functions.

       This should be useful for file system workload characterization when analyzing the performance of applications.

       Note that tracing VFS level reads and writes can be a frequent activity, and this tool can begin to cost measurable overhead at high I/O rates.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -d     Defines a list of directories, comma separated, to observe.  Wildcards are allowed if between single bracket.

       -C     Don't clear the screen.

       -r MAXROWS
	      Maximum number of rows to print. Default is 20.

       -s {reads,writes,rbytes,wbytes}
	      Sort column. Default is rbytes (read throughput).

       -p PID Trace this PID only.

       interval
	      Interval between updates, seconds.

       count  Number of interval summaries.

EXAMPLES
       Summarize block device I/O by directory, 1 second screen refresh:
	      # dirtop -d '/hdfs/uuid/*/yarn'

       Don't clear the screen, and top 8 rows only:
	      # dirtop -d '/hdfs/uuid/*/yarn' -Cr 8

       5 second summaries, 10 times only:
	      # dirtop -d '/hdfs/uuid/*/yarn' 5 10

       Report read & write IOs generated in mutliple yarn and data directories:
	      # dirtop -d '/hdfs/uuid/*/yarn,/hdfs/uuid/*/data'

FIELDS
       loadavg:
	      The contents of /proc/loadavg

       READS  Count of reads during interval.

       WRITES Count of writes during interval.

       R_Kb   Total read Kbytes during interval.

       W_Kb   Total write Kbytes during interval.

       PATH   The path were the IOs were accounted.

OVERHEAD
       Depending on the frequency of application reads and writes, overhead can become significant, in the worst case slowing applications by over 50%.	 Hope‐
       fully  for  real	 world	workloads the overhead is much less -- test before use. The reason for the high overhead is that VFS reads and writes can be a
       frequent event, and despite the eBPF overhead being very small per event, if you multiply this small overhead by a million events per  second,  it  be‐
       comes a million times worse. Literally. You can gauge the number of reads and writes using the vfsstat(8) tool, also from bcc.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Erwan Velu

INSPIRATION
       filetop(8) by Brendan Gregg

SEE ALSO
       vfsstat(8), vfscount(8), fileslower(8)

USER COMMANDS								  2020-03-16								     dirtop(8)
