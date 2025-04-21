inotify_rm_watch(2)						      System Calls Manual						   inotify_rm_watch(2)

NAME
       inotify_rm_watch - remove an existing watch from an inotify instance

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/inotify.h>

       int inotify_rm_watch(int fd, int wd);

DESCRIPTION
       inotify_rm_watch() removes the watch associated with the watch descriptor wd from the inotify instance associated with the file descriptor fd.

       Removing a watch causes an IN_IGNORED event to be generated for this watch descriptor.  (See inotify(7).)

RETURN VALUE
       On success, inotify_rm_watch() returns zero.  On error, -1 is returned and errno is set to indicate the error.

ERRORS
       EBADF  fd is not a valid file descriptor.

       EINVAL The watch descriptor wd is not valid; or fd is not an inotify file descriptor.

STANDARDS
       Linux.

HISTORY
       Linux 2.6.13.

SEE ALSO
       inotify_add_watch(2), inotify_init(2), inotify(7)

Linux man-pages 6.7							  2023-10-31							   inotify_rm_watch(2)
