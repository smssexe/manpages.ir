putwchar(3)							   Library Functions Manual							   putwchar(3)

NAME
       putwchar - write a wide character to standard output

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wint_t putwchar(wchar_t wc);

DESCRIPTION
       The putwchar() function is the wide-character equivalent of the putchar(3) function.  It writes the wide character wc to stdout.	 If ferror(stdout) be‐
       comes true, it returns WEOF.  If a wide character conversion error occurs, it sets errno to EILSEQ and returns WEOF.  Otherwise, it returns wc.

       For a nonlocking counterpart, see unlocked_stdio(3).

RETURN VALUE
       The putwchar() function returns wc if no error occurred, or WEOF to indicate an error.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ putwchar()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of putwchar() depends on the LC_CTYPE category of the current locale.

       It is reasonable to expect that putwchar() will actually write the multibyte sequence corresponding to the wide character wc.

SEE ALSO
       fputwc(3), unlocked_stdio(3)

Linux man-pages 6.7							  2023-10-31								   putwchar(3)
