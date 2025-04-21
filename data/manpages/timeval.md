timeval(3type)																	timeval(3type)

NAME
       timeval - time in seconds and microseconds

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/time.h>

       struct timeval {
	   time_t	tv_sec;	  /* Seconds */
	   suseconds_t	tv_usec;  /* Microseconds */
       };

DESCRIPTION
       Describes times in seconds and microseconds.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following headers also provide this type: <sys/resource.h>, <sys/select.h>, and <utmpx.h>.

SEE ALSO
       gettimeofday(2), select(2), utimes(2), adjtime(3), futimes(3), timeradd(3), suseconds_t(3type), time_t(3type), timespec(3type)

Linux man-pages 6.7							  2023-10-31								timeval(3type)
