proc_pid_mem(5)							      File Formats Manual						       proc_pid_mem(5)

NAME
       /proc/pid/mem - memory

DESCRIPTION
       /proc/pid/mem
	      This file can be used to access the pages of a process's memory through open(2), read(2), and lseek(2).

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_pid_mem(5)
