memcmp(3)							   Library Functions Manual							     memcmp(3)

NAME
       memcmp - compare memory areas

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       int memcmp(const void s1[.n], const void s2[.n], size_t n);

DESCRIPTION
       The memcmp() function compares the first n bytes (each interpreted as unsigned char) of the memory areas s1 and s2.

RETURN VALUE
       The  memcmp() function returns an integer less than, equal to, or greater than zero if the first n bytes of s1 is found, respectively, to be less than,
       to match, or be greater than the first n bytes of s2.

       For a nonzero return value, the sign is determined by the sign of the difference between the first pair of bytes (interpreted as	 unsigned  char)  that
       differ in s1 and s2.

       If n is zero, the return value is zero.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ memcmp()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89, SVr4, 4.3BSD.

CAVEATS
       Do  not	use memcmp() to compare confidential data, such as cryptographic secrets, because the CPU time required for the comparison depends on the con‐
       tents of the addresses compared, this function is subject to timing-based side-channel attacks.	In such cases, a function that performs comparisons in
       deterministic time, depending only on n (the quantity of bytes compared) is required.  Some operating systems provide such a function  (e.g.,  NetBSD's
       consttime_memequal()), but no such function is specified in POSIX.  On Linux, you may need to implement such a function yourself.

SEE ALSO
       bstring(3), strcasecmp(3), strcmp(3), strcoll(3), strncasecmp(3), strncmp(3), wmemcmp(3)

Linux man-pages 6.7							  2023-10-31								     memcmp(3)
