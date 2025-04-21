wcsnlen(3)							   Library Functions Manual							    wcsnlen(3)

NAME
       wcsnlen - determine the length of a fixed-size wide-character string

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       size_t wcsnlen(const wchar_t s[.maxlen], size_t maxlen);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       wcsnlen():
	   Since glibc 2.10:
	       _POSIX_C_SOURCE >= 200809L
	   Before glibc 2.10:
	       _GNU_SOURCE

DESCRIPTION
       The  wcsnlen() function is the wide-character equivalent of the strnlen(3) function.  It returns the number of wide-characters in the string pointed to
       by s, not including the terminating null wide character (L'\0'), but at most maxlen wide characters (note: this parameter is not a byte count).	In do‐
       ing this, wcsnlen() looks at only the first maxlen wide characters at s and never beyond s[maxlen-1].

RETURN VALUE
       The wcsnlen() function returns wcslen(s), if that is less than maxlen, or maxlen if there is no null wide character among the first maxlen wide charac‐
       ters pointed to by s.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcsnlen()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.

SEE ALSO
       strnlen(3), wcslen(3)

Linux man-pages 6.7							  2023-10-31								    wcsnlen(3)
