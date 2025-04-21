proc_pid_wchan(5)						      File Formats Manual						     proc_pid_wchan(5)

NAME
       /proc/pid/wchan - wait channel

DESCRIPTION
       /proc/pid/wchan (since Linux 2.6.0)
	      The symbolic name corresponding to the location in the kernel where the process is sleeping.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							     proc_pid_wchan(5)
