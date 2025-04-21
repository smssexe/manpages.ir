grantpt(3)							   Library Functions Manual							    grantpt(3)

NAME
       grantpt - grant access to the slave pseudoterminal

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdlib.h>

       int grantpt(int fd);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       grantpt():
	   Since glibc 2.24:
	       _XOPEN_SOURCE >= 500
	   glibc 2.23 and earlier:
	       _XOPEN_SOURCE

DESCRIPTION
       The grantpt() function changes the mode and owner of the slave pseudoterminal device corresponding to the master pseudoterminal referred to by the file
       descriptor  fd.	The user ID of the slave is set to the real UID of the calling process.	 The group ID is set to an unspecified value (e.g., tty).  The
       mode of the slave is set to 0620 (crw--w----).

       The behavior of grantpt() is unspecified if a signal handler is installed to catch SIGCHLD signals.

RETURN VALUE
       When successful, grantpt() returns 0.  Otherwise, it returns -1 and sets errno to indicate the error.

ERRORS
       EACCES The corresponding slave pseudoterminal could not be accessed.

       EBADF  The fd argument is not a valid open file descriptor.

       EINVAL The fd argument is valid but not associated with a master pseudoterminal.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ grantpt()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

       This is part of the UNIX 98 pseudoterminal support, see pts(4).

       Historical systems implemented this function via a set-user-ID helper binary called "pt_chown".	glibc on Linux before glibc 2.33 could do so as	 well,
       in  order  to support configurations with only BSD pseudoterminals; this support has been removed.  On modern systems this is either a no-op —with per‐
       missions configured on pty allocation, as is the case on Linux— or an ioctl(2).

SEE ALSO
       open(2), posix_openpt(3), ptsname(3), unlockpt(3), pts(4), pty(7)

Linux man-pages 6.7							  2023-10-31								    grantpt(3)
