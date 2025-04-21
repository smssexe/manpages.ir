acos(3)								   Library Functions Manual							       acos(3)

NAME
       acos, acosf, acosl - arc cosine function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double acos(double x);
       float acosf(float x);
       long double acosl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       acosf(), acosl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
	       || /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       These functions calculate the arc cosine of x; that is the value whose cosine is x.

RETURN VALUE
       On success, these functions return the arc cosine of x in radians; the return value is in the range [0, pi].

       If x is a NaN, a NaN is returned.

       If x is +1, +0 is returned.

       If x is positive infinity or negative infinity, a domain error occurs, and a NaN is returned.

       If x is outside the range [-1, 1], a domain error occurs, and a NaN is returned.

ERRORS
       See math_error(7) for information on how to determine whether an error has occurred when calling these functions.

       The following errors can occur:

       Domain error: x is outside the range [-1, 1]
	      errno is set to EDOM.  An invalid floating-point exception (FE_INVALID) is raised.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ acos(), acosf(), acosl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

       The variant returning double also conforms to C89, SVr4, 4.3BSD.

SEE ALSO
       asin(3), atan(3), atan2(3), cacos(3), cos(3), sin(3), tan(3)

Linux man-pages 6.7							  2023-10-31								       acos(3)
