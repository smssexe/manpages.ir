toascii(3)							   Library Functions Manual							    toascii(3)

NAME
       toascii - convert character to ASCII

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <ctype.h>

       [[deprecated]] int toascii(int c);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       toascii():
	   _XOPEN_SOURCE
	       || /* glibc >= 2.19: */ _DEFAULT_SOURCE
	       || /* glibc <= 2.19: */ _SVID_SOURCE || _BSD_SOURCE

DESCRIPTION
       toascii() converts c to a 7-bit unsigned char value that fits into the ASCII character set, by clearing the high-order bits.

RETURN VALUE
       The value returned is that of the converted character.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ toascii()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       SVr4, BSD, POSIX.1-2001.	 Obsolete in POSIX.1-2008, noting that it cannot be used portably in a localized application.

BUGS
       Many people will be unhappy if you use this function.  This function will convert accented letters into random characters.

SEE ALSO
       isascii(3), tolower(3), toupper(3)

Linux man-pages 6.7							  2023-10-31								    toascii(3)
