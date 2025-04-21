getresuid(2)							      System Calls Manual							  getresuid(2)

NAME
       getresuid, getresgid - get real, effective, and saved user/group IDs

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <unistd.h>

       int getresuid(uid_t *ruid, uid_t *euid, uid_t *suid);
       int getresgid(gid_t *rgid, gid_t *egid, gid_t *sgid);

DESCRIPTION
       getresuid()  returns  the real UID, the effective UID, and the saved set-user-ID of the calling process, in the arguments ruid, euid, and suid, respec‐
       tively.	getresgid() performs the analogous task for the process's group IDs.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EFAULT One of the arguments specified an address outside the calling program's address space.

STANDARDS
       None.  These calls also appear on HP-UX and some of the BSDs.

HISTORY
       Linux 2.1.44, glibc 2.3.2.

       The original Linux getresuid() and getresgid() system calls supported only 16-bit user and group IDs.  Subsequently, Linux 2.4 added getresuid32()  and
       getresgid32(),  supporting  32-bit  IDs.	  The glibc getresuid() and getresgid() wrapper functions transparently deal with the variations across kernel
       versions.

SEE ALSO
       getuid(2), setresuid(2), setreuid(2), setuid(2), credentials(7)

Linux man-pages 6.7							  2023-10-31								  getresuid(2)
