getgid(2)							      System Calls Manual							     getgid(2)

NAME
       getgid, getegid - get group identity

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       gid_t getgid(void);
       gid_t getegid(void);

DESCRIPTION
       getgid() returns the real group ID of the calling process.

       getegid() returns the effective group ID of the calling process.

ERRORS
       These functions are always successful and never modify errno.

VERSIONS
       On Alpha, instead of a pair of getgid() and getegid() system calls, a single getxgid() system call is provided, which returns a pair of real and effec‐
       tive GIDs.  The glibc getgid() and getegid() wrapper functions transparently deal with this.  See syscall(2) for details regarding register mapping.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, 4.3BSD.

       The original Linux getgid() and getegid() system calls supported only 16-bit group IDs.	Subsequently, Linux 2.4 added getgid32() and getegid32(), sup‐
       porting 32-bit IDs.  The glibc getgid() and getegid() wrapper functions transparently deal with the variations across kernel versions.

SEE ALSO
       getresgid(2), setgid(2), setregid(2), credentials(7)

Linux man-pages 6.7							  2023-10-31								     getgid(2)
