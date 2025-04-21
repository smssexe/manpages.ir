memcpy(3)							   Library Functions Manual							     memcpy(3)

NAME
       memcpy - copy memory area

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       void *memcpy(void dest[restrict .n], const void src[restrict .n],
		    size_t n);

DESCRIPTION
       The  memcpy() function copies n bytes from memory area src to memory area dest.	The memory areas must not overlap.  Use memmove(3) if the memory areas
       do overlap.

RETURN VALUE
       The memcpy() function returns a pointer to dest.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memcpy()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

CAVEATS
       Failure to observe the requirement that the memory areas do not overlap has been the source of significant bugs.	 (POSIX and the C  standards  are  ex‐
       plicit that employing memcpy() with overlapping areas produces undefined behavior.)  Most notably, in glibc 2.13 a performance optimization of memcpy()
       on some platforms (including x86-64) included changing the order in which bytes were copied from src to dest.

       This change revealed breakages in a number of applications that performed copying with overlapping areas.  Under the previous implementation, the order
       in  which  the  bytes  were copied had fortuitously hidden the bug, which was revealed when the copying order was reversed.  In glibc 2.14, a versioned
       symbol was added so that old binaries (i.e., those linked against glibc versions earlier than 2.14) employed a memcpy() implementation that safely han‐
       dles the overlapping buffers case (by providing an "older" memcpy() implementation that was aliased to memmove(3)).

SEE ALSO
       bcopy(3), bstring(3), memccpy(3), memmove(3), mempcpy(3), strcpy(3), strncpy(3), wmemcpy(3)

Linux man-pages 6.7							  2023-10-31								     memcpy(3)
