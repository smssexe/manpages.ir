fgetpwent(3)							   Library Functions Manual							  fgetpwent(3)

NAME
       fgetpwent - get password file entry

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>
       #include <sys/types.h>
       #include <pwd.h>

       struct passwd *fgetpwent(FILE *stream);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       fgetpwent():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _SVID_SOURCE

DESCRIPTION
       The  fgetpwent()	 function returns a pointer to a structure containing the broken out fields of a line in the file stream.  The first time it is called
       it returns the first entry; thereafter, it returns successive entries.  The file referred to by stream must have the same format	 as  /etc/passwd  (see
       passwd(5)).

       The passwd structure is defined in <pwd.h> as follows:

	   struct passwd {
	       char   *pw_name;	      /* username */
	       char   *pw_passwd;     /* user password */
	       uid_t   pw_uid;	      /* user ID */
	       gid_t   pw_gid;	      /* group ID */
	       char   *pw_gecos;      /* real name */
	       char   *pw_dir;	      /* home directory */
	       char   *pw_shell;      /* shell program */
	   };

RETURN VALUE
       The  fgetpwent()	 function returns a pointer to a passwd structure, or NULL if there are no more entries or an error occurs.  In the event of an error,
       errno is set to indicate the error.

ERRORS
       ENOMEM Insufficient memory to allocate passwd structure.

FILES
       /etc/passwd
	      password database file

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬──────────────────────────┐
       │ Interface												  │ Attribute	  │ Value		     │
       ├──────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼──────────────────────────┤
       │ fgetpwent()												  │ Thread safety │ MT-Unsafe race:fgetpwent │
       └──────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴──────────────────────────┘

STANDARDS
       None.

HISTORY
       SVr4.

SEE ALSO
       endpwent(3), fgetpwent_r(3), fopen(3), getpw(3), getpwent(3), getpwnam(3), getpwuid(3), putpwent(3), setpwent(3), passwd(5)

Linux man-pages 6.7							  2023-10-31								  fgetpwent(3)
