stime(2)							      System Calls Manual							      stime(2)

NAME
       stime - set time

SYNOPSIS
       #include <time.h>

       [[deprecated]] int stime(const time_t *t);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       stime():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _SVID_SOURCE

DESCRIPTION
       NOTE: This function is deprecated; use clock_settime(2) instead.

       stime()	sets  the  system's  idea  of the time and date.  The time, pointed to by t, is measured in seconds since the Epoch, 1970-01-01 00:00:00 +0000
       (UTC).  stime() may be executed only by the superuser.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EFAULT Error in getting information from user space.

       EPERM  The calling process has insufficient privilege.  Under Linux, the CAP_SYS_TIME privilege is required.

STANDARDS
       None.

HISTORY
       SVr4.

       Starting with glibc 2.31, this function is no longer available to newly linked applications and is no longer declared in <time.h>.

SEE ALSO
       date(1), settimeofday(2), capabilities(7)

Linux man-pages 6.7							  2023-10-31								      stime(2)
