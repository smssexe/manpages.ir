casinh(3)							   Library Functions Manual							     casinh(3)

NAME
       casinh, casinhf, casinhl - complex arc sine hyperbolic

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex casinh(double complex z);
       float complex casinhf(float complex z);
       long double complex casinhl(long double complex z);

DESCRIPTION
       These  functions calculate the complex arc hyperbolic sine of z.	 If y = casinh(z), then z = csinh(y).  The imaginary part of y is chosen in the inter‐
       val [-pi/2,pi/2].

       One has:

	   casinh(z) = clog(z + csqrt(z * z + 1))

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ casinh(), casinhf(), casinhl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       asinh(3), cabs(3), cimag(3), csinh(3), complex(7)

Linux man-pages 6.7							  2023-10-31								     casinh(3)
