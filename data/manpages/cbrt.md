cbrt(3)								   Library Functions Manual							       cbrt(3)

NAME
       cbrt, cbrtf, cbrtl - cube root function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double cbrt(double x);
       float cbrtf(float x);
       long double cbrtl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       cbrt():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
	       || _XOPEN_SOURCE >= 500
	       || /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

       cbrtf(), cbrtl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
	       || /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       These functions return the (real) cube root of x.  This function cannot fail; every representable real value has a real cube root, and rounding it to a
       representable value never causes overflow nor underflow.

RETURN VALUE
       These functions return the cube root of x.

       If x is +0, -0, positive infinity, negative infinity, or NaN, x is returned.

ERRORS
       No errors occur.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cbrt(), cbrtf(), cbrtl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

SEE ALSO
       pow(3), sqrt(3)

Linux man-pages 6.7							  2024-03-12								       cbrt(3)
