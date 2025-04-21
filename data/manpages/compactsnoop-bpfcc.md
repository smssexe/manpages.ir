compactsnoop(8)							    System Manager's Manual						       compactsnoop(8)

NAME
       compactsnoop - Trace compact zone events. Uses Linux eBPF/bcc.

SYNOPSIS
       compactsnoop [-h] [-T] [-p PID] [-d DURATION] [-K] [-e]

DESCRIPTION
       compactsnoop traces the compact zone events, showing which processes are allocing pages with memory compaction. This can be useful for discovering when
       compact_stall (/proc/vmstat) continues to increase, whether it is caused by some critical processes or not.

       This works by tracing the compact zone events using raw_tracepoints and one kretprobe.

       For the Centos 7.6 (3.10.x kernel), see the version under tools/old, which uses an older memory compaction mechanism.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include a timestamp column.

       -p PID Trace this process ID only (filtered in-kernel).

       -d DURATION
	      Total duration of trace in seconds.

       -K     Output kernel stack trace

       -e     Show extended fields.

EXAMPLES
       Trace all compact zone events:
	      # compactsnoop

       Trace all compact zone events, for 10 seconds only:
	      # compactsnoop -d 10

FIELDS
       TIME(s)
	      Time of the call, in seconds.

       COMM   Process name

       PID    Process ID

       NODE   Memory node

       ZONE   Zone of the node (such as DMA, DMA32, NORMAL eg)

       ORDER  Shows which order alloc cause memory compaction, -1 means all orders (eg: write to /proc/sys/vm/compact_memory)

       MODE   SYNC OR ASYNC

       FRAGIDX (extra column)
	      The FRAGIDX is short for fragmentation index, which only makes sense if an allocation of a requested size would fail. If that is true, the frag‐
	      mentation index indicates whether external fragmentation or a lack of memory was the problem. The value can be used to determine if page reclaim
	      or compaction should be used.

	       Index is between 0 and 1 so return within 3 decimal places

	       0 => allocation would fail due to lack of memory

	       1 => allocation would fail due to fragmentation

       MIN (extra column)
	      The min watermark of the zone

       LOW (extra column)
	      The low watermark of the zone

       HIGH (extra column)
	      The high watermark of the zone

       FREE (extra column)
	      The nr_free_pages of the zone

       LAT(ms)
	      compact zone's latency

       STATUS The compaction's result.

	       For (CentOS 7.6's kernel), the status include:

	       "skipped" (COMPACT_SKIPPED): compaction didn't start as it was not possible or direct reclaim was more suitable

	       "continue" (COMPACT_CONTINUE): compaction should continue to another pageblock

	       "partial" (COMPACT_PARTIAL): direct compaction partially compacted a zone and there are suitable pages

	       "complete" (COMPACT_COMPLETE): The full zone was compacted

	       For (kernel 4.7 and above):

	       "not_suitable_zone" (COMPACT_NOT_SUITABLE_ZONE): For more detailed tracepoint output - internal to compaction

	       "skipped" (COMPACT_SKIPPED): compaction didn't start as it was not possible or direct reclaim was more suitable

	       "deferred" (COMPACT_DEFERRED): compaction didn't start as it was deferred due to past failures

	       "no_suitable_page" (COMPACT_NOT_SUITABLE_PAGE): For more detailed tracepoint output - internal to compaction

	       "continue" (COMPACT_CONTINUE): compaction should continue to another pageblock

	       "complete" (COMPACT_COMPLETE): The full zone was compacted scanned but wasn't successful to compact suitable pages.

	       "partial_skipped" (COMPACT_PARTIAL_SKIPPED): direct compaction has scanned part of the zone but wasn't successful to compact suitable pages.

	       "contended" (COMPACT_CONTENDED): compaction terminated prematurely due to lock contentions

	       "success" (COMPACT_SUCCESS): direct compaction terminated after concluding that the allocation should now succeed

OVERHEAD
       This  traces the kernel compact zone kprobe/kretprobe or raw_tracepoints and prints output for each event. As the rate of this is generally expected to
       be low (< 1000/s), the overhead is also expected to be negligible.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Wenbo Zhang

USER COMMANDS								   2019-11-1							       compactsnoop(8)
