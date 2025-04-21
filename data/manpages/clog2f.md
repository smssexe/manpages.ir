clog2(3)							   Library Functions Manual							      clog2(3)

NAME
       clog2, clog2f, clog2l - base-2 logarithm of a complex number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex clog2(double complex z);
       float complex clog2f(float complex z);
       long double complex clog2l(long double complex z);

DESCRIPTION
       The call clog2(z) is equivalent to clog(z)/log(2).

       The other functions perform the same task for float and long double.

       Note that z close to zero will cause an overflow.

STANDARDS
       None.

HISTORY
       These function names are reserved for future use in C99.

       Not yet in glibc, as at glibc 2.19.

SEE ALSO
       cabs(3), cexp(3), clog(3), clog10(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      clog2(3)
