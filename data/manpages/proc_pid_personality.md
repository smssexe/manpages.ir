proc_pid_personality(5)						      File Formats Manual					       proc_pid_personality(5)

NAME
       /proc/pid/personality - execution domain

DESCRIPTION
       /proc/pid/personality (since Linux 2.6.28)
	      This read-only file exposes the process's execution domain, as set by personality(2).  The value is displayed in hexadecimal notation.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15						       proc_pid_personality(5)
