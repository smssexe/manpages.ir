dysize(3)							   Library Functions Manual							     dysize(3)

NAME
       dysize - get number of days for a given year

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <time.h>

       int dysize(int year);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       dysize():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       The function returns 365 for a normal year and 366 for a leap year.  The calculation for leap year is based on:

	   (year) %4 == 0 && ((year) %100 != 0 || (year) %400 == 0)

       The formula is defined in the macro __isleap(year) also found in <time.h>.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ dysize()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

HISTORY
       SunOS 4.x.

       This is a compatibility function only.  Don't use it in new programs.

SEE ALSO
       strftime(3)

Linux man-pages 6.7							  2023-10-31								     dysize(3)
