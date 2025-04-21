strspn(3)							   Library Functions Manual							     strspn(3)

NAME
       strspn, strcspn - get length of a prefix substring

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       size_t strspn(const char *s, const char *accept);
       size_t strcspn(const char *s, const char *reject);

DESCRIPTION
       The strspn() function calculates the length (in bytes) of the initial segment of s which consists entirely of bytes in accept.

       The strcspn() function calculates the length of the initial segment of s which consists entirely of bytes not in reject.

RETURN VALUE
       The strspn() function returns the number of bytes in the initial segment of s which consist only of bytes from accept.

       The strcspn() function returns the number of bytes in the initial segment of s which are not in the string reject.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ strspn(), strcspn()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

SEE ALSO
       memchr(3), strchr(3), string(3), strpbrk(3), strsep(3), strstr(3), strtok(3), wcscspn(3), wcsspn(3)

Linux man-pages 6.7							  2023-10-31								     strspn(3)
