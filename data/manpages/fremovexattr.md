removexattr(2)							      System Calls Manual							removexattr(2)

NAME
       removexattr, lremovexattr, fremovexattr - remove an extended attribute

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/xattr.h>

       int removexattr(const char *path, const char *name);
       int lremovexattr(const char *path, const char *name);
       int fremovexattr(int fd, const char *name);

DESCRIPTION
       Extended	 attributes are name:value pairs associated with inodes (files, directories, symbolic links, etc.).  They are extensions to the normal attrib‐
       utes which are associated with all inodes in the system (i.e., the stat(2) data).  A complete overview of extended attributes concepts can be found  in
       xattr(7).

       removexattr() removes the extended attribute identified by name and associated with the given path in the filesystem.

       lremovexattr()  is identical to removexattr(), except in the case of a symbolic link, where the extended attribute is removed from the link itself, not
       the file that it refers to.

       fremovexattr() is identical to removexattr(), only the extended attribute is removed from the open file referred to by fd (as returned by  open(2))  in
       place of path.

       An  extended  attribute	name  is a null-terminated string.  The name includes a namespace prefix; there may be several, disjoint namespaces associated
       with an individual inode.

RETURN VALUE
       On success, zero is returned.  On failure, -1 is returned and errno is set to indicate the error.

ERRORS
       ENODATA
	      The named attribute does not exist.

       ENOTSUP
	      Extended attributes are not supported by the filesystem, or are disabled.

       In addition, the errors documented in stat(2) can also occur.

STANDARDS
       Linux.

HISTORY
       Linux 2.4, glibc 2.3.

SEE ALSO
       getfattr(1), setfattr(1), getxattr(2), listxattr(2), open(2), setxattr(2), stat(2), symlink(7), xattr(7)

Linux man-pages 6.7							  2023-10-31								removexattr(2)
