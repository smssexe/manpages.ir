clock_t(3type)																	clock_t(3type)

NAME
       clock_t - system time

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <time.h>

       typedef /* ... */ clock_t;

DESCRIPTION
       Used for system time in clock ticks or CLOCKS_PER_SEC (defined in <time.h>).  According to POSIX, it is an integer type or a real-floating type.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

NOTES
       The following headers also provide this type: <sys/types.h> and <sys/times.h>.

SEE ALSO
       times(2), clock(3)

Linux man-pages 6.7							  2023-10-31								clock_t(3type)
