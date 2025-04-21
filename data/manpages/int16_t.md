intN_t(3type)																	 intN_t(3type)

NAME
       intN_t, int8_t, int16_t, int32_t, int64_t, uintN_t, uint8_t, uint16_t, uint32_t, uint64_t - fixed-width basic integer types

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdint.h>

       typedef /* ... */ int8_t;
       typedef /* ... */ int16_t;
       typedef /* ... */ int32_t;
       typedef /* ... */ int64_t;

       typedef /* ... */ uint8_t;
       typedef /* ... */ uint16_t;
       typedef /* ... */ uint32_t;
       typedef /* ... */ uint64_t;

       #define INT8_WIDTH   8
       #define INT16_WIDTH  16
       #define INT32_WIDTH  32
       #define INT64_WIDTH  64

       #define UINT8_WIDTH  8
       #define UINT16_WIDTH 16
       #define UINT32_WIDTH 32
       #define UINT64_WIDTH 64

       #define INT8_MAX	    /*	2**(INT8_WIDTH - 1) - 1	  */
       #define INT16_MAX    /*	2**(INT16_WIDTH - 1) - 1  */
       #define INT32_MAX    /*	2**(INT32_WIDTH - 1) - 1  */
       #define INT64_MAX    /*	2**(INT64_WIDTH - 1) - 1  */

       #define INT8_MIN	    /*	- 2**(INT8_WIDTH - 1)	  */
       #define INT16_MIN    /*	- 2**(INT16_WIDTH - 1)	  */
       #define INT32_MIN    /*	- 2**(INT32_WIDTH - 1)	  */
       #define INT64_MIN    /*	- 2**(INT64_WIDTH - 1)	  */

       #define UINT8_MAX    /*	2**INT8_WIDTH - 1	  */
       #define UINT16_MAX   /*	2**INT16_WIDTH - 1	  */
       #define UINT32_MAX   /*	2**INT32_WIDTH - 1	  */
       #define UINT64_MAX   /*	2**INT64_WIDTH - 1	  */

       #define INT8_C(c)    c ## /* ... */
       #define INT16_C(c)   c ## /* ... */
       #define INT32_C(c)   c ## /* ... */
       #define INT64_C(c)   c ## /* ... */

       #define UINT8_C(c)   c ## /* ... */
       #define UINT16_C(c)  c ## /* ... */
       #define UINT32_C(c)  c ## /* ... */
       #define UINT64_C(c)  c ## /* ... */

DESCRIPTION
       intN_t  are signed integer types of a fixed width of exactly N bits, N being the value specified in its type name.  They are be capable of storing val‐
       ues in the range [INTN_MIN, INTN_MAX], substituting N by the appropriate number.

       uintN_t are unsigned integer types of a fixed width of exactly N bits, N being the value specified in its type name.  They are capable of storing  val‐
       ues in the range [0, UINTN_MAX], substituting N by the appropriate number.

       According to POSIX, [u]int8_t, [u]int16_t, and [u]int32_t are required; [u]int64_t are only required in implementations that provide integer types with
       width 64; and all other types of this form are optional.

       The macros [U]INTN_WIDTH expand to the width in bits of these types (N).

       The macros [U]INTN_MAX expand to the maximum value that these types can hold.

       The macros INTN_MIN expand to the minimum value that these types can hold.

       The macros [U]INTN_C() expand their argument to an integer constant of type [u]intN_t.

       The  length  modifiers for the [u]intN_t types for the printf(3) family of functions are expanded by macros of the forms PRIdN, PRIiN, PRIuN, and PRIxN
       (defined in <inttypes.h>); resulting for example in %"PRId64" or %"PRIi64" for printing int64_t values.	The length modifiers for the  [u]intN_t	 types
       for the scanf(3) family of functions are expanded by macros of the forms SCNdN, SCNiN, SCNuN, and SCNxN, (defined in <inttypes.h>); resulting for exam‐
       ple in %"SCNu8" or %"SCNx8" for scanning uint8_t values.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

       The [U]INTN_WIDTH macros were added in C23.

NOTES
       The following header also provides these types: <inttypes.h>.  <arpa/inet.h> also provides uint16_t and uint32_t.

SEE ALSO
       intmax_t(3type), intptr_t(3type), printf(3)

Linux man-pages 6.7							  2023-10-31								 intN_t(3type)
