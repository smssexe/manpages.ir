wmemcpy(3)							   Library Functions Manual							    wmemcpy(3)

NAME
       wmemcpy - copy an array of wide-characters

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wmemcpy(wchar_t dest[restrict .n],
			const wchar_t src[restrict .n],
			size_t n);

DESCRIPTION
       The  wmemcpy()  function is the wide-character equivalent of the memcpy(3) function.  It copies n wide characters from the array starting at src to the
       array starting at dest.

       The arrays may not overlap; use wmemmove(3) to copy between overlapping arrays.

       The programmer must ensure that there is room for at least n wide characters at dest.

RETURN VALUE
       wmemcpy() returns dest.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wmemcpy()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       memcpy(3), wcscpy(3), wmemmove(3), wmempcpy(3)

Linux man-pages 6.7							  2023-10-31								    wmemcpy(3)
