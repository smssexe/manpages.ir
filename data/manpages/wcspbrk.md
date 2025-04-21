wcspbrk(3)							   Library Functions Manual							    wcspbrk(3)

NAME
       wcspbrk - search a wide-character string for any of a set of wide characters

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wcspbrk(const wchar_t *wcs, const wchar_t *accept);

DESCRIPTION
       The  wcspbrk() function is the wide-character equivalent of the strpbrk(3) function.  It searches for the first occurrence in the wide-character string
       pointed to by wcs of any of the characters in the wide-character string pointed to by accept.

RETURN VALUE
       The wcspbrk() function returns a pointer to the first occurrence in wcs of any of the characters listed in accept.  If wcs contains none of these char‐
       acters, NULL is returned.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcspbrk()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strpbrk(3), wcschr(3), wcscspn(3)

Linux man-pages 6.7							  2023-10-31								    wcspbrk(3)
