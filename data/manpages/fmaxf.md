fmax(3)								   Library Functions Manual							       fmax(3)

NAME
       fmax, fmaxf, fmaxl - determine maximum of two floating-point numbers

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double fmax(double x, double y);
       float fmaxf(float x, float y);
       long double fmaxl(long double x, long double y);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       fmax(), fmaxf(), fmaxl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L

DESCRIPTION
       These functions return the larger value of x and y.

RETURN VALUE
       These functions return the maximum of x and y.

       If one argument is a NaN, the other argument is returned.

       If both arguments are NaN, a NaN is returned.

ERRORS
       No errors occur.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ fmax(), fmaxf(), fmaxl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       fdim(3), fmin(3)

Linux man-pages 6.7							  2023-10-31								       fmax(3)
