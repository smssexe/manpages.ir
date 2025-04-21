iswctype(3)							   Library Functions Manual							   iswctype(3)

NAME
       iswctype - wide-character classification

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       int iswctype(wint_t wc, wctype_t desc);

DESCRIPTION
       If wc is a wide character having the character property designated by desc (or in other words: belongs to the character class designated by desc), then
       the iswctype() function returns nonzero.	 Otherwise, it returns zero.  If wc is WEOF, zero is returned.

       desc must be a character property descriptor returned by the wctype(3) function.

RETURN VALUE
       The iswctype() function returns nonzero if the wc has the designated property.  Otherwise, it returns 0.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ iswctype()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of iswctype() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       iswalnum(3),  iswalpha(3),  iswblank(3),	 iswcntrl(3),  iswdigit(3),  iswgraph(3),  iswlower(3),	 iswprint(3),  iswpunct(3),  iswspace(3), iswupper(3),
       iswxdigit(3), wctype(3)

Linux man-pages 6.7							  2023-10-31								   iswctype(3)
