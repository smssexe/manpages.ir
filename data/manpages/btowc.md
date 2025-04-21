btowc(3)							   Library Functions Manual							      btowc(3)

NAME
       btowc - convert single byte to wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wint_t btowc(int c);

DESCRIPTION
       The  btowc() function converts c, interpreted as a multibyte sequence of length 1, starting in the initial shift state, to a wide character and returns
       it.  If c is EOF or not a valid multibyte sequence of length 1, the btowc() function returns WEOF.

RETURN VALUE
       The btowc() function returns the wide character converted from the single byte c.  If c is EOF or not a valid multibyte sequence of length  1,  it  re‐
       turns WEOF.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ btowc()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

NOTES
       The behavior of btowc() depends on the LC_CTYPE category of the current locale.

       This  function should never be used.  It does not work for encodings which have state, and unnecessarily treats single bytes differently from multibyte
       sequences.  Use either mbtowc(3) or the thread-safe mbrtowc(3) instead.

SEE ALSO
       mbrtowc(3), mbtowc(3), wctob(3)

Linux man-pages 6.7							  2023-10-31								      btowc(3)
