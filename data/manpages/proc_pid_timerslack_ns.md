proc_pid_timerslack_ns(5)					      File Formats Manual					     proc_pid_timerslack_ns(5)

NAME
       /proc/pid/timerslack_ns - timer slack in nanoseconds

DESCRIPTION
       /proc/pid/timerslack_ns (since Linux 4.6)
	      This file exposes the process's "current" timer slack value, expressed in nanoseconds.  The file is writable, allowing the process's timer slack
	      value  to be changed.  Writing 0 to this file resets the "current" timer slack to the "default" timer slack value.  For further details, see the
	      discussion of PR_SET_TIMERSLACK in prctl(2).

	      Initially, permission to access this file was governed by a ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check (see ptrace(2)).	However,  this
	      was  subsequently	 deemed too strict a requirement (and had the side effect that requiring a process to have the CAP_SYS_PTRACE capability would
	      also allow it to view and change any process's memory).  Therefore, since Linux 4.9, only the (weaker) CAP_SYS_NICE capability  is  required  to
	      access this file.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15						     proc_pid_timerslack_ns(5)
