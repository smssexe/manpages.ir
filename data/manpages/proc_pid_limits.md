proc_oid_limits(5)						      File Formats Manual						    proc_oid_limits(5)

NAME
       /proc/pid/limits - resource limits

DESCRIPTION
       /proc/pid/limits (since Linux 2.6.24)
	      This file displays the soft limit, hard limit, and units of measurement for each of the process's resource limits (see getrlimit(2)).  Up to and
	      including	 Linux 2.6.35, this file is protected to allow reading only by the real UID of the process.  Since Linux 2.6.36, this file is readable
	      by all users on the system.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_oid_limits(5)
