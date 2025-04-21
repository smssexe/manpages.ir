memccpy(3)							   Library Functions Manual							    memccpy(3)

NAME
       memccpy - copy memory area

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       void *memccpy(void dest[restrict .n], const void src[restrict .n],
		     int c, size_t n);

DESCRIPTION
       The memccpy() function copies no more than n bytes from memory area src to memory area dest, stopping when the character c is found.

       If the memory areas overlap, the results are undefined.

RETURN VALUE
       The memccpy() function returns a pointer to the next character in dest after c, or NULL if c was not found in the first n characters of src.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memccpy()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.

SEE ALSO
       bcopy(3), bstring(3), memcpy(3), memmove(3), strcpy(3), strncpy(3)

Linux man-pages 6.7							  2023-10-31								    memccpy(3)
