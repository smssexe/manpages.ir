wcsncmp(3)							   Library Functions Manual							    wcsncmp(3)

NAME
       wcsncmp - compare two fixed-size wide-character strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       int wcsncmp(const wchar_t s1[.n], const wchar_t s2[.n], size_t n);

DESCRIPTION
       The  wcsncmp()  function	 is  the wide-character equivalent of the strncmp(3) function.	It compares the wide-character string pointed to by s1 and the
       wide-character string pointed to by s2, but at most n wide characters from each string.	In each string, the comparison extends only up	to  the	 first
       occurrence of a null wide character (L'\0'), if any.

RETURN VALUE
       The  wcsncmp()  function	 returns  zero	if  the	 wide-character strings at s1 and s2, truncated to at most length n, are equal.	 It returns an integer
       greater than zero if at the first differing position i (i < n), the corresponding wide-character s1[i] is greater than s2[i].  It  returns  an  integer
       less than zero if at the first differing position i (i < n), the corresponding wide-character s1[i] is less than s2[i].

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcsncmp()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strncmp(3), wcsncasecmp(3)

Linux man-pages 6.7							  2023-10-31								    wcsncmp(3)
