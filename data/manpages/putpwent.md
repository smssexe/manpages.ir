putpwent(3)							   Library Functions Manual							   putpwent(3)

NAME
       putpwent - write a password file entry

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>
       #include <sys/types.h>
       #include <pwd.h>

       int putpwent(const struct passwd *restrict p, FILE *restrict stream);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       putpwent():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _SVID_SOURCE

DESCRIPTION
       The putpwent() function writes a password entry from the structure p in the file associated with stream.

       The passwd structure is defined in <pwd.h> as follows:

	   struct passwd {
	       char    *pw_name;	/* username */
	       char    *pw_passwd;	/* user password */
	       uid_t	pw_uid;		/* user ID */
	       gid_t	pw_gid;		/* group ID */
	       char    *pw_gecos;	/* real name */
	       char    *pw_dir;		/* home directory */
	       char    *pw_shell;	/* shell program */
	   };

RETURN VALUE
       The putpwent() function returns 0 on success.  On failure, it returns -1, and errno is set to indicate the error.

ERRORS
       EINVAL Invalid (NULL) argument given.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ putpwent()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       None.

HISTORY
       SVr4.

SEE ALSO
       endpwent(3), fgetpwent(3), getpw(3), getpwent(3), getpwnam(3), getpwuid(3), setpwent(3)

Linux man-pages 6.7							  2023-10-31								   putpwent(3)
