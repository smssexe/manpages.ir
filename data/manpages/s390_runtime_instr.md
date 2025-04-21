s390_runtime_instr(2)						      System Calls Manual						 s390_runtime_instr(2)

NAME
       s390_runtime_instr - enable/disable s390 CPU run-time instrumentation

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <asm/runtime_instr.h> /* Definition of S390_* constants */
       #include <sys/syscall.h>	      /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_s390_runtime_instr, int command, int signum);

       Note: glibc provides no wrapper for s390_runtime_instr(), necessitating the use of syscall(2).

DESCRIPTION
       The s390_runtime_instr() system call starts or stops CPU run-time instrumentation for the calling thread.

       The command argument controls whether run-time instrumentation is started (S390_RUNTIME_INSTR_START, 1) or stopped (S390_RUNTIME_INSTR_STOP, 2) for the
       calling thread.

       The  signum  argument  specifies	 the  number of a real-time signal.  This argument was used to specify a signal number that should be delivered to the
       thread if the run-time instrumentation buffer was full or if the run-time-instrumentation-halted interrupt had occurred.	 This feature was never	 used,
       and in Linux 4.4 support for this feature was removed; thus, in current kernels, this argument is ignored.

RETURN VALUE
       On  success, s390_runtime_instr() returns 0 and enables the thread for run-time instrumentation by assigning the thread a default run-time instrumenta‐
       tion control block.  The caller can then read and modify the control block and start the run-time instrumentation.  On error, -1 is returned and	 errno
       is set to indicate the error.

ERRORS
       EINVAL The value specified in command is not a valid command.

       EINVAL The  value  specified in signum is not a real-time signal number.	 From Linux 4.4 onwards, the signum argument has no effect, so that an invalid
	      signal number will not result in an error.

       ENOMEM Allocating memory for the run-time instrumentation control block failed.

       EOPNOTSUPP
	      The run-time instrumentation facility is not available.

STANDARDS
       Linux on s390.

HISTORY
       Linux 3.7.  System z EC12.

NOTES
       The asm/runtime_instr.h header file is available since Linux 4.16.

       Starting with Linux 4.4, support for signalling was removed, as was the check whether signum is a valid real-time signal.  For backwards	 compatibility
       with older kernels, it is recommended to pass a valid real-time signal number in signum and install a handler for that signal.

SEE ALSO
       syscall(2), signal(7)

Linux man-pages 6.7							  2023-10-31							 s390_runtime_instr(2)
