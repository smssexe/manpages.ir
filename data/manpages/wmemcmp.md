wmemcmp(3)							   Library Functions Manual							    wmemcmp(3)

NAME
       wmemcmp - compare two arrays of wide-characters

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       int wmemcmp(const wchar_t s1[.n], const wchar_t s2[.n], size_t n);

DESCRIPTION
       The  wmemcmp()  function	 is the wide-character equivalent of the memcmp(3) function.  It compares the n wide-characters starting at s1 and the n wide-
       characters starting at s2.

RETURN VALUE
       The wmemcmp() function returns zero if the wide-character arrays of size n at s1 and s2 are equal.  It returns an integer greater than zero if  at  the
       first differing position i (i < n), the corresponding wide-character s1[i] is greater than s2[i].  It returns an integer less than zero if at the first
       differing position i (i < n), the corresponding wide-character s1[i] is less than s2[i].

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wmemcmp()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       memcmp(3), wcscmp(3)

Linux man-pages 6.7							  2023-10-31								    wmemcmp(3)
