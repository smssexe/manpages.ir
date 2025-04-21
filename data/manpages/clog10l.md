clog10(3)							   Library Functions Manual							     clog10(3)

NAME
       clog10, clog10f, clog10l - base-10 logarithm of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <complex.h>

       double complex clog10(double complex z);
       float complex clog10f(float complex z);
       long double complex clog10l(long double complex z);

DESCRIPTION
       The call clog10(z) is equivalent to:

	   clog(z)/log(10)

       or equally:

	   log10(cabs(c)) + I * carg(c) / log(10)

       The other functions perform the same task for float and long double.

       Note that z close to zero will cause an overflow.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ clog10(), clog10f(), clog10l()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       GNU.

HISTORY
       glibc 2.1.

       The identifiers are reserved for future use in C99 and C11.

SEE ALSO
       cabs(3), cexp(3), clog(3), clog2(3), complex(7)

Linux man-pages 6.7							  2023-10-31								     clog10(3)
