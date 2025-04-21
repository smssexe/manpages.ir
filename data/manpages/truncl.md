trunc(3)							   Library Functions Manual							      trunc(3)

NAME
       trunc, truncf, truncl - round to integer, toward zero

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double trunc(double x);
       float truncf(float x);
       long double truncl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       trunc(), truncf(), truncl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L

DESCRIPTION
       These functions round x to the nearest integer value that is not larger in magnitude than x.

RETURN VALUE
       These functions return the rounded integer value, in floating format.

       If x is integral, infinite, or NaN, x itself is returned.

ERRORS
       No errors occur.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ trunc(), truncf(), truncl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

NOTES
       The  integral  value returned by these functions may be too large to store in an integer type (int, long, etc.).	 To avoid an overflow, which will pro‐
       duce undefined results, an application should perform a range check on the returned value before assigning it to an integer type.

SEE ALSO
       ceil(3), floor(3), lrint(3), nearbyint(3), rint(3), round(3)

Linux man-pages 6.7							  2023-10-31								      trunc(3)
