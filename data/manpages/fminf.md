fmin(3)								   Library Functions Manual							       fmin(3)

NAME
       fmin, fminf, fminl - determine minimum of two floating-point numbers

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double fmin(double x, double y);
       float fminf(float x, float y);
       long double fminl(long double x, long double y);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       fmin(), fminf(), fminl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L

DESCRIPTION
       These functions return the lesser value of x and y.

RETURN VALUE
       These functions return the minimum of x and y.

       If one argument is a NaN, the other argument is returned.

       If both arguments are NaN, a NaN is returned.

ERRORS
       No errors occur.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ fmin(), fminf(), fminl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       fdim(3), fmax(3)

Linux man-pages 6.7							  2023-10-31								       fmin(3)
