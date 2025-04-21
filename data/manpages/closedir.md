closedir(3)							   Library Functions Manual							   closedir(3)

NAME
       closedir - close a directory

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/types.h>
       #include <dirent.h>

       int closedir(DIR *dirp);

DESCRIPTION
       The  closedir()	function closes the directory stream associated with dirp.  A successful call to closedir() also closes the underlying file descriptor
       associated with dirp.  The directory stream descriptor dirp is not available after this call.

RETURN VALUE
       The closedir() function returns 0 on success.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EBADF  Invalid directory stream descriptor dirp.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ closedir()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.

SEE ALSO
       close(2), opendir(3), readdir(3), rewinddir(3), scandir(3), seekdir(3), telldir(3)

Linux man-pages 6.7							  2023-10-31								   closedir(3)
