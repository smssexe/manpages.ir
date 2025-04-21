towctrans(3)							   Library Functions Manual							  towctrans(3)

NAME
       towctrans - wide-character transliteration

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       wint_t towctrans(wint_t wc, wctrans_t desc);

DESCRIPTION
       If  wc  is  a wide character, then the towctrans() function translates it according to the transliteration descriptor desc.  If wc is WEOF, WEOF is re‐
       turned.

       desc must be a transliteration descriptor returned by the wctrans(3) function.

RETURN VALUE
       The towctrans() function returns the translated wide character, or WEOF if wc is WEOF.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ towctrans()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of towctrans() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       towlower(3), towupper(3), wctrans(3)

Linux man-pages 6.7							  2023-10-31								  towctrans(3)
