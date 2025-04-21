strcoll(3)							   Library Functions Manual							    strcoll(3)

NAME
       strcoll - compare two strings using the current locale

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       int strcoll(const char *s1, const char *s2);

DESCRIPTION
       The  strcoll()  function	 compares  the two strings s1 and s2.  It returns an integer less than, equal to, or greater than zero if s1 is found, respec‐
       tively, to be less than, to match, or be greater than s2.  The comparison is based on strings interpreted as appropriate for the program's current  lo‐
       cale for category LC_COLLATE.  (See setlocale(3).)

RETURN VALUE
       The  strcoll()  function	 returns  an  integer less than, equal to, or greater than zero if s1 is found, respectively, to be less than, to match, or be
       greater than s2, when both are interpreted as appropriate for the current locale.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ strcoll()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

NOTES
       In the POSIX or C locales strcoll() is equivalent to strcmp(3).

SEE ALSO
       memcmp(3), setlocale(3), strcasecmp(3), strcmp(3), string(3), strxfrm(3)

Linux man-pages 6.7							  2023-10-31								    strcoll(3)
