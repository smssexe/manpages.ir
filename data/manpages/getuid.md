getuid(2)							      System Calls Manual							     getuid(2)

NAME
       getuid, geteuid - get user identity

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       uid_t getuid(void);
       uid_t geteuid(void);

DESCRIPTION
       getuid() returns the real user ID of the calling process.

       geteuid() returns the effective user ID of the calling process.

ERRORS
       These functions are always successful and never modify errno.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, 4.3BSD.

       In UNIX V6 the getuid() call returned (euid << 8) + uid.	 UNIX V7 introduced separate calls getuid() and geteuid().

       The  original Linux getuid() and geteuid() system calls supported only 16-bit user IDs.	Subsequently, Linux 2.4 added getuid32() and geteuid32(), sup‐
       porting 32-bit IDs.  The glibc getuid() and geteuid() wrapper functions transparently deal with the variations across kernel versions.

       On Alpha, instead of a pair of getuid() and geteuid() system calls, a single getxuid() system call is provided, which returns a pair of real and effec‐
       tive UIDs.  The glibc getuid() and geteuid() wrapper functions transparently deal with this.  See syscall(2) for details regarding register mapping.

SEE ALSO
       getresuid(2), setreuid(2), setuid(2), credentials(7)

Linux man-pages 6.7							  2023-10-31								     getuid(2)
