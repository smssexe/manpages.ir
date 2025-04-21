execsnoop(8)							    System Manager's Manual							  execsnoop(8)

NAME
       execsnoop - Trace new processes via exec() syscalls. Uses Linux eBPF/bcc.

SYNOPSIS
       execsnoop [-h] [-T] [-t] [-x] [--cgroupmap CGROUPMAP] [--mntnsmap MAPPATH] [-u USER] [-q] [-n NAME] [-l LINE] [-U] [--max-args MAX_ARGS]

DESCRIPTION
       execsnoop traces new processes, showing the filename executed and argument list.

       It works by traces the execve() system call (commonly used exec() variant).  This catches new processes that follow the fork->exec sequence, as well as
       processes  that	re-exec()  themselves.	Some applications fork() but do not exec(), eg, for worker processes, which won't be included in the execsnoop
       output.

       This works by tracing the kernel sys_execve() function using dynamic tracing, and will need updating to match any changes to this function.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include a time column (HH:MM:SS).

       -U     Include UID column.

       -t     Include a timestamp column.

       -u USER
	      Filter by UID (or username)

       -x     Include failed exec()s

       -q     Add "quotemarks" around arguments. Escape quotemarks in arguments with a backslash. For tracing empty arguments or arguments that contain white‐
	      space.

       -n NAME
	      Only print command lines matching this name (regex)

       -l LINE
	      Only print commands where arg contains this line (regex)

       --max-args MAXARGS
	      Maximum number of arguments parsed and displayed, defaults to 20

       --cgroupmap MAPPATH
	      Trace cgroups in this BPF map only (filtered in-kernel).

       --mntnsmap  MAPPATH
	      Trace mount namespaces in this BPF map only (filtered in-kernel).

       -P PPID
	      Trace this parent PID only.

       EXAMPLES

       Trace all exec() syscalls:
	      # execsnoop

       Trace all exec() syscalls, and include timestamps:
	      # execsnoop -t

       Display process UID:
	      # execsnoop -U

       Trace only UID 1000:
	      # execsnoop -u 1000

       Trace only processes launched by root and display UID column:
	      # execsnoop -Uu root

       Include failed exec()s:
	      # execsnoop -x

       Put quotemarks around arguments.
	      # execsnoop -q

       Only trace exec()s where the filename contains "mount":
	      # execsnoop -n mount

       Only trace exec()s where argument's line contains "testpkg":
	      # execsnoop -l testpkg

       Trace a set of cgroups only (see special_filtering.md from bcc sources for more details):
	      # execsnoop --cgroupmap /sys/fs/bpf/test01

FIELDS
       TIME   Time of exec() return, in HH:MM:SS format.

       TIME(s)
	      Time of exec() return, in seconds.

       UID    User ID

       PCOMM  Parent process/command name.

       PID    Process ID

       PPID   Parent process ID

       RET    Return value of exec(). 0 == successs. Failures are only shown when using the -x option.

       ARGS   Filename for the exec(), followed be up to 19 arguments. An ellipsis "..." is shown if the argument list is known to be truncated.

OVERHEAD
       This traces the kernel execve function and prints output for each event. As the rate of this is generally expected to be low (< 1000/s),	 the  overhead
       is also expected to be negligible. If you have an application that is calling a high rate of exec()s, then test and understand overhead before use.

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
       opensnoop(1)

USER COMMANDS								  2020-02-20								  execsnoop(8)
