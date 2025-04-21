proc_pid_comm(5)						      File Formats Manual						      proc_pid_comm(5)

NAME
       /proc/pid/comm - command name

DESCRIPTION
       /proc/pid/comm (since Linux 2.6.33)
	      This  file  exposes  the	process's comm value—that is, the command name associated with the process.  Different threads in the same process may
	      have different comm values, accessible via /proc/pid/task/tid/comm.  A thread may modify its comm value, or that of any of other thread  in  the
	      same  thread  group  (see	 the  discussion  of  CLONE_THREAD in clone(2)), by writing to the file /proc/self/task/tid/comm.  Strings longer than
	      TASK_COMM_LEN (16) characters (including the terminating null byte) are silently truncated.

	      This file provides a superset of the prctl(2) PR_SET_NAME and PR_GET_NAME operations, and is employed by pthread_setname_np(3) when used to  re‐
	      name threads other than the caller.  The value in this file is used for the %e specifier in /proc/sys/kernel/core_pattern; see core(5).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							      proc_pid_comm(5)
