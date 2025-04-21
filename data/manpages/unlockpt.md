unlockpt(3)							   Library Functions Manual							   unlockpt(3)

NAME
       unlockpt - unlock a pseudoterminal master/slave pair

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _XOPEN_SOURCE
       #include <stdlib.h>

       int unlockpt(int fd);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       unlockpt():
	   Since glibc 2.24:
	       _XOPEN_SOURCE >= 500
	   glibc 2.23 and earlier:
	       _XOPEN_SOURCE

DESCRIPTION
       The unlockpt() function unlocks the slave pseudoterminal device corresponding to the master pseudoterminal referred to by the file descriptor fd.

       unlockpt() should be called before opening the slave side of a pseudoterminal.

RETURN VALUE
       When successful, unlockpt() returns 0.  Otherwise, it returns -1 and sets errno to indicate the error.

ERRORS
       EBADF  The fd argument is not a file descriptor open for writing.

       EINVAL The fd argument is not associated with a master pseudoterminal.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ unlockpt()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

SEE ALSO
       grantpt(3), posix_openpt(3), ptsname(3), pts(4), pty(7)

Linux man-pages 6.7							  2023-10-31								   unlockpt(3)
