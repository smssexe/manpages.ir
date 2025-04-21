telldir(3)							   Library Functions Manual							    telldir(3)

NAME
       telldir - return current location in directory stream

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <dirent.h>

       long telldir(DIR *dirp);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       telldir():
	   _XOPEN_SOURCE
	      || /* glibc >= 2.19: */ _DEFAULT_SOURCE
	      || /* glibc <= 2.19: */ _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       The telldir() function returns the current location associated with the directory stream dirp.

RETURN VALUE
       On  success,  the  telldir() function returns the current location in the directory stream.  On error, -1 is returned, and errno is set to indicate the
       error.

ERRORS
       EBADF  Invalid directory stream descriptor dirp.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ telldir()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, 4.3BSD.

       Up to glibc 2.1.1, the return type of telldir() was off_t.  POSIX.1-2001 specifies long, and this is the type used since glibc 2.1.2.

       In early filesystems, the value returned by telldir() was a simple file offset within a directory.  Modern filesystems use  tree	 or  hash  structures,
       rather  than  flat  tables,  to	represent  directories.	 On such filesystems, the value returned by telldir() (and used internally by readdir(3)) is a
       "cookie" that is used by the implementation to derive a position within a directory.  Application programs should treat	this  strictly	as  an	opaque
       value, making no assumptions about its contents.

SEE ALSO
       closedir(3), opendir(3), readdir(3), rewinddir(3), scandir(3), seekdir(3)

Linux man-pages 6.7							  2023-10-31								    telldir(3)
