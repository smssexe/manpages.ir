significand(3)							   Library Functions Manual							significand(3)

NAME
       significand, significandf, significandl - get mantissa of floating-point number

LIBRARY
       Math library (libm, -lm)

SYNOPSIS
       #include <math.h>

       double significand(double x);
       float significandf(float x);
       long double significandl(long double x);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       significand(), significandf(), significandl():
	   /* Since glibc 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       These functions return the mantissa of x scaled to the range [1, FLT_RADIX).  They are equivalent to

	   scalb(x, (double) -ilogb(x))

       This function exists mainly for use in certain standardized tests for IEEE 754 conformance.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ significand(), significandf(), significandl()										   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

       significand()
	      BSD.

HISTORY
       significand()
	      BSD.

SEE ALSO
       ilogb(3), scalb(3)

Linux man-pages 6.7							  2024-03-12								significand(3)
