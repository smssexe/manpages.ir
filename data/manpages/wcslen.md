wcslen(3)							   Library Functions Manual							     wcslen(3)

NAME
       wcslen - determine the length of a wide-character string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       size_t wcslen(const wchar_t *s);

DESCRIPTION
       The  wcslen() function is the wide-character equivalent of the strlen(3) function.  It determines the length of the wide-character string pointed to by
       s, excluding the terminating null wide character (L'\0').

RETURN VALUE
       The wcslen() function returns the number of wide characters in s.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcslen()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       In cases where the input buffer may not contain a terminating null wide character, wcsnlen(3) should be used instead.

SEE ALSO
       strlen(3)

Linux man-pages 6.7							  2023-10-31								     wcslen(3)
