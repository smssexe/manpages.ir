ptrdiff_t(3type)															      ptrdiff_t(3type)

NAME
       ptrdiff_t - count of elements or array index

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stddef.h>

       typedef /* ... */  ptrdiff_t;

DESCRIPTION
       Used  for a count of elements, or an array index.  It is the result of subtracting two pointers.	 It is a signed integer type capable of storing values
       in the range [PTRDIFF_MIN, PTRDIFF_MAX].

       The length modifier for ptrdiff_t for the printf(3) and the scanf(3) families of functions is  t,  resulting  commonly  in  %td	or  %ti	 for  printing
       ptrdiff_t values.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

SEE ALSO
       size_t(3type)

Linux man-pages 6.7							  2023-10-31							      ptrdiff_t(3type)
