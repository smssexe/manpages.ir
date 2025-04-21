wctrans(3)							   Library Functions Manual							    wctrans(3)

NAME
       wctrans - wide-character translation mapping

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       wctrans_t wctrans(const char *name);

DESCRIPTION
       The wctrans_t type represents a mapping which can map a wide character to another wide character.  Its nature is implementation-dependent, but the spe‐
       cial value (wctrans_t) 0 denotes an invalid mapping.  Nonzero wctrans_t values can be passed to the towctrans(3) function to actually perform the wide-
       character mapping.

       The  wctrans()  function	 returns a mapping, given by its name.	The set of valid names depends on the LC_CTYPE category of the current locale, but the
       following names are valid in all locales.

	   "tolower" - realizes the tolower(3) mapping
	   "toupper" - realizes the toupper(3) mapping

RETURN VALUE
       The wctrans() function returns a mapping descriptor if the name is valid.  Otherwise, it returns (wctrans_t) 0.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ wctrans()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of wctrans() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       towctrans(3)

Linux man-pages 6.7							  2023-10-31								    wctrans(3)
