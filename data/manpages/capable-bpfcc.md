capable(8)							    System Manager's Manual							    capable(8)

NAME
       capable - Trace security capability checks (cap_capable()).

SYNOPSIS
       capable [-h] [-v] [-p PID] [-K] [-U] [-x] [--cgroupmap MAPPATH]
		  [--mntnsmap MAPPATH] [--unique]

DESCRIPTION
       This traces security capability checks in the kernel, and prints details for each call. This can be useful for general debugging, and also security en‐
       forcement: determining a white list of capabilities an application needs.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF, bcc.

OPTIONS
       -h USAGE message.

       -v     Include  non-audit  capability checks. These are those deemed not interesting and not necessary to audit, such as CAP_SYS_ADMIN checks on memory
	      allocation to affect the behavior of overcommit.

       -K     Include kernel stack traces to the output.

       -U     Include user-space stack traces to the output.

       -x     Show extra fields in TID and INSETID columns.

       --cgroupmap MAPPATH
	      Trace cgroups in this BPF map only (filtered in-kernel).

       --mntnsmap  MAPPATH
	      Trace mount namespaces in this BPF map only (filtered in-kernel).

       --unique
	      Don't repeat stacks for the same PID or cgroup.

EXAMPLES
       Trace all capability checks system-wide:
	      # capable

       Trace capability checks for PID 181:
	      # capable -p 181

       Trace capability checks in a set of cgroups only (see special_filtering.md
	      from bcc sources for more details): # capable --cgroupmap /sys/fs/bpf/test01

FIELDS
       TIME(s)
	      Time of capability check: HH:MM:SS.

       UID    User ID.

       PID    Process ID.

       COMM   Process name.  CAP Capability number.  NAME Capability name. See capabilities(7) for descriptions.

       AUDIT  Whether this was an audit event. Use -v to include non-audit events.  INSETID Whether the INSETID bit was set (Linux >= 5.1).

OVERHEAD
       This adds low-overhead instrumentation to capability checks, which are expected to be low frequency, however, that depends on the application. Test  in
       a lab environment before use.

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
       capabilities(7)

USER COMMANDS								  2020-03-08								    capable(8)
