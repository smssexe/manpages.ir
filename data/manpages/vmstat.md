VMSTAT(8)							     System Administration							     VMSTAT(8)

NAME
       vmstat - Report virtual memory statistics

SYNOPSIS
       vmstat [options] [delay [count]]

DESCRIPTION
       vmstat reports information about processes, memory, paging, block IO, traps, disks and cpu activity.

       The first report produced gives averages since the last reboot.	Additional reports give information on a sampling period of length delay.  The process
       and memory reports are instantaneous in either case.

OPTIONS
       delay  The delay between updates in seconds.  If no delay is specified, only one report is printed with the average values since boot.

       count  Number of updates.  In absence of count, when delay is defined, default is infinite.

       -a, --active
	      Display active and  inactive memory, given a 2.5.41 kernel or better.

       -f, --forks
	      The  -f  switch  displays the number of forks since boot.	 This includes the fork, vfork, and clone system calls, and is equivalent to the total
	      number of tasks created.	Each process is represented by one or more tasks, depending on thread usage.  This display does not repeat.

       -m, --slabs
	      Displays slabinfo.

       -n, --one-header
	      Display the header only once rather than periodically.

       -s, --stats
	      Displays a table of various event counters and memory statistics.	 This display does not repeat.

       -d, --disk
	      Report disk statistics (2.5.70 or above required).

       -D, --disk-sum
	      Report some summary statistics about disk activity.

       -p, --partition device
	      Detailed statistics about partition (2.5.70 or above required).

       -S, --unit character
	      Switches outputs between 1000 (k), 1024 (K), 1000000 (m), or 1048576 (M) bytes.  Note this does not change the swap  (si/so)  or	block  (bi/bo)
	      fields.

       -t, --timestamp
	      Append timestamp to each line

       -w, --wide
	      Wide  output  mode  (useful for systems with higher amount of memory, where the default output mode suffers from unwanted column breakage).  The
	      output is wider than 80 characters per line.

       -y, --no-first
	      Omits first report with statistics since system boot.

       -V, --version
	      Display version information and exit.

       -h, --help
	      Display help and exit.

FIELD DESCRIPTION FOR VM MODE
   Procs
       r: The number of runnable processes (running or waiting for run time).
       b: The number of processes blocked waiting for I/O to complete.

   Memory
       These are affected by the --unit option.
       swpd: the amount of swap memory used.
       free: the amount of idle memory.
       buff: the amount of memory used as buffers.
       cache: the amount of memory used as cache.
       inact: the amount of inactive memory.  (-a option)
       active: the amount of active memory.  (-a option)

   Swap
       These are affected by the --unit option.
       si: Amount of memory swapped in from disk (/s).
       so: Amount of memory swapped to disk (/s).

   IO
       bi: Kibibyte received from a block device (KiB/s).
       bo: Kibibyte sent to a block device (KiB/s).

   System
       in: The number of interrupts per second, including the clock.
       cs: The number of context switches per second.

   CPU
       These are percentages of total CPU time.
       us: Time spent running non-kernel code.	(user time, including nice time)
       sy: Time spent running kernel code.  (system time)
       id: Time spent idle.  Prior to Linux 2.5.41, this includes IO-wait time.
       wa: Time spent waiting for IO.  Prior to Linux 2.5.41, included in idle.
       st: Time stolen from a virtual machine.	Prior to Linux 2.6.11, unknown.
       gu: Time spent running KVM guest code (guest time, including guest nice).

FIELD DESCRIPTION FOR DISK MODE
   Reads
       total: Total reads completed successfully
       merged: grouped reads (resulting in one I/O)
       sectors: Sectors read successfully
       ms: milliseconds spent reading

   Writes
       total: Total writes completed successfully
       merged: grouped writes (resulting in one I/O)
       sectors: Sectors written successfully
       ms: milliseconds spent writing

   IO
       cur: I/O in progress
       s: seconds spent for I/O

FIELD DESCRIPTION FOR DISK PARTITION MODE
       reads: Total number of reads issued to this partition
       read sectors: Total read sectors for partition
       writes : Total number of writes issued to this partition
       requested writes: Total number of write requests made for partition

FIELD DESCRIPTION FOR SLAB MODE
       Slab mode shows statistics per slab, for more information about this information see slabinfo(5)

       cache: Cache name
       num: Number of currently active objects
       total: Total number of available objects
       size: Size of each object
       pages: Number of pages with at least one active object

NOTES
       vmstat requires read access to files under /proc. The -m requires read access to /proc/slabinfo which may not be available to  standard	users.	 Mount
       options for /proc such as subset=pid may also impact what is visible.

SEE ALSO
       free(1), iostat(1), mpstat(1), ps(1), sar(1), top(1), slabinfo(5)

REPORTING BUGS
       Please send bug reports to procps@freelists.org

procps-ng								  2023-01-18								     VMSTAT(8)
