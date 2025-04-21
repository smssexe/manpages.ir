cacosh(3)							   Library Functions Manual							     cacosh(3)

NAME
       cacosh, cacoshf, cacoshl - complex arc hyperbolic cosine

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex cacosh(double complex z);
       float complex cacoshf(float complex z);
       long double complex cacoshl(long double complex z);

DESCRIPTION
       These  functions	 calculate the complex arc hyperbolic cosine of z.  If y = cacosh(z), then z = ccosh(y).  The imaginary part of y is chosen in the in‐
       terval [-pi,pi].	 The real part of y is chosen nonnegative.

       One has:

	   cacosh(z) = 2 * clog(csqrt((z + 1) / 2) + csqrt((z - 1) / 2))

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cacosh(), cacoshf(), cacoshl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.  glibc 2.1.

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

	   c = cacosh(z);
	   printf("cacosh() = %6.3f %6.3f*i\n", creal(c), cimag(c));

	   f = 2 * clog(csqrt((z + 1)/2) + csqrt((z - 1)/2));
	   printf("formula  = %6.3f %6.3f*i\n", creal(f), cimag(f));

	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       acosh(3), cabs(3), ccosh(3), cimag(3), complex(7)

Linux man-pages 6.7							  2023-10-31								     cacosh(3)
