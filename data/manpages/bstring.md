bstring(3)							   Library Functions Manual							    bstring(3)

NAME
       bcmp, bcopy, bzero, memccpy, memchr, memcmp, memcpy, memfrob, memmem, memmove, memset - byte string operations

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       int bcmp(const void s1[.n], const void s2[.n], size_t n);

       void bcopy(const void src[.n], void dest[.n], size_t n);

       void bzero(void s[.n], size_t n);

       void *memccpy(void dest[.n], const void src[.n], int c, size_t n);

       void *memchr(const void s[.n], int c, size_t n);

       int memcmp(const void s1[.n], const void s2[.n], size_t n);

       void *memcpy(void dest[.n], const void src[.n], size_t n);

       void *memfrob(void s[.n], size_t n);

       void *memmem(const void haystack[.haystacklen], size_t haystacklen,
		    const void needle[.needlelen], size_t needlelen);

       void *memmove(void dest[.n], const void src[.n], size_t n);

       void *memset(void s[.n], int c, size_t n);

DESCRIPTION
       The  byte  string functions perform operations on strings (byte arrays) that are not necessarily null-terminated.  See the individual man pages for de‐
       scriptions of each function.

NOTES
       The functions bcmp() and bcopy() are obsolete.  Use memcmp() and memmove() instead.

SEE ALSO
       bcmp(3), bcopy(3), bzero(3), memccpy(3), memchr(3), memcmp(3), memcpy(3), memfrob(3), memmem(3), memmove(3), memset(3), string(3)

Linux man-pages 6.7							  2023-10-31								    bstring(3)
