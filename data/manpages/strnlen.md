strnlen(3)							   Library Functions Manual							    strnlen(3)

NAME
       strnlen - determine the length of a fixed-size string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <string.h>

       size_t strnlen(const char s[.maxlen], size_t maxlen);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       strnlen():
	   Since glibc 2.10:
	       _POSIX_C_SOURCE >= 200809L
	   Before glibc 2.10:
	       _GNU_SOURCE

DESCRIPTION
       The  strnlen()  function returns the number of bytes in the string pointed to by s, excluding the terminating null byte ('\0'), but at most maxlen.  In
       doing this, strnlen() looks only at the first maxlen characters in the string pointed to by s and never beyond s[maxlen-1].

RETURN VALUE
       The strnlen() function returns strlen(s), if that is less than maxlen, or maxlen if there is no null terminating ('\0') among the first maxlen  charac‐
       ters pointed to by s.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ strnlen()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2008.

SEE ALSO
       strlen(3)

Linux man-pages 6.7							  2023-10-31								    strnlen(3)
