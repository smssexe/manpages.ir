killsnoop(8)							    System Manager's Manual							  killsnoop(8)

NAME
       killsnoop - Trace signals issued by the kill() syscall. Uses Linux eBPF/bcc.

SYNOPSIS
       killsnoop [-h] [-x] [-p PID] [-T PID] [-s SIGNAL]

DESCRIPTION
       killsnoop  traces  the  kill() syscall, to show signals sent via this method. This may be useful to troubleshoot failing applications, where an unknown
       mechanism is sending signals.

       This works by tracing the kernel sys_kill() function using dynamic tracing, and will need updating to match any changes to this function.

       This makes use of a Linux 4.4 feature (bpf_perf_event_output()); for kernels older than 4.4, see the version under tools/old, which uses an older mech‐
       anism.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -x     Only print failed kill() syscalls.

       -p PID Trace this process ID only which is the sender of signal (filtered in-kernel).

       -T PID Trace this target process ID only which is the receiver of signal (filtered in-kernel).

       -s SIGNAL
	      Trace this signal only (filtered in-kernel).

EXAMPLES
       Trace all kill() syscalls:
	      # killsnoop

       Trace only kill() syscalls that failed:
	      # killsnoop -x

       Trace PID 181 only:
	      # killsnoop -p 181

       Trace target PID 189 only:
	      # killsnoop -T 189

       Trace signal 9 only:
	      # killsnoop -s 9

FIELDS
       TIME   Time of the kill call.

       PID    Source process ID

       COMM   Source process name

       SIG    Signal number. See signal(7).

       TPID   Target process ID

       RES    Result. 0 == success, a negative value (of the error code) for failure.

OVERHEAD
       This traces the kernel kill function and prints output for each event. As the rate of this is generally expected to be low (< 100/s), the  overhead  is
       also  expected to be negligible. If you have an application that is calling a very high rate of kill()s for some reason, then test and understand over‐
       head before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Brendan Gregg

SEE ALSO
       opensnoop(8), funccount(8)

USER COMMANDS								  2015-08-20								  killsnoop(8)
