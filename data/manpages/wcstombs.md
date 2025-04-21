wcstombs(3)							   Library Functions Manual							   wcstombs(3)

NAME
       wcstombs - convert a wide-character string to a multibyte string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdlib.h>

       size_t wcstombs(char dest[restrict .n], const wchar_t *restrict src,
		       size_t n);

DESCRIPTION
       If  dest is not NULL, the wcstombs() function converts the wide-character string src to a multibyte string starting at dest.  At most n bytes are writ‐
       ten to dest.  The sequence of characters placed in dest begins in the initial shift state.  The conversion can stop for three reasons:

       •  A wide character has been encountered that can not be represented as a multibyte  sequence  (according  to  the  current  locale).   In  this	 case,
	  (size_t) -1 is returned.

       •  The length limit forces a stop.  In this case, the number of bytes written to dest is returned, but the shift state at this point is lost.

       •  The  wide-character  string has been completely converted, including the terminating null wide character (L'\0').  In this case, the conversion ends
	  in the initial shift state.  The number of bytes written to dest, excluding the terminating null byte ('\0'), is returned.

       The programmer must ensure that there is room for at least n bytes at dest.

       If dest is NULL, n is ignored, and the conversion proceeds as above, except that the converted bytes are not written out to memory, and no length limit
       exists.

       In order to avoid the case 2 above, the programmer should make sure n is greater than or equal to wcstombs(NULL,src,0)+1.

RETURN VALUE
       The wcstombs() function returns the number of bytes that make up the converted part of a multibyte sequence, not including the terminating  null	 byte.
       If a wide character was encountered which could not be converted, (size_t) -1 is returned.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcstombs()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

VERSIONS
       The function wcsrtombs(3) provides a better interface to the same functionality.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of wcstombs() depends on the LC_CTYPE category of the current locale.

SEE ALSO
       mblen(3), mbstowcs(3), mbtowc(3), wcsrtombs(3), wctomb(3)

Linux man-pages 6.7							  2023-10-31								   wcstombs(3)
