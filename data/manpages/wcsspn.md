wcsspn(3)							   Library Functions Manual							     wcsspn(3)

NAME
       wcsspn - get length of a prefix wide-character substring

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wchar.h>

       size_t wcsspn(const wchar_t *wcs, const wchar_t *accept);

DESCRIPTION
       The wcsspn() function is the wide-character equivalent of the strspn(3) function.  It determines the length of the longest initial segment of wcs which
       consists	 entirely  of  wide-characters	listed	in accept.  In other words, it searches for the first occurrence in the wide-character string wcs of a
       wide-character not contained in the wide-character string accept.

RETURN VALUE
       The wcsspn() function returns the number of wide characters in the longest initial segment of wcs which consists entirely of wide-characters listed  in
       accept.	 In  other  words,  it	returns the position of the first occurrence in the wide-character string wcs of a wide-character not contained in the
       wide-character string accept, or wcslen(wcs) if there is none.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ wcsspn()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C99.

SEE ALSO
       strspn(3), wcscspn(3)

Linux man-pages 6.7							  2023-10-31								     wcsspn(3)
