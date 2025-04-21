proc_pid_auxv(5)						      File Formats Manual						      proc_pid_auxv(5)

NAME
       /proc/pid/auxv - exec(3) information

DESCRIPTION
       /proc/pid/auxv (since Linux 2.6.0)
	      This  contains  the contents of the ELF interpreter information passed to the process at exec time.  The format is one unsigned long ID plus one
	      unsigned long value for each entry.  The last entry contains two zeros.  See also getauxval(3).

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							      proc_pid_auxv(5)
