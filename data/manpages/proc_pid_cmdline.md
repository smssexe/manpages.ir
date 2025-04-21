proc_pid_cmdline(5)						      File Formats Manual						   proc_pid_cmdline(5)

NAME
       /proc/pid/cmdline - command line

DESCRIPTION
       /proc/pid/cmdline
	      This  read-only  file  holds the complete command line for the process, unless the process is a zombie.  In the latter case, there is nothing in
	      this file: that is, a read on this file will return 0 characters.

	      For processes which are still running, the command-line arguments appear in this file in the same layout as they do in process  memory:  If  the
	      process is well-behaved, it is a set of strings separated by null bytes ('\0'), with a further null byte after the last string.

	      This  is the common case, but processes have the freedom to override the memory region and break assumptions about the contents or format of the
	      /proc/pid/cmdline file.

	      If, after an execve(2), the process modifies its argv strings, those changes will show up here.  This is not the same  thing  as	modifying  the
	      argv array.

	      Furthermore, a process may change the memory location that this file refers via prctl(2) operations such as PR_SET_MM_ARG_START.

	      Think of this file as the command line that the process wants you to see.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_pid_cmdline(5)
