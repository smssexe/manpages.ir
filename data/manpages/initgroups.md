initgroups(3)							   Library Functions Manual							 initgroups(3)

NAME
       initgroups - initialize the supplementary group access list

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/types.h>
       #include <grp.h>

       int initgroups(const char *user, gid_t group);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       initgroups():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _BSD_SOURCE

DESCRIPTION
       The  initgroups()  function  initializes the group access list by reading the group database /etc/group and using all groups of which user is a member.
       The additional group group is also added to the list.

       The user argument must be non-NULL.

RETURN VALUE
       The initgroups() function returns 0 on success.	On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       ENOMEM Insufficient memory to allocate group information structure.

       EPERM  The calling process has insufficient privilege.  See the underlying system call setgroups(2).

FILES
       /etc/group
	      group database file

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬────────────────┐
       │ Interface													    │ Attribute	    │ Value	     │
       ├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼────────────────┤
       │ initgroups()													    │ Thread safety │ MT-Safe locale │
       └────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴────────────────┘

STANDARDS
       None.

HISTORY
       SVr4, 4.3BSD.

SEE ALSO
       getgroups(2), setgroups(2), credentials(7)

Linux man-pages 6.7							  2023-10-31								 initgroups(3)
