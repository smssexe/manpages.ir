proc_pid_syscall(5)						      File Formats Manual						   proc_pid_syscall(5)

NAME
       /proc/pid/syscall - currently executed system call

DESCRIPTION
       /proc/pid/syscall (since Linux 2.6.27)
	      This  file  exposes  the	system call number and argument registers for the system call currently being executed by the process, followed by the
	      values of the stack pointer and program counter registers.  The values of all six argument registers are exposed, although most system calls use
	      fewer registers.

	      If the process is blocked, but not in a system call, then the file displays -1 in place of the system call number, followed by just  the	values
	      of the stack pointer and program counter.	 If process is not blocked, then the file contains just the string "running".

	      This file is present only if the kernel was configured with CONFIG_HAVE_ARCH_TRACEHOOK.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_ATTACH_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_pid_syscall(5)
