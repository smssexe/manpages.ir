csinh(3)							   Library Functions Manual							      csinh(3)

NAME
       csinh, csinhf, csinhl - complex hyperbolic sine

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex csinh(double complex z);
       float complex csinhf(float complex z);
       long double complex csinhl(long double complex z);

DESCRIPTION
       These functions calculate the complex hyperbolic sine of z.

       The complex hyperbolic sine function is defined as:

	   csinh(z) = (exp(z)-exp(-z))/2

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ csinh(), csinhf(), csinhl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), casinh(3), ccosh(3), ctanh(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      csinh(3)
