difftime(3)							   Library Functions Manual							   difftime(3)

NAME
       difftime - calculate time difference

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <time.h>

       double difftime(time_t time1, time_t time0);

DESCRIPTION
       The difftime() function returns the number of seconds elapsed between time time1 and time time0, represented as a double.  Each time is a count of sec‐
       onds.

       difftime(b, a) acts like (b-a) except that the result does not overflow and is rounded to double.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ difftime()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

SEE ALSO
       date(1), gettimeofday(2), time(2), ctime(3), gmtime(3), localtime(3)

Linux man-pages 6.7							  2023-11-11								   difftime(3)
