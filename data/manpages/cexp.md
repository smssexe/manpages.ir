cexp(3)								   Library Functions Manual							       cexp(3)

NAME
       cexp, cexpf, cexpl - complex exponential function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex cexp(double complex z);
       float complex cexpf(float complex z);
       long double complex cexpl(long double complex z);

DESCRIPTION
       These functions calculate e (2.71828..., the base of natural logarithms) raised to the power of z.

       One has:

	   cexp(I * z) = ccos(z) + I * csin(z)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cexp(), cexpf(), cexpl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), cexp2(3), clog(3), cpow(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       cexp(3)
