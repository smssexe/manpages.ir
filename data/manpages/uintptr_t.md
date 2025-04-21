intptr_t(3type)																       intptr_t(3type)

NAME
       intptr_t, uintptr_t - integer types wide enough to hold pointers

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdint.h>

       typedef /* ... */ intptr_t;
       typedef /* ... */ uintptr_t;

       #define INTPTR_WIDTH  /* ... */
       #define UINTPTR_WIDTH INTPTR_WIDTH

       #define INTPTR_MAX    /*	 2**(INTPTR_WIDTH - 1) - 1  */
       #define INTPTR_MIN    /*	 - 2**(INTPTR_WIDTH - 1)    */
       #define UINTPTR_MAX   /*	 2**UINTPTR_WIDTH - 1	    */

DESCRIPTION
       intptr_t	 is  a signed integer type such that any valid (void *) value can be converted to this type and then converted back.  It is capable of storing
       values in the range [INTPTR_MIN, INTPTR_MAX].

       uintptr_t is an unsigned integer type such that any valid (void *) value can be converted to this type and then converted back.	It is capable of stor‐
       ing values in the range [0, INTPTR_MAX].

       The macros [U]INTPTR_WIDTH expand to the width in bits of these types.

       The macros [U]INTPTR_MAX expand to the maximum value that these types can hold.

       The macro INTPTR_MIN expands to the minimum value that intptr_t can hold.

       The length modifiers for the [u]intptr_t types for the printf(3) family of functions are expanded by the macros PRIdPTR, PRIiPTR, and PRIuPTR  (defined
       in  <inttypes.h>); resulting commonly in %"PRIdPTR" or %"PRIiPTR" for printing intptr_t values.	The length modifiers for the [u]intptr_t types for the
       scanf(3) family of functions are expanded by the macros SCNdPTR, SCNiPTR, and SCNuPTR (defined in <inttypes.h>); resulting commonly in  %"SCNuPTR"  for
       scanning uintptr_t values.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

NOTES
       The following header also provides these types: <inttypes.h>.

SEE ALSO
       intmax_t(3type), void(3)

Linux man-pages 6.7							  2023-10-31							       intptr_t(3type)
