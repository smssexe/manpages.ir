ctan(3)								   Library Functions Manual							       ctan(3)

NAME
       ctan, ctanf, ctanl - complex tangent function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex ctan(double complex z);
       float complex ctanf(float complex z);
       long double complex ctanl(long double complex z);

DESCRIPTION
       These functions calculate the complex tangent of z.

       The complex tangent function is defined as:

	   ctan(z) = csin(z) / ccos(z)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ ctan(), ctanf(), ctanl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), catan(3), ccos(3), csin(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       ctan(3)
