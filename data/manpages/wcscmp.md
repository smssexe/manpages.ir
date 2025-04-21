wcscmp(3)							   Library Functions Manual							     wcscmp(3)

NAME
       wcscmp - compare two wide-character strings

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       int wcscmp(const wchar_t *s1, const wchar_t *s2);

DESCRIPTION
       The wcscmp() function is the wide-character equivalent of the strcmp(3) function.  It compares the wide-character string pointed to by s1 and the wide-
       character string pointed to by s2.

RETURN VALUE
       The  wcscmp() function returns zero if the wide-character strings at s1 and s2 are equal.  It returns an integer greater than zero if at the first dif‐
       fering position i, the corresponding wide-character s1[i] is greater than s2[i].	 It returns an integer less than zero if at the first differing	 posi‐
       tion i, the corresponding wide-character s1[i] is less than s2[i].

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcscmp()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strcmp(3), wcscasecmp(3), wmemcmp(3)

Linux man-pages 6.7							  2023-10-31								     wcscmp(3)
