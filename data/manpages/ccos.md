ccos(3)								   Library Functions Manual							       ccos(3)

NAME
       ccos, ccosf, ccosl - complex cosine function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex ccos(double complex z);
       float complex ccosf(float complex z);
       long double complex ccosl(long double complex z);

DESCRIPTION
       These functions calculate the complex cosine of z.

       The complex cosine function is defined as:

	   ccos(z) = (exp(i * z) + exp(-i * z)) / 2

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ ccos(), ccosf(), ccosl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), cacos(3), csin(3), ctan(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       ccos(3)
