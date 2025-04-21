cproj(3)							   Library Functions Manual							      cproj(3)

NAME
       cproj, cprojf, cprojl - project into Riemann Sphere

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex cproj(double complex z);
       float complex cprojf(float complex z);
       long double complex cprojl(long double complex z);

DESCRIPTION
       These  functions	 project  a point in the plane onto the surface of a Riemann Sphere, the one-point compactification of the complex plane.  Each finite
       point z projects to z itself.  Every complex infinite value is projected to a single infinite value, namely to positive infinity on the real axis.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ cproj(), cprojf(), cprojl()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

       In glibc 2.11 and earlier, the implementation does something different (a stereographic projection onto a Riemann Sphere).

SEE ALSO
       cabs(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      cproj(3)
