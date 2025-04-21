time_t(3type)																	 time_t(3type)

NAME
       time_t, suseconds_t, useconds_t - integer time

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <time.h>

       typedef /* ... */  time_t;

       #include <sys/types.h>

       typedef /* ... */  suseconds_t;
       typedef /* ... */  useconds_t;

DESCRIPTION
       time_t Used for time in seconds.	 According to POSIX, it is an integer type.

       suseconds_t
	      Used for time in microseconds.  It is a signed integer type capable of storing values at least in the range [-1, 1000000].

       useconds_t
	      Used for time in microseconds.  It is an unsigned integer type capable of storing values at least in the range [0, 1000000].

STANDARDS
       time_t C11, POSIX.1-2008.

       suseconds_t
       useconds_t
	      POSIX.1-2008.

HISTORY
       time_t C89, POSIX.1-2001.

       suseconds_t
       useconds_t
	      POSIX.1-2001.

       <sched.h> defines time_t since POSIX.1-2008.

       POSIX.1-2001 defined useconds_t in <unistd.h> too.

NOTES
       On some architectures, the width of time_t can be controlled with the feature test macro _TIME_BITS.  See feature_test_macros(7).

       The following headers also provide time_t: <sched.h>, <sys/msg.h>, <sys/select.h>, <sys/sem.h>, <sys/shm.h>, <sys/stat.h>, <sys/time.h>, <sys/types.h>,
       and <utime.h>.

       The following headers also provide suseconds_t: <sys/select.h> and <sys/time.h>.

SEE ALSO
       stime(2), time(2), ctime(3), difftime(3), usleep(3), timeval(3type)

Linux man-pages 6.7							  2023-11-11								 time_t(3type)
