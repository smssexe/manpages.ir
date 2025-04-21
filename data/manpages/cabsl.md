cabs(3)								   Library Functions Manual							       cabs(3)

NAME
       cabs, cabsf, cabsl - absolute value of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double cabs(double complex z);
       float cabsf(float complex z);
       long double cabsl(long double complex z);

DESCRIPTION
       These functions return the absolute value of the complex number z.  The result is a real number.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cabs(), cabsf(), cabsl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

NOTES
       The function is actually an alias for hypot(a, b) (or, equivalently, sqrt(a*a + b*b)).

SEE ALSO
       abs(3), cimag(3), hypot(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       cabs(3)
