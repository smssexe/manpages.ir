cimag(3)							   Library Functions Manual							      cimag(3)

NAME
       cimag, cimagf, cimagl - get imaginary part of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double cimag(double complex z);
       float cimagf(float complex z);
       long double cimagl(long double complex z);

DESCRIPTION
       These functions return the imaginary part of the complex number z.

       One has:

	   z = creal(z) + I * cimag(z)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cimag(), cimagf(), cimagl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

VERSIONS
       GCC also supports __imag__.  That is a GNU extension.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), creal(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      cimag(3)
