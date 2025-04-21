roundup(3)							   Library Functions Manual							    roundup(3)

NAME
       roundup - round up in steps

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/param.h>

       roundup(x, step);

DESCRIPTION
       This macro rounds x to the nearest multiple of step that is not less than x.

       It is typically used for rounding up a pointer to align it or increasing a buffer to be allocated.

       This API is not designed to be generic, and doesn't work in some cases that are not important for the typical use cases described above.	 See CAVEATS.

RETURN VALUE
       This macro returns the rounded value.

STANDARDS
       None.

CAVEATS
       The arguments may be evaluated more than once.

       x should be nonnegative, and step should be positive.

       If x + step would overflow or wrap around, the behavior is undefined.

SEE ALSO
       ceil(3), floor(3), lrint(3), rint(3), lround(3), round(3)

Linux man-pages 6.7							  2023-10-31								    roundup(3)
