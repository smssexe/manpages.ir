tm(3type)																	     tm(3type)

NAME
       tm - broken-down time

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <time.h>

       struct tm {
	   int	       tm_sec;	  /* Seconds	      [0, 60] */
	   int	       tm_min;	  /* Minutes	      [0, 59] */
	   int	       tm_hour;	  /* Hour	      [0, 23] */
	   int	       tm_mday;	  /* Day of the month [1, 31] */
	   int	       tm_mon;	  /* Month	      [0, 11]  (January = 0) */
	   int	       tm_year;	  /* Year minus 1900 */
	   int	       tm_wday;	  /* Day of the week  [0, 6]   (Sunday = 0) */
	   int	       tm_yday;	  /* Day of the year  [0, 365] (Jan/01 = 0) */
	   int	       tm_isdst;  /* Daylight savings flag */

	   long	       tm_gmtoff; /* Seconds East of UTC */
	   const char *tm_zone;	  /* Timezone abbreviation */
       };

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       tm_gmtoff, tm_zone:
	   Since glibc 2.20:
	       _DEFAULT_SOURCE
	   glibc 2.20 and earlier:
	       _BSD_SOURCE

DESCRIPTION
       Describes time, broken down into distinct components.

       tm_isdst	 describes  whether daylight saving time is in effect at the time described.  The value is positive if daylight saving time is in effect, zero
       if it is not, and negative if the information is not available.

       tm_gmtoff is the difference, in seconds, of the timezone represented by this broken-down time and UTC (this is the additive inverse of timezone(3)).

       tm_zone is the equivalent of tzname(3) for the timezone represented by this broken-down time.

VERSIONS
       In C90, tm_sec could represent values in the range [0, 61], which could represent a double leap second.	UTC doesn't permit double leap seconds, so  it
       was limited to 60 in C99.

       timezone(3), as a variable, is an XSI extension: some systems provide the V7-compatible timezone(3) function.  The tm_gmtoff field provides an alterna‐
       tive (with the opposite sign) for those systems.

       tm_zone	points	to  static  storage and may be overridden on subsequent calls to localtime(3) and similar functions (however, this never happens under
       glibc).

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

       tm_gmtoff and tm_zone originate from 4.3BSD-Tahoe (where tm_zone is a char *).

NOTES
       tm_sec can represent a leap second with the value 60.

SEE ALSO
       ctime(3), strftime(3), strptime(3), time(7)

Linux man-pages 6.7							  2023-10-31								     tm(3type)
