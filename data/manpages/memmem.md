memmem(3)							   Library Functions Manual							     memmem(3)

NAME
       memmem - locate a substring

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	   /* See feature_test_macros(7) */
       #include <string.h>

       void *memmem(const void haystack[.haystacklen], size_t haystacklen,
		    const void needle[.needlelen], size_t needlelen);

DESCRIPTION
       The  memmem()  function	finds  the  start  of  the  first occurrence of the substring needle of length needlelen in the memory area haystack of length
       haystacklen.

RETURN VALUE
       The memmem() function returns a pointer to the beginning of the substring, or NULL if the substring is not found.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memmem()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

HISTORY
       musl libc 0.9.7; FreeBSD 6.0, OpenBSD 5.4, NetBSD, Illumos.

BUGS
       In glibc 2.0, if needle is empty, memmem() returns a pointer to the last byte of haystack.  This is fixed in glibc 2.1.

SEE ALSO
       bstring(3), strstr(3)

Linux man-pages 6.7							  2023-10-31								     memmem(3)
