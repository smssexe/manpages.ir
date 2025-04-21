ctanh(3)							   Library Functions Manual							      ctanh(3)

NAME
       ctanh, ctanhf, ctanhl - complex hyperbolic tangent

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex ctanh(double complex z);
       float complex ctanhf(float complex z);
       long double complex ctanhl(long double complex z);

DESCRIPTION
       These functions calculate the complex hyperbolic tangent of z.

       The complex hyperbolic tangent function is defined mathematically as:

	   ctanh(z) = csinh(z) / ccosh(z)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ ctanh(), ctanhf(), ctanhl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), catanh(3), ccosh(3), csinh(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      ctanh(3)
