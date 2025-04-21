towlower(3)							   Library Functions Manual							   towlower(3)

NAME
       towlower, towlower_l - convert a wide character to lowercase

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <wctype.h>

       wint_t towlower(wint_t wc);
       wint_t towlower_l(wint_t wc, locale_t locale);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       towlower_l():
	   Since glibc 2.10:
	       _XOPEN_SOURCE >= 700
	   Before glibc 2.10:
	       _GNU_SOURCE

DESCRIPTION
       The  towlower()	function is the wide-character equivalent of the tolower(3) function.  If wc is an uppercase wide character, and there exists a lower‐
       case equivalent in the current locale, it returns the lowercase equivalent of wc.  In all other cases, wc is returned unchanged.

       The towlower_l() function performs the same task, but performs the conversion based on the character type information in the locale  specified  by  lo‐
       cale.   The  behavior  of towlower_l() is undefined if locale is the special locale object LC_GLOBAL_LOCALE (see duplocale(3)) or is not a valid locale
       object handle.

       The argument wc must be representable as a wchar_t and be a valid character in the locale or be the value WEOF.

RETURN VALUE
       If wc was convertible to lowercase, towlower() returns its lowercase equivalent; otherwise it returns wc.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ towlower()													    │ Thread safety │ MT-Safe locale │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ towlower_l()													    │ Thread safety │ MT-Safe	     │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       towlower()
	      C11, POSIX.1-2008 (XSI).

       towlower_l()
	      POSIX.1-2008.

STANDARDS
       towlower()
	      C99, POSIX.1-2001 (XSI).	Obsolete in POSIX.1-2008 (XSI).

       towlower_l()
	      glibc 2.3.  POSIX.1-2008.

NOTES
       The behavior of these functions depends on the LC_CTYPE category of the locale.

       These functions are not very appropriate for dealing with Unicode characters, because Unicode knows about three cases: upper, lower, and title case.

SEE ALSO
       iswlower(3), towctrans(3), towupper(3), locale(7)

Linux man-pages 6.7							  2023-10-31								   towlower(3)
