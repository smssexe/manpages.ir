isatty(3)							   Library Functions Manual							     isatty(3)

NAME
       isatty - test whether a file descriptor refers to a terminal

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       int isatty(int fd);

DESCRIPTION
       The isatty() function tests whether fd is an open file descriptor referring to a terminal.

RETURN VALUE
       isatty() returns 1 if fd is an open file descriptor referring to a terminal; otherwise 0 is returned, and errno is set to indicate the error.

ERRORS
       EBADF  fd is not a valid file descriptor.

       ENOTTY fd refers to a file other than a terminal.  On some older kernels, some types of files resulted in the error EINVAL in this case (which is a vi‐
	      olation of POSIX, which specifies the error ENOTTY).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ isatty()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.

SEE ALSO
       fstat(2), ttyname(3)

Linux man-pages 6.7							  2023-10-31								     isatty(3)
