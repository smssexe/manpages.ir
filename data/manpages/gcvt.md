gcvt(3)								   Library Functions Manual							       gcvt(3)

NAME
       gcvt - convert a floating-point number to a string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdlib.h>

       char *gcvt(double number, int ndigit, char *buf);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       gcvt():
	   Since glibc 2.17
	       (_XOPEN_SOURCE >= 500 && ! (_POSIX_C_SOURCE >= 200809L))
		   || /* glibc >= 2.20 */ _DEFAULT_SOURCE
		   || /* glibc <= 2.19 */ _SVID_SOURCE
	   glibc 2.12 to glibc 2.16:
	       (_XOPEN_SOURCE >= 500 && ! (_POSIX_C_SOURCE >= 200112L))
		   || _SVID_SOURCE
	   Before glibc 2.12:
	       _SVID_SOURCE || _XOPEN_SOURCE >= 500

DESCRIPTION
       The gcvt() function converts number to a minimal length null-terminated ASCII string and stores the result in buf.  It produces ndigit significant dig‐
       its in either printf(3) F format or E format.

RETURN VALUE
       The gcvt() function returns buf.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ gcvt()															   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

HISTORY
       Marked as LEGACY in POSIX.1-2001.  POSIX.1-2008 removed it, recommending the use of sprintf(3) instead (though snprintf(3) may be preferable).

SEE ALSO
       ecvt(3), fcvt(3), sprintf(3)

Linux man-pages 6.7							  2023-10-31								       gcvt(3)
