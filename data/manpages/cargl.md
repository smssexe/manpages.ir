carg(3)								   Library Functions Manual							       carg(3)

NAME
       carg, cargf, cargl - calculate the complex argument

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double carg(double complex z);
       float cargf(float complex z);
       long double cargl(long double complex z);

DESCRIPTION
       These functions calculate the complex argument (also called phase angle) of z, with a branch cut along the negative real axis.

       A complex number can be described by two real coordinates.  One may use rectangular coordinates and gets

	   z = x + I * y

       where x = creal(z) and y = cimag(z).

       Or one may use polar coordinates and gets

	   z = r * cexp(I * a)

       where r = cabs(z) is the "radius", the "modulus", the absolute value of z, and a = carg(z) is the "phase angle", the argument of z.

       One has:

	   tan(carg(z)) = cimag(z) / creal(z)

RETURN VALUE
       The return value is in the range of [-pi,pi].

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ carg(), cargf(), cargl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), complex(7)

Linux man-pages 6.7							  2023-10-31								       carg(3)
