catanh(3)							   Library Functions Manual							     catanh(3)

NAME
       catanh, catanhf, catanhl - complex arc tangents hyperbolic

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex catanh(double complex z);
       float complex catanhf(float complex z);
       long double complex catanhl(long double complex z);

DESCRIPTION
       These  functions calculate the complex arc hyperbolic tangent of z.  If y = catanh(z), then z = ctanh(y).  The imaginary part of y is chosen in the in‐
       terval [-pi/2,pi/2].

       One has:

	   catanh(z) = 0.5 * (clog(1 + z) - clog(1 - z))

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ catanh(), catanhf(), catanhl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

EXAMPLES
       /* Link with "-lm" */

       #include <complex.h>
       #include <stdio.h>
       #include <stdlib.h>
       #include <unistd.h>

       int
       main(int argc, char *argv[])
       {
	   double complex z, c, f;

	   if (argc != 3) {
	       fprintf(stderr, "Usage: %s <real> <imag>\n", argv[0]);
	       exit(EXIT_FAILURE);
	   }

	   z = atof(argv[1]) + atof(argv[2]) * I;

	   c = catanh(z);
	   printf("catanh() = %6.3f %6.3f*i\n", creal(c), cimag(c));

	   f = 0.5 * (clog(1 + z) - clog(1 - z));
	   printf("formula  = %6.3f %6.3f*i\n", creal(f), cimag(f));

	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       atanh(3), cabs(3), cimag(3), ctanh(3), complex(7)

Linux man-pages 6.7							  2023-10-31								     catanh(3)
