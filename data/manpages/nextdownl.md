nextup(3)							   Library Functions Manual							     nextup(3)

NAME
       nextup, nextupf, nextupl, nextdown, nextdownf, nextdownl - return next floating-point number toward positive/negative infinity

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #define _GNU_SOURCE     /* See feature_test_macros(7) */
       #include <math.h>

       double nextup(double x);
       float nextupf(float x);
       long double nextupl(long double x);

       double nextdown(double x);
       float nextdownf(float x);
       long double nextdownl(long double x);

DESCRIPTION
       The nextup(), nextupf(), and nextupl() functions return the next representable floating-point number greater than x.

       If x is the smallest representable negative number in the corresponding type, these functions return -0.	 If x is 0, the returned value is the smallest
       representable positive number of the corresponding type.

       If  x is positive infinity, the returned value is positive infinity.  If x is negative infinity, the returned value is the largest representable finite
       negative number of the corresponding type.

       If x is Nan, the returned value is NaN.

       The value returned by nextdown(x) is -nextup(-x), and similarly for the other types.

RETURN VALUE
       See DESCRIPTION.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ nextup(), nextupf(), nextupl(), nextdown(), nextdownf(), nextdownl()							   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       These functions are described in IEEE Std 754-2008 - Standard for Floating-Point Arithmetic and ISO/IEC TS 18661.

HISTORY
       glibc 2.24.

SEE ALSO
       nearbyint(3), nextafter(3)

Linux man-pages 6.7							  2023-10-31								     nextup(3)
