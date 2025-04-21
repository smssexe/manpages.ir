iswgraph(3)							   Library Functions Manual							   iswgraph(3)

NAME
       iswgraph - test for graphic wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       int iswgraph(wint_t wc);

DESCRIPTION
       The  iswgraph()	function  is the wide-character equivalent of the isgraph(3) function.	It tests whether wc is a wide character belonging to the wide-
       character class "graph".

       The wide-character class "graph" is a subclass of the wide-character class "print".

       Being a subclass of the wide-character class "print", the wide-character class "graph" is disjoint from the wide-character class "cntrl".

       The wide-character class "graph" is disjoint from the wide-character class "space" and therefore also disjoint from its subclass "blank".

       The wide-character class "graph" contains all the wide characters from the wide-character class "print" except the space character.  It therefore  con‐
       tains the wide-character classes "alnum" and "punct".

RETURN VALUE
       The iswgraph() function returns nonzero if wc is a wide character belonging to the wide-character class "graph".	 Otherwise, it returns zero.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ iswgraph()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of iswgraph() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       isgraph(3), iswctype(3)

Linux man-pages 6.7							  2023-10-31								   iswgraph(3)
