cpow(3)								   Library Functions Manual							       cpow(3)

NAME
       cpow, cpowf, cpowl - complex power function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex cpow(double complex x, double complex z);
       float complex cpowf(float complex x, float complex z);
       long double complex cpowl(long double complex x,
				 long double complex z);

DESCRIPTION
       These functions calculate x raised to the power z (with a branch cut for x along the negative real axis).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cpow(), cpowf(), cpowl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), pow(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       cpow(3)
