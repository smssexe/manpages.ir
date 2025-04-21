wcsncat(3)							   Library Functions Manual							    wcsncat(3)

NAME
       wcsncat - concatenate two wide-character strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wcsncat(wchar_t dest[restrict .n],
			const wchar_t src[restrict .n],
			size_t n);

DESCRIPTION
       The wcsncat() function is the wide-character equivalent of the strncat(3) function.  It copies at most n wide characters from the wide-character string
       pointed to by src to the end of the wide-character string pointed to by dest, and adds a terminating null wide character (L'\0').

       The strings may not overlap.

       The programmer must ensure that there is room for at least wcslen(dest)+n+1 wide characters at dest.

RETURN VALUE
       wcsncat() returns dest.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcsncat()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strncat(3), wcscat(3)

Linux man-pages 6.7							  2023-10-31								    wcsncat(3)
