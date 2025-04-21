ccosh(3)							   Library Functions Manual							      ccosh(3)

NAME
       ccosh, ccoshf, ccoshl - complex hyperbolic cosine

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <complex.h>

       double complex ccosh(double complex z);
       float complex ccoshf(float complex z);
       long double complex ccoshl(long double complex z);

DESCRIPTION
       These functions calculate the complex hyperbolic cosine of z.

       The complex hyperbolic cosine function is defined as:

	   ccosh(z) = (exp(z)+exp(-z))/2

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       glibc 2.1.  C99, POSIX.1-2001.

SEE ALSO
       cabs(3), cacosh(3), csinh(3), ctanh(3), complex(7)

Linux man-pages 6.7							  2023-10-31								      ccosh(3)
