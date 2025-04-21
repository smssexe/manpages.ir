tcgetsid(3)							   Library Functions Manual							   tcgetsid(3)

NAME
       tcgetsid - get session ID

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _XOPEN_SOURCE 500	/* See feature_test_macros(7) */
       #include <termios.h>

       pid_t tcgetsid(int fd);

DESCRIPTION
       The  function  tcgetsid()  returns the session ID of the current session that has the terminal associated to fd as controlling terminal.	 This terminal
       must be the controlling terminal of the calling process.

RETURN VALUE
       When fd refers to the controlling terminal of our session, the function tcgetsid() will return the session ID of this session.  Otherwise,  -1  is  re‐
       turned, and errno is set to indicate the error.

ERRORS
       EBADF  fd is not a valid file descriptor.

       ENOTTY The calling process does not have a controlling terminal, or it has one but it is not described by fd.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ tcgetsid()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

       This function is implemented via the TIOCGSID ioctl(2), present since Linux 2.1.71.

SEE ALSO
       getsid(2)

Linux man-pages 6.7							  2023-10-31								   tcgetsid(3)
