intmax_t(3type)																       intmax_t(3type)

NAME
       intmax_t, uintmax_t - greatest-width basic integer types

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdint.h>

       typedef /* ... */ intmax_t;
       typedef /* ... */ uintmax_t;

       #define INTMAX_WIDTH  /* ... */
       #define UINTMAX_WIDTH INTMAX_WIDTH

       #define INTMAX_MAX    /*	 2**(INTMAX_WIDTH - 1) - 1  */
       #define INTMAX_MIN    /*	 - 2**(INTMAX_WIDTH - 1)    */
       #define UINTMAX_MAX   /*	 2**UINTMAX_WIDTH - 1	    */

       #define INTMAX_C(c)   c ## /* ... */
       #define UINTMAX_C(c)  c ## /* ... */

DESCRIPTION
       intmax_t is a signed integer type capable of representing any value of any basic signed integer type supported by the implementation.  It is capable of
       storing values in the range [INTMAX_MIN, INTMAX_MAX].

       uintmax_t  is an unsigned integer type capable of representing any value of any basic unsigned integer type supported by the implementation.  It is ca‐
       pable of storing values in the range [0, UINTMAX_MAX].

       The macros [U]INTMAX_WIDTH expand to the width in bits of these types.

       The macros [U]INTMAX_MAX expand to the maximum value that these types can hold.

       The macro INTMAX_MIN expands to the minimum value that intmax_t can hold.

       The macros [U]INTMAX_C() expand their argument to an integer constant of type [u]intmax_t.

       The length modifier for [u]intmax_t for the printf(3) and the scanf(3) families of functions is j; resulting commonly in %jd,  %ji,  %ju,  or  %jx  for
       printing [u]intmax_t values.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

NOTES
       The following header also provides these types: <inttypes.h>.

BUGS
       These types may not be as large as extended integer types, such as __int128

SEE ALSO
       int64_t(3type), intptr_t(3type), printf(3), strtoimax(3)

Linux man-pages 6.7							  2023-10-31							       intmax_t(3type)
