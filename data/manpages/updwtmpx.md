updwtmp(3)							   Library Functions Manual							    updwtmp(3)

NAME
       updwtmp, logwtmp - append an entry to the wtmp file

LIBRARY
       System utilities library (libutil, -lutil)

SYNOPSIS
       #include <utmp.h>

       void updwtmp(const char *wtmp_file, const struct utmp *ut);
       void logwtmp(const char *line, const char *name, const char *host);

DESCRIPTION
       updwtmp() appends the utmp structure ut to the wtmp file.

       logwtmp() constructs a utmp structure using line, name, host, current time, and current process ID.  Then it calls updwtmp() to append the structure to
       the wtmp file.

FILES
       /var/log/wtmp
	      database of past user logins

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬──────────────────────────┐
       │ Interface												  │ Attribute	  │ Value		     │
       ├──────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼──────────────────────────┤
       │ updwtmp(), logwtmp()											  │ Thread safety │ MT-Unsafe sig:ALRM timer │
       └──────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴──────────────────────────┘

VERSIONS
       For consistency with the other "utmpx" functions (see getutxent(3)), glibc provides (since glibc 2.1):

	   #define _GNU_SOURCE		/* See feature_test_macros(7) */
	   #include <utmpx.h>
	   void updwtmpx (const char *wtmpx_file, const struct utmpx *utx);

       This function performs the same task as updwtmp(), but differs in that it takes a utmpx structure as its last argument.

STANDARDS
       None.

HISTORY
       Solaris, NetBSD.

SEE ALSO
       getutxent(3), wtmp(5)

Linux man-pages 6.7							  2023-10-31								    updwtmp(3)
