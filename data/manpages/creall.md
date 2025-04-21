creal(3)							   Library Functions Manual							      creal(3)

NAME
       creal, crealf, creall - get real part of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double creal(double complex z);
       float crealf(float complex z);
       long double creall(long double complex z);

DESCRIPTION
       These functions return the real part of the complex number z.

       One has:

	   z = creal(z) + I * cimag(z)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ creal(), crealf(), creall()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

VERSIONS
       GCC supports also __real__.  That is a GNU extension.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), cimag(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      creal(3)
