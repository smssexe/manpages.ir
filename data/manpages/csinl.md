csin(3)								   Library Functions Manual							       csin(3)

NAME
       csin, csinf, csinl - complex sine function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex csin(double complex z);
       float complex csinf(float complex z);
       long double complex csinl(long double complex z);

DESCRIPTION
       These functions calculate the complex sine of z.

       The complex sine function is defined as:

	   csin(z) = (exp(i * z) - exp(-i * z)) / (2 * i)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ csin(), csinf(), csinl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), casin(3), ccos(3), ctan(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       csin(3)
