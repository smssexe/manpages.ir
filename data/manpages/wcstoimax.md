wcstoimax(3)							   Library Functions Manual							  wcstoimax(3)

NAME
       wcstoimax, wcstoumax - convert wide-character string to integer

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stddef.h>
       #include <inttypes.h>

       intmax_t wcstoimax(const wchar_t *restrict nptr,
			  wchar_t **restrict endptr, int base);
       uintmax_t wcstoumax(const wchar_t *restrict nptr,
			  wchar_t **restrict endptr, int base);

DESCRIPTION
       These functions are just like wcstol(3) and wcstoul(3), except that they return a value of type intmax_t and uintmax_t, respectively.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ wcstoimax(), wcstoumax()											    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       imaxabs(3), imaxdiv(3), strtoimax(3), strtoumax(3), wcstol(3), wcstoul(3)

Linux man-pages 6.7							  2023-10-31								  wcstoimax(3)
