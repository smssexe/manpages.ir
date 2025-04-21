wcschr(3)							   Library Functions Manual							     wcschr(3)

NAME
       wcschr - search a wide character in a wide-character string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wcschr(const wchar_t *wcs, wchar_t wc);

DESCRIPTION
       The  wcschr() function is the wide-character equivalent of the strchr(3) function.  It searches the first occurrence of wc in the wide-character string
       pointed to by wcs.

RETURN VALUE
       The wcschr() function returns a pointer to the first occurrence of wc in the wide-character string pointed to by wcs, or NULL if wc does not  occur  in
       the string.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcschr()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strchr(3), wcspbrk(3), wcsrchr(3), wcsstr(3), wmemchr(3)

Linux man-pages 6.7							  2023-10-31								     wcschr(3)
