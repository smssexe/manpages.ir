NULL(3const)																	  NULL(3const)

NAME
       NULL - null pointer constant

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stddef.h>

       #define NULL  ((void *) 0)

DESCRIPTION
       NULL represents a null pointer constant, that is, a pointer that does not point to anything.

CONFORMING TO
       C99 and later; POSIX.1-2001 and later.

NOTES
       The following headers also provide NULL: <locale.h>, <stdio.h>, <stdlib.h>, <string.h>, <time.h>, <unistd.h>, and <wchar.h>.

CAVEATS
       It is undefined behavior to dereference a null pointer, and that usually causes a segmentation fault in practice.

       It is also undefined behavior to perform pointer arithmetic on it.

       NULL - NULL is undefined behavior, according to ISO C, but is defined to be 0 in C++.

       To avoid confusing human readers of the code, do not compare pointer variables to 0, and do not assign 0 to them.  Instead, always use NULL.

       NULL shouldn't be confused with NUL, which is an ascii(7) character, represented in C as '\0'.

BUGS
       When  it is necessary to set a pointer variable to a null pointer, it is not enough to use memset(3) to zero the pointer (this is usually done when ze‐
       roing a struct that contains pointers), since ISO C and POSIX don't guarantee that a bit pattern of all 0s represent a null pointer.  See the  EXAMPLES
       section in getaddrinfo(3) for an example program that does this correctly.

SEE ALSO
       void(3type)

Linux man-pages 6.7							  2023-10-31								  NULL(3const)
