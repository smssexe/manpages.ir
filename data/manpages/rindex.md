index(3)							   Library Functions Manual							      index(3)

NAME
       index, rindex - locate character in string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <strings.h>

       [[deprecated]] char *index(const char *s, int c);
       [[deprecated]] char *rindex(const char *s, int c);

DESCRIPTION
       index() is identical to strchr(3).

       rindex() is identical to strrchr(3).

       Use strchr(3) and strrchr(3) instead of these functions.

STANDARDS
       None.

HISTORY
       4.3BSD; marked as LEGACY in POSIX.1-2001.  Removed in POSIX.1-2008, recommending strchr(3) and strrchr(3) instead.

SEE ALSO
       strchr(3), strrchr(3)

Linux man-pages 6.7							  2023-10-31								      index(3)
