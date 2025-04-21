bcmp(3)								   Library Functions Manual							       bcmp(3)

NAME
       bcmp - compare byte sequences

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <strings.h>

       [[deprecated]] int bcmp(const void s1[.n], const void s2[.n], size_t n);

DESCRIPTION
       bcmp() is identical to memcmp(3); use the latter instead.

STANDARDS
       None.

HISTORY
       4.3BSD.	Marked as LEGACY in POSIX.1-2001; removed in POSIX.1-2008.

SEE ALSO
       memcmp(3)

Linux man-pages 6.7							  2023-11-02								       bcmp(3)
