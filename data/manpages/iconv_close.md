iconv_close(3)							   Library Functions Manual							iconv_close(3)

NAME
       iconv_close - deallocate descriptor for character set conversion

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <iconv.h>

       int iconv_close(iconv_t cd);

DESCRIPTION
       The iconv_close() function deallocates a conversion descriptor cd previously allocated using iconv_open(3).

RETURN VALUE
       On success, iconv_close() returns 0; otherwise, it returns -1 and sets errno to indicate the error.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ iconv_close()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

SEE ALSO
       iconv(3), iconv_open(3)

Linux man-pages 6.7							  2023-10-31								iconv_close(3)
