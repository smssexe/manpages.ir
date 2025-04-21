proc_pid_cwd(5)							      File Formats Manual						       proc_pid_cwd(5)

NAME
       /proc/pid/cwd - symbolic link to current working directory

DESCRIPTION
       /proc/pid/cwd
	      This is a symbolic link to the current working directory of the process.	To find out the current working directory of process 20, for instance,
	      you can do this:

		  $ cd /proc/20/cwd; pwd -P

	      In a multithreaded process, the contents of this symbolic link are not available if the main thread has already terminated (typically by calling
	      pthread_exit(3)).

	      Permission  to  dereference  or  read  (readlink(2))  this symbolic link is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see
	      ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_pid_cwd(5)
