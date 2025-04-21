exit_group(2)							      System Calls Manual							 exit_group(2)

NAME
       exit_group - exit all threads in a process

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/syscall.h>	      /* Definition of SYS_* constants */
       #include <unistd.h>

       [[noreturn]] void syscall(SYS_exit_group, int status);

       Note: glibc provides no wrapper for exit_group(), necessitating the use of syscall(2).

DESCRIPTION
       This system call terminates all threads in the calling process's thread group.

RETURN VALUE
       This system call does not return.

STANDARDS
       Linux.

HISTORY
       Linux 2.5.35.

NOTES
       Since glibc 2.3, this is the system call invoked when the _exit(2) wrapper function is called.

SEE ALSO
       _exit(2)

Linux man-pages 6.7							  2023-10-31								 exit_group(2)
