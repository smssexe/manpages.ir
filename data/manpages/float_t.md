double_t(3type)																       double_t(3type)

NAME
       float_t, double_t - most efficient floating types

LIBRARY
       Math library (libm)

SYNOPSIS
       #include <math.h>

       typedef /* ... */ float_t;
       typedef /* ... */ double_t;

DESCRIPTION
       The  implementation's  most  efficient  floating types at least as wide as float and double respectively.  Their type depends on the value of the macro
       FLT_EVAL_METHOD (defined in <float.h>):

       FLT_EVAL_METHOD	     float_t	  double_t
       ────────────────────────────────────────────
	      0		       float	    double
	      1		      double	    double
	      2		 long double   long double

       For other values of FLT_EVAL_METHOD, the types of float_t and double_t are implementation-defined.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

SEE ALSO
       float.h(0p), math.h(0p)

Linux man-pages 6.7							  2023-10-31							       double_t(3type)
