wctob(3)							   Library Functions Manual							      wctob(3)

NAME
       wctob - try to represent a wide character as a single byte

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       int wctob(wint_t c);

DESCRIPTION
       The  wctob() function tests whether the multibyte representation of the wide character c, starting in the initial state, consists of a single byte.  If
       so, it is returned as an unsigned char.

       Never use this function.	 It cannot help you in writing internationalized programs.  Internationalized programs must never distinguish single-byte  and
       multibyte characters.

RETURN VALUE
       The wctob() function returns the single-byte representation of c, if it exists, or EOF otherwise.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wctob()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of wctob() depends on the LC_CTYPE category of the current locale.

       This  function  should never be used.  Internationalized programs must never distinguish single-byte and multibyte characters.  Use either wctomb(3) or
       the thread-safe wcrtomb(3) instead.

SEE ALSO
       btowc(3), wcrtomb(3), wctomb(3)

Linux man-pages 6.7							  2023-10-31								      wctob(3)
