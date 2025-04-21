RENICE(1)								 User Commands								     RENICE(1)

NAME
       renice - alter priority of running processes

SYNOPSIS
       renice [--priority|--relative] priority [-g|-p|-u] identifier...

DESCRIPTION
       renice alters the scheduling priority of one or more running processes. The first argument is the priority value to be used. The other arguments are
       interpreted as process IDs (by default), process group IDs, user IDs, or user names. renice'ing a process group causes all processes in the process
       group to have their scheduling priority altered. renice'ing a user causes all processes owned by the user to have their scheduling priority altered.

       If no -n, --priority or --relative option is used, then the priority is set as absolute.

OPTIONS
       -n priority
	   Specify the absolute or relative (depending on environment variable POSIXLY_CORRECT) scheduling priority to be used for the process, process group,
	   or user. Use of the option -n is optional, but when used, it must be the first argument. See NOTES for more information.

       --priority priority
	   Specify an absolute scheduling priority. Priority is set to the given value. This is the default, when no option is specified.

       --relative priority
	   Specify a relative scheduling priority. Same as the standard POSIX -n option. Priority gets incremented/decremented by the given value.

       -g, --pgrp
	   Interpret the succeeding arguments as process group IDs.

       -p, --pid
	   Interpret the succeeding arguments as process IDs (the default).

       -u, --user
	   Interpret the succeeding arguments as usernames or UIDs.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

FILES
       /etc/passwd
	   to map user names to user IDs

NOTES
       Users other than the superuser may only alter the priority of processes they own. Furthermore, an unprivileged user can only increase the "nice value"
       (i.e., choose a lower priority) and such changes are irreversible unless (since Linux 2.6.12) the user has a suitable "nice" resource limit (see
       ulimit(1p) and getrlimit(2)).

       The superuser may alter the priority of any process and set the priority to any value in the range -20 to 19. Useful priorities are: 19 (the affected
       processes will run only when nothing else in the system wants to), 0 (the "base" scheduling priority), anything negative (to make things go very fast).

       For historical reasons in this implementation, the -n option did not follow the POSIX specification. Therefore, instead of setting a relative priority,
       it sets an absolute priority by default. As this may not be desirable, this behavior can be controlled by setting the environment variable
       POSIXLY_CORRECT to be fully POSIX compliant. See the -n option for details. See --relative and --priority for options that do not change behavior
       depending on environment variables.

HISTORY
       The renice command appeared in 4.0BSD.

EXAMPLES
       The following command would change the priority of the processes with PIDs 987 and 32, plus all processes owned by the users daemon and root:

       renice +1 987 -u daemon root -p 32

SEE ALSO
       nice(1), chrt(1), getpriority(2), setpriority(2), credentials(7), sched(7)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The renice command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								     RENICE(1)
