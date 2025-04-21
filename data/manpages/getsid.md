getsid(2)							      System Calls Manual							     getsid(2)

NAME
       getsid - get session ID

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       pid_t getsid(pid_t pid);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       getsid():
	   _XOPEN_SOURCE >= 500
	       || /* Since glibc 2.12: */ _POSIX_C_SOURCE >= 200809L

DESCRIPTION
       getsid() returns the session ID of the process with process ID pid.  If pid is 0, getsid() returns the session ID of the calling process.

RETURN VALUE
       On success, a session ID is returned.  On error, (pid_t) -1 is returned, and errno is set to indicate the error.

ERRORS
       EPERM  A process with process ID pid exists, but it is not in the same session as the calling process, and the implementation considers this an error.

       ESRCH  No process with process ID pid was found.

VERSIONS
       Linux does not return EPERM.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4.  Linux 2.0.

NOTES
       See credentials(7) for a description of sessions and session IDs.

SEE ALSO
       getpgid(2), setsid(2), credentials(7)

Linux man-pages 6.7							  2023-10-31								     getsid(2)
