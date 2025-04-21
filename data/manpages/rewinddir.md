rewinddir(3)							   Library Functions Manual							  rewinddir(3)

NAME
       rewinddir - reset directory stream

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/types.h>
       #include <dirent.h>

       void rewinddir(DIR *dirp);

DESCRIPTION
       The rewinddir() function resets the position of the directory stream dirp to the beginning of the directory.

RETURN VALUE
       The rewinddir() function returns no value.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ rewinddir()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.

SEE ALSO
       closedir(3), opendir(3), readdir(3), scandir(3), seekdir(3), telldir(3)

Linux man-pages 6.7							  2023-10-31								  rewinddir(3)
