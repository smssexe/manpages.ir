csqrt(3)							   Library Functions Manual							      csqrt(3)

NAME
       csqrt, csqrtf, csqrtl - complex square root

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex csqrt(double complex z);
       float complex csqrtf(float complex z);
       long double complex csqrtl(long double complex z);

DESCRIPTION
       These functions calculate the complex square root of z, with a branch cut along the negative real axis.	(That means that csqrt(-1+eps*I) will be close
       to I while csqrt(-1-eps*I) will be close to -I, if eps is a small positive real number.)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ csqrt(), csqrtf(), csqrtl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), cexp(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      csqrt(3)
