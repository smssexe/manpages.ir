memmove(3)							   Library Functions Manual							    memmove(3)

NAME
       memmove - copy memory area

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       void *memmove(void dest[.n], const void src[.n], size_t n);

DESCRIPTION
       The  memmove() function copies n bytes from memory area src to memory area dest.	 The memory areas may overlap: copying takes place as though the bytes
       in src are first copied into a temporary array that does not overlap src or dest, and the bytes are then copied from the temporary array to dest.

RETURN VALUE
       The memmove() function returns a pointer to dest.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memmove()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

SEE ALSO
       bcopy(3), bstring(3), memccpy(3), memcpy(3), strcpy(3), strncpy(3), wmemmove(3)

Linux man-pages 6.7							  2023-10-31								    memmove(3)
