getdirentries(3)						   Library Functions Manual						      getdirentries(3)

NAME
       getdirentries - get directory entries in a filesystem-independent format

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <dirent.h>

       ssize_t getdirentries(int fd, char buf[restrict .nbytes], size_t nbytes,
			     off_t *restrict basep);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       getdirentries():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       Read  directory	entries from the directory specified by fd into buf.  At most nbytes are read.	Reading starts at offset *basep, and *basep is updated
       with the new position after reading.

RETURN VALUE
       getdirentries() returns the number of bytes read or zero when at the end of the directory.  If an error occurs, -1 is returned, and errno is set to in‐
       dicate the error.

ERRORS
       See the Linux library source code for details.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ getdirentries()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       BSD.

NOTES
       Use opendir(3) and readdir(3) instead.

SEE ALSO
       lseek(2), open(2)

Linux man-pages 6.7							  2023-10-31							      getdirentries(3)
