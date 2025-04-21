cexp2(3)							   Library Functions Manual							      cexp2(3)

NAME
       cexp2, cexp2f, cexp2l - base-2 exponent of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex cexp2(double complex z);
       float complex cexp2f(float complex z);
       long double complex cexp2l(long double complex z);

DESCRIPTION
       The function returns 2 raised to the power of z.

STANDARDS
       These function names are reserved for future use in C99.

       As at glibc 2.31, these functions are not provided in glibc.

SEE ALSO
       cabs(3), cexp(3), clog10(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      cexp2(3)
