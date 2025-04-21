MB_LEN_MAX(3)							   Library Functions Manual							 MB_LEN_MAX(3)

NAME
       MB_LEN_MAX - maximum multibyte length of a character across all locales

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <limits.h>

DESCRIPTION
       The MB_LEN_MAX macro is the maximum number of bytes needed to represent a single wide character, in any of the supported locales.

RETURN VALUE
       A constant integer greater than zero.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

NOTES
       The  entities MB_LEN_MAX and sizeof(wchar_t) are totally unrelated.  In glibc, MB_LEN_MAX is typically 16 (6 in glibc versions earlier than 2.2), while
       sizeof(wchar_t) is 4.

SEE ALSO
       MB_CUR_MAX(3)

Linux man-pages 6.7							  2023-03-30								 MB_LEN_MAX(3)
