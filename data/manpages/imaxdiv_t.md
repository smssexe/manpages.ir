div_t(3type)																	  div_t(3type)

NAME
       div_t, ldiv_t, lldiv_t, imaxdiv_t - quotient and remainder of an integer division

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdlib.h>

       typedef struct {
	   int quot; /* Quotient */
	   int rem;  /* Remainder */
       } div_t;

       typedef struct {
	   long quot; /* Quotient */
	   long rem;  /* Remainder */
       } ldiv_t;

       typedef struct {
	   long long quot; /* Quotient */
	   long long rem;  /* Remainder */
       } lldiv_t;

       #include <inttypes.h>

       typedef struct {
	   intmax_t quot; /* Quotient */
	   intmax_t rem;  /* Remainder */
       } imaxdiv_t;

DESCRIPTION
       [[l]l]div_t is the type of the value returned by the [[l]l]div(3) function.

       imaxdiv_t is the type of the value returned by the imaxdiv(3) function.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

SEE ALSO
       div(3), imaxdiv(3), ldiv(3), lldiv(3)

Linux man-pages 6.7							  2024-01-16								  div_t(3type)
