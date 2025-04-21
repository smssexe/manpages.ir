proc_pid_environ(5)						      File Formats Manual						   proc_pid_environ(5)

NAME
       /proc/pid/environ - initial environment

DESCRIPTION
       /proc/pid/environ
	      This  file  contains the initial environment that was set when the currently executing program was started via execve(2).	 The entries are sepa‐
	      rated by null bytes ('\0'), and there may be a null byte at the end.  Thus, to print out the environment of process 1, you would do:

		  $ cat /proc/1/environ | tr '\000' '\n'

	      If, after an execve(2), the process modifies its environment (e.g., by calling functions such as putenv(3) or modifying the environ(7)  variable
	      directly), this file will not reflect those changes.

	      Furthermore, a process may change the memory location that this file refers via prctl(2) operations such as PR_SET_MM_ENV_START.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_pid_environ(5)
