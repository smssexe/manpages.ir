conj(3)								   Library Functions Manual							       conj(3)

NAME
       conj, conjf, conjl - calculate the complex conjugate

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex conj(double complex z);
       float complex conjf(float complex z);
       long double complex conjl(long double complex z);

DESCRIPTION
       These functions return the complex conjugate value of z.	 That is the value obtained by changing the sign of the imaginary part.

       One has:

	   cabs(z) = csqrt(z * conj(z))

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ conj(), conjf(), conjl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), csqrt(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       conj(3)
