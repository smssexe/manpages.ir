getutmp(3)							   Library Functions Manual							    getutmp(3)

NAME
       getutmp, getutmpx - copy utmp structure to utmpx, and vice versa

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #define _GNU_SOURCE	       /* See feature_test_macros(7) */
       #include <utmpx.h>

       void getutmp(const struct utmpx *ux, struct utmp *u);
       void getutmpx(const struct utmp *u, struct utmpx *ux);

DESCRIPTION
       The  getutmp()  function	 copies	 the fields of the utmpx structure pointed to by ux to the corresponding fields of the utmp structure pointed to by u.
       The getutmpx() function performs the converse operation.

RETURN VALUE
       These functions do not return a value.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ getutmp(), getutmpx()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       None.

HISTORY
       glibc 2.1.1.  Solaris, NetBSD.

NOTES
       These functions exist primarily for compatibility with other systems where the utmp and utmpx structures contain different fields, or the size of  cor‐
       responding fields differs.  On Linux, the two structures contain the same fields, and the fields have the same sizes.

SEE ALSO
       utmpdump(1), getutent(3), utmp(5)

Linux man-pages 6.7							  2023-10-31								    getutmp(3)
