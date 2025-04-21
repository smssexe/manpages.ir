mode_t(3type)																	 mode_t(3type)

NAME
       mode_t - file attributes

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */ mode_t;

DESCRIPTION
       Used for some file attributes (e.g., file mode).	 It is an integer type.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following headers also provide this type: <fcntl.h>, <ndbm.h>, <spawn.h>, <sys/ipc.h>, <sys/mman.h>, and <sys/stat.h>.

SEE ALSO
       chmod(2), mkdir(2), open(2), umask(2), stat(3type)

Linux man-pages 6.7							  2023-10-31								 mode_t(3type)
