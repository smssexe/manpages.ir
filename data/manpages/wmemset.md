wmemset(3)							   Library Functions Manual							    wmemset(3)

NAME
       wmemset - fill an array of wide-characters with a constant wide character

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       wchar_t *wmemset(wchar_t wcs[.n], wchar_t wc, size_t n);

DESCRIPTION
       The  wmemset()  function	 is  the  wide-character equivalent of the memset(3) function.	It fills the array of n wide-characters starting at wcs with n
       copies of the wide character wc.

RETURN VALUE
       wmemset() returns wcs.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wmemset()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       memset(3)

Linux man-pages 6.7							  2023-10-31								    wmemset(3)
