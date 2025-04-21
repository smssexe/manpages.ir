getw(3)								   Library Functions Manual							       getw(3)

NAME
       getw, putw - input and output of words (ints)

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>

       int getw(FILE *stream);
       int putw(int w, FILE *stream);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       getw(), putw():
	   Since glibc 2.3.3:
	       _XOPEN_SOURCE && ! (_POSIX_C_SOURCE >= 200112L)
		   || /* glibc >= 2.19: */ _DEFAULT_SOURCE
		   || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE
	   Before glibc 2.3.3:
	       _SVID_SOURCE || _BSD_SOURCE || _XOPEN_SOURCE

DESCRIPTION
       getw() reads a word (that is, an int) from stream.  It's provided for compatibility with SVr4.  We recommend you use fread(3) instead.

       putw() writes the word w (that is, an int) to stream.  It is provided for compatibility with SVr4, but we recommend you use fwrite(3) instead.

RETURN VALUE
       Normally, getw() returns the word read, and putw() returns 0.  On error, they return EOF.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ getw(), putw()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

HISTORY
       SVr4, SUSv2.

BUGS
       The value returned on error is also a legitimate data value.  ferror(3) can be used to distinguish between the two cases.

SEE ALSO
       ferror(3), fread(3), fwrite(3), getc(3), putc(3)

Linux man-pages 6.7							  2023-10-31								       getw(3)
