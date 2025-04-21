clockid_t(3type)															      clockid_t(3type)

NAME
       clockid_t - clock ID for the clock and timer functions

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */ clockid_t;

DESCRIPTION
       Used for clock ID type in the clock and timer functions.	 It is defined as an arithmetic type.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following header also provides this type: <time.h>.

SEE ALSO
       clock_adjtime(2), clock_getres(2), clock_nanosleep(2), timer_create(2), clock_getcpuclockid(3)

Linux man-pages 6.7							  2023-10-31							      clockid_t(3type)
