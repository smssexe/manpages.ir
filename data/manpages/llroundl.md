lround(3)							   Library Functions Manual							     lround(3)

NAME
       lround, lroundf, lroundl, llround, llroundf, llroundl - round to nearest integer

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       long lround(double x);
       long lroundf(float x);
       long lroundl(long double x);

       long long llround(double x);
       long long llroundf(float x);
       long long llroundl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       All functions shown above:
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L

DESCRIPTION
       These  functions round their argument to the nearest integer value, rounding halfway cases away from zero, regardless of the current rounding direction
       (see fenv(3)).

       Note that unlike the round(3) and ceil(3), functions, the return type of these functions differs from that of their arguments.

RETURN VALUE
       These functions return the rounded integer value.

       If x is a NaN or an infinity, or the rounded value is too large to be stored in a long (long long in the case of the ll* functions), then a domain  er‐
       ror occurs, and the return value is unspecified.

ERRORS
       See math_error(7) for information on how to determine whether an error has occurred when calling these functions.

       The following errors can occur:

       Domain error: x is a NaN or infinite, or the rounded value is too large
	      An invalid floating-point exception (FE_INVALID) is raised.

       These functions do not set errno.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ lround(), lroundf(), lroundl(), llround(), llroundf(), llroundl()							   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       ceil(3), floor(3), lrint(3), nearbyint(3), rint(3), round(3)

Linux man-pages 6.7							  2023-10-31								     lround(3)
