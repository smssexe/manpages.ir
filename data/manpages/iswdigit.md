iswdigit(3)							   Library Functions Manual							   iswdigit(3)

NAME
       iswdigit - test for decimal digit wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       int iswdigit(wint_t wc);

DESCRIPTION
       The  iswdigit()	function  is the wide-character equivalent of the isdigit(3) function.	It tests whether wc is a wide character belonging to the wide-
       character class "digit".

       The wide-character class "digit" is a subclass of the wide-character class "xdigit", and therefore also a subclass of the wide-character class "alnum",
       of the wide-character class "graph" and of the wide-character class "print".

       Being a subclass of the wide character class "print", the wide-character class "digit" is disjoint from the wide-character class "cntrl".

       Being a subclass of the wide-character class "graph", the wide-character class "digit" is disjoint from the wide-character class "space" and  its  sub‐
       class "blank".

       Being a subclass of the wide-character class "alnum", the wide-character class "digit" is disjoint from the wide-character class "punct".

       The wide-character class "digit" is disjoint from the wide-character class "alpha" and therefore also disjoint from its subclasses "lower", "upper".

       The wide-character class "digit" always contains exactly the digits '0' to '9'.

RETURN VALUE
       The iswdigit() function returns nonzero if wc is a wide character belonging to the wide-character class "digit".	 Otherwise, it returns zero.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ iswdigit()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of iswdigit() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       isdigit(3), iswctype(3)

Linux man-pages 6.7							  2023-10-31								   iswdigit(3)
