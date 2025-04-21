wcsrtombs(3)							   Library Functions Manual							  wcsrtombs(3)

NAME
       wcsrtombs - convert a wide-character string to a multibyte string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       size_t wcsrtombs(char dest[restrict .len], const wchar_t **restrict src,
			size_t len, mbstate_t *restrict ps);

DESCRIPTION
       If  dest	 is  not NULL, the wcsrtombs() function converts the wide-character string *src to a multibyte string starting at dest.	 At most len bytes are
       written to dest.	 The shift state *ps is updated.  The conversion is effectively performed by repeatedly calling wcrtomb(dest, *src, ps),  as  long  as
       this call succeeds, and then incrementing dest by the number of bytes written and *src by one.  The conversion can stop for three reasons:

       •  A  wide character has been encountered that can not be represented as a multibyte sequence (according to the current locale).	 In this case, *src is
	  left pointing to the invalid wide character, (size_t) -1 is returned, and errno is set to EILSEQ.

       •  The length limit forces a stop.  In this case, *src is left pointing to the next wide character to be converted, and the number of bytes written  to
	  dest is returned.

       •  The  wide-character string has been completely converted, including the terminating null wide character (L'\0'), which has the side effect of bring‐
	  ing back *ps to the initial state.  In this case, *src is set to NULL, and the number of bytes written to dest, excluding the terminating null  byte
	  ('\0'), is returned.

       If  dest	 is  NULL,  len	 is  ignored, and the conversion proceeds as above, except that the converted bytes are not written out to memory, and that no
       length limit exists.

       In both of the above cases, if ps is NULL, a static anonymous state known only to the wcsrtombs() function is used instead.

       The programmer must ensure that there is room for at least len bytes at dest.

RETURN VALUE
       The wcsrtombs() function returns the number of bytes that make up the converted part of multibyte sequence, not including the  terminating  null	 byte.
       If a wide character was encountered which could not be converted, (size_t) -1 is returned, and errno set to EILSEQ.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌─────────────┬───────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
       │ Interface   │ Attribute     │ Value														     │
       ├─────────────┼───────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
       │ wcsrtombs() │ Thread safety │ MT-Unsafe race:wcsrtombs/!ps											     │
       └─────────────┴───────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

NOTES
       The behavior of wcsrtombs() depends on the LC_CTYPE category of the current locale.

       Passing NULL as ps is not multithread safe.

SEE ALSO
       iconv(3), mbsinit(3), wcrtomb(3), wcsnrtombs(3), wcstombs(3)

Linux man-pages 6.7							  2023-10-31								  wcsrtombs(3)
