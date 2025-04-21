dev_t(3type)																	  dev_t(3type)

NAME
       dev_t - device ID

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */  dev_t;

DESCRIPTION
       Used for device IDs.  It is an integer type.  For further details of this type, see makedev(3).

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following header also provides this type: <sys/stat.h>.

SEE ALSO
       mknod(2), stat(3type)

Linux man-pages 6.7							  2023-10-31								  dev_t(3type)
