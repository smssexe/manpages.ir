timer_t(3type)																	timer_t(3type)

NAME
       timer_t - timer ID

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */  timer_t;

DESCRIPTION
       Used for timer ID returned by timer_create(2).

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following header also provides timer_t: <time.h>.

SEE ALSO
       timer_create(2), timer_delete(2), timer_getoverrun(2), timer_settime(2)

Linux man-pages 6.7							  2023-10-31								timer_t(3type)
