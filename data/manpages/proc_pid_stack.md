proc_pid_stack(5)						      File Formats Manual						     proc_pid_stack(5)

NAME
       /proc/pid/stack - kernel stack

DESCRIPTION
       /proc/pid/stack (since Linux 2.6.29)
	      This  file  provides  a symbolic trace of the function calls in this process's kernel stack.  This file is provided only if the kernel was built
	      with the CONFIG_STACKTRACE configuration option.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							     proc_pid_stack(5)
