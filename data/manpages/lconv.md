lconv(3type)																	  lconv(3type)

NAME
       lconv - numeric formatting information

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <locale.h>

       struct lconv {		     /* Values in the "C" locale: */
	   char *decimal_point;	     /* "." */
	   char *thousands_sep;	     /* "" */
	   char *grouping;	     /* "" */
	   char *mon_decimal_point;  /* "" */
	   char *mon_thousands_sep;  /* "" */
	   char *mon_grouping;	     /* "" */
	   char *positive_sign;	     /* "" */
	   char *negative_sign;	     /* "" */
	   char *currency_symbol;    /* "" */
	   char	 frac_digits;	     /* CHAR_MAX */
	   char	 p_cs_precedes;	     /* CHAR_MAX */
	   char	 n_cs_precedes;	     /* CHAR_MAX */
	   char	 p_sep_by_space;     /* CHAR_MAX */
	   char	 n_sep_by_space;     /* CHAR_MAX */
	   char	 p_sign_posn;	     /* CHAR_MAX */
	   char	 n_sign_posn;	     /* CHAR_MAX */
	   char *int_curr_symbol;    /* "" */
	   char	 int_frac_digits;    /* CHAR_MAX */
	   char	 int_p_cs_precedes;  /* CHAR_MAX */
	   char	 int_n_cs_precedes;  /* CHAR_MAX */
	   char	 int_p_sep_by_space; /* CHAR_MAX */
	   char	 int_n_sep_by_space; /* CHAR_MAX */
	   char	 int_p_sign_posn;    /* CHAR_MAX */
	   char	 int_n_sign_posn;    /* CHAR_MAX */
       };

DESCRIPTION
       Contains members related to the formatting of numeric values.  In the "C" locale, its members have the values shown in the comments above.

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       setlocale(3), localeconv(3), charsets(7), locale(7)

Linux man-pages 6.7							  2023-10-31								  lconv(3type)
