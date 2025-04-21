itimerspec(3type)															     itimerspec(3type)

NAME
       itimerspec - interval for a timer with nanosecond precision

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <time.h>

       struct itimerspec {
	   struct timespec  it_interval;  /* Interval for periodic timer */
	   struct timespec  it_value;	  /* Initial expiration */
       };

DESCRIPTION
       Describes the initial expiration of a timer, and its interval, in seconds and nanoseconds.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       timerfd_create(2), timer_settime(2), timespec(3type)

Linux man-pages 6.7							  2023-10-31							     itimerspec(3type)
