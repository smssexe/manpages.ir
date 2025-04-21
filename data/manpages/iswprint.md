iswprint(3)							   Library Functions Manual							   iswprint(3)

NAME
       iswprint - test for printing wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       int iswprint(wint_t wc);

DESCRIPTION
       The  iswprint()	function  is the wide-character equivalent of the isprint(3) function.	It tests whether wc is a wide character belonging to the wide-
       character class "print".

       The wide-character class "print" is disjoint from the wide-character class "cntrl".

       The wide-character class "print" contains the wide-character class "graph".

RETURN VALUE
       The iswprint() function returns nonzero if wc is a wide character belonging to the wide-character class "print".	 Otherwise, it returns zero.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ iswprint()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of iswprint() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       isprint(3), iswctype(3)

Linux man-pages 6.7							  2023-10-31								   iswprint(3)
