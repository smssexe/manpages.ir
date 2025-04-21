exp10(3)							   Library Functions Manual							      exp10(3)

NAME
       exp10, exp10f, exp10l - base-10 exponential function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <math.h>

       double exp10(double x);
       float exp10f(float x);
       long double exp10l(long double x);

DESCRIPTION
       These functions return the value of 10 raised to the power of x.

RETURN VALUE
       On success, these functions return the base-10 exponential value of x.

       For various special cases, including the handling of infinity and NaN, as well as overflows and underflows, see exp(3).

ERRORS
       See math_error(7) for information on how to determine whether an error has occurred when calling these functions.

       For a discussion of the errors that can occur for these functions, see exp(3).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ exp10(), exp10f(), exp10l()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

HISTORY
       glibc 2.1.

BUGS
       Before glibc 2.19, the glibc implementation of these functions did not set errno to ERANGE when an underflow error occurred.

SEE ALSO
       cbrt(3), exp(3), exp2(3), log10(3), sqrt(3)

Linux man-pages 6.7							  2023-10-31								      exp10(3)
