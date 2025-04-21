timespec(3type)																       timespec(3type)

NAME
       timespec - time in seconds and nanoseconds

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <time.h>

       struct timespec {
	   time_t     tv_sec;	/* Seconds */
	   /* ... */  tv_nsec;	/* Nanoseconds [0, 999'999'999] */
       };

DESCRIPTION
       Describes times in seconds and nanoseconds.

       tv_nsec	is  of an implementation-defined signed type capable of holding the specified range.  Under glibc, this is usually long, and long long on X32.
       It can be safely down-cast to any concrete 32-bit integer type for processing.

VERSIONS
       Prior to C23, tv_nsec was long.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following headers also provide this type: <aio.h>, <mqueue.h>, <sched.h>, <signal.h>, <sys/select.h>, and <sys/stat.h>.

SEE ALSO
       clock_gettime(2), clock_nanosleep(2), nanosleep(2), timerfd_gettime(2), timer_gettime(2), time_t(3type), timeval(3type)

Linux man-pages 6.7							  2023-10-31							       timespec(3type)
