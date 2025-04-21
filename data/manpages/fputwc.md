fputwc(3)							   Library Functions Manual							     fputwc(3)

NAME
       fputwc, putwc - write a wide character to a FILE stream

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>
       #include <wchar.h>

       wint_t fputwc(wchar_t wc, FILE *stream);
       wint_t putwc(wchar_t wc, FILE *stream);

DESCRIPTION
       The fputwc() function is the wide-character equivalent of the fputc(3) function.	 It writes the wide character wc to stream.  If ferror(stream) becomes
       true, it returns WEOF.  If a wide-character conversion error occurs, it sets errno to EILSEQ and returns WEOF.  Otherwise, it returns wc.

       The  putwc()  function  or  macro  functions  identically to fputwc().  It may be implemented as a macro, and may evaluate its argument more than once.
       There is no reason ever to use it.

       For nonlocking counterparts, see unlocked_stdio(3).

RETURN VALUE
       On success, fputwc() function returns wc.  Otherwise, WEOF is returned, and errno is set to indicate the error.

ERRORS
       Apart from the usual ones, there is

       EILSEQ Conversion of wc to the stream's encoding fails.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ fputwc(), putwc()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

NOTES
       The behavior of fputwc() depends on the LC_CTYPE category of the current locale.

       In the absence of additional information passed to the fopen(3) call, it is reasonable to expect that fputwc() will actually write  the	multibyte  se‐
       quence corresponding to the wide character wc.

SEE ALSO
       fgetwc(3), fputws(3), unlocked_stdio(3)

Linux man-pages 6.7							  2023-10-31								     fputwc(3)
