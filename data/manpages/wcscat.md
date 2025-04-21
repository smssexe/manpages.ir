wcscat(3)							   Library Functions Manual							     wcscat(3)

NAME
       wcscat - concatenate two wide-character strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wcscat(wchar_t *restrict dest, const wchar_t *restrict src);

DESCRIPTION
       The wcscat() function is the wide-character equivalent of the strcat(3) function.  It copies the wide-character string pointed to by src, including the
       terminating null wide character (L'\0'), to the end of the wide-character string pointed to by dest.

       The strings may not overlap.

       The programmer must ensure that there is room for at least wcslen(dest)+wcslen(src)+1 wide characters at dest.

RETURN VALUE
       wcscat() returns dest.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcscat()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strcat(3), wcpcpy(3), wcscpy(3), wcsncat(3)

Linux man-pages 6.7							  2023-10-31								     wcscat(3)
