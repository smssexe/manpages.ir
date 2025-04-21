wcwidth(3)							   Library Functions Manual							    wcwidth(3)

NAME
       wcwidth - determine columns needed for a wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _XOPEN_SOURCE	   /* See feature_test_macros(7) */
       #include <wchar.h>

       int wcwidth(wchar_t c);

DESCRIPTION
       The  wcwidth()  function	 returns  the number of columns needed to represent the wide character c.  If c is a printable wide character, the value is at
       least 0.	 If c is null wide character (L'\0'), the value is 0.  Otherwise, -1 is returned.

RETURN VALUE
       The wcwidth() function returns the number of column positions for c.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ wcwidth()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

       Note that before glibc 2.2.5, glibc used the prototype

       int wcwidth(wint_t c);

NOTES
       The behavior of wcwidth() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       iswprint(3), wcswidth(3)

Linux man-pages 6.7							  2023-10-31								    wcwidth(3)
