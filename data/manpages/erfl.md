erf(3)								   Library Functions Manual								erf(3)

NAME
       erf, erff, erfl - error function

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double erf(double x);
       float erff(float x);
       long double erfl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       erf():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L || _XOPEN_SOURCE
	       || /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

       erff(), erfl():
	   _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L
	       || /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       These functions return the error function of x, defined as

	   erf(x) = 2/sqrt(pi) * integral from 0 to x of exp(-t*t) dt

RETURN VALUE
       On success, these functions return the value of the error function of x, a value in the range [-1, 1].

       If x is a NaN, a NaN is returned.

       If x is +0 (-0), +0 (-0) is returned.

       If x is positive infinity (negative infinity), +1 (-1) is returned.

       If x is subnormal, a range error occurs, and the return value is 2*x/sqrt(pi).

ERRORS
       See math_error(7) for information on how to determine whether an error has occurred when calling these functions.

       The following errors can occur:

       Range error: result underflow (x is subnormal)
	      An underflow floating-point exception (FE_UNDERFLOW) is raised.

       These functions do not set errno.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ erf(), erff(), erfl()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

       The variant returning double also conforms to SVr4, 4.3BSD.

SEE ALSO
       cerf(3), erfc(3), exp(3)

Linux man-pages 6.7							  2023-10-31									erf(3)
