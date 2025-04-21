ppchcalls(8)							    System Manager's Manual							  ppchcalls(8)

NAME
       ppchcalls - Summarize ppc hcall counts and latencies.

SYNOPSIS
       ppchcalls [-h] [-p PID] [-t TID] [-i INTERVAL] [-d DURATION] [-T TOP] [-x] [-e ERRNO] [-L] [-m] [-P] [-l] [--hcall HCALL]

DESCRIPTION
       This  tool traces hcall entry and exit raw tracepoints and summarizes either the number of hcalls of each type, or the number of hcalls per process. It
       can also collect min, max and average latency for each hcall or each process.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc. Linux 4.17+ is required to attach a BPF program to the raw_hcalls:hcall_{enter,exit} tracepoints, used by this tool.

OPTIONS
       -h     Print usage message.

       -p PID Trace only this process.

       -t TID Trace only this thread.

       -i INTERVAL
	      Print the summary at the specified interval (in seconds).

       -d DURATION
	      Total duration of trace (in seconds).

       -T TOP Print only this many entries. Default: 10.

       -x     Trace only failed hcalls (i.e., the return value from the hcall was < 0).

       -e ERRNO
	      Trace only hcalls that failed with that error (e.g. -e EPERM or -e 1).

       -m     Display times in milliseconds. Default: microseconds.

       -P     Summarize by process and not by hcall.

       -l     List the hcalls recognized by the tool (hard-coded list). Hcalls beyond this list will still be displayed, as "[unknown: nnn]" where nnn is  the
	      hcall number.

       --hcall HCALL
	      Trace this hcall only (use option -l to get all recognized hcalls).

EXAMPLES
       Summarize all hcalls by hcall:
	      # ppchcalls

       Summarize all hcalls by process:
	      # ppchcalls -P

       Summarize only failed hcalls:
	      # ppchcalls -x

       Summarize only hcalls that failed with EPERM:
	      # ppchcalls -e EPERM

       Trace PID 181 only:
	      # ppchcalls -p 181

       Summarize hcalls counts and latencies:
	      # ppchcalls -L

FIELDS
       PID    Process ID

       COMM   Process name

       HCALL  Hcall name, or "[unknown: nnn]" for hcalls that aren't recognized

       COUNT  The number of events

       MIN    The minimum elapsed time (in us or ms)

       MAX    The maximum elapsed time (in us or ms)

       AVG    The average elapsed time (in us or ms)

OVERHEAD
       For  most  applications, the overhead should be manageable if they perform 1000's or even 10,000's of hcalls per second. For higher rates, the overhead
       may become considerable.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Harsh Prateek Bora

SEE ALSO
       syscount(8)

USER COMMANDS								  2022-10-19								  ppchcalls(8)
