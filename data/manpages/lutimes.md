futimes(3)							   Library Functions Manual							    futimes(3)

NAME
       futimes, lutimes - change file timestamps

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/time.h>

       int futimes(int fd, const struct timeval tv[2]);
       int lutimes(const char *filename, const struct timeval tv[2]);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       futimes(), lutimes():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _BSD_SOURCE

DESCRIPTION
       futimes()  changes  the access and modification times of a file in the same way as utimes(2), with the difference that the file whose timestamps are to
       be changed is specified via a file descriptor, fd, rather than via a pathname.

       lutimes() changes the access and modification times of a file in the same way as utimes(2), with the difference that if filename refers to  a  symbolic
       link, then the link is not dereferenced: instead, the timestamps of the symbolic link are changed.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       Errors are as for utimes(2), with the following additions for futimes():

       EBADF  fd is not a valid file descriptor.

       ENOSYS The /proc filesystem could not be accessed.

       The following additional error may occur for lutimes():

       ENOSYS The kernel does not support this call; Linux 2.6.22 or later is required.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ futimes(), lutimes()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       Linux, BSD.

HISTORY
       futimes()
	      glibc 2.3.

       lutimes()
	      glibc 2.6.

NOTES
       lutimes() is implemented using the utimensat(2) system call.

SEE ALSO
       utime(2), utimensat(2), symlink(7)

Linux man-pages 6.7							  2023-10-31								    futimes(3)
