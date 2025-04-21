casin(3)							   Library Functions Manual							      casin(3)

NAME
       casin, casinf, casinl - complex arc sine

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex casin(double complex z);
       float complex casinf(float complex z);
       long double complex casinl(long double complex z);

DESCRIPTION
       These functions calculate the complex arc sine of z.  If y = casin(z), then z = csin(y).	 The real part of y is chosen in the interval [-pi/2,pi/2].

       One has:

	   casin(z) = -i clog(iz + csqrt(1 - z * z))

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ casin(), casinf(), casinl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       clog(3), csin(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      casin(3)
