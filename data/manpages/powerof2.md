powerof2(3)							   Library Functions Manual							   powerof2(3)

NAME
       powerof2 - test if a value is a power of 2

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/param.h>

       int powerof2(x);

DESCRIPTION
       This macro returns true if x is a power of 2, and false otherwise.

       0 is considered a power of 2.  This can make sense considering wrapping of unsigned integers, and has interesting properties.

RETURN VALUE
       True or false, if x is a power of 2 or not, respectively.

STANDARDS
       BSD.

CAVEATS
       The arguments may be evaluated more than once.

       Because this macro is implemented using bitwise operations, some negative values can invoke undefined behavior.	For example, the following invokes un‐
       defined behavior: powerof2(INT_MIN);.  Call it only with unsigned types to be safe.

SEE ALSO
       stdc_bit_ceil(3), stdc_bit_floor(3)

Linux man-pages 6.7							  2023-10-31								   powerof2(3)
