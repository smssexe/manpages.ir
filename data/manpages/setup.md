setup(2)							      System Calls Manual							      setup(2)

NAME
       setup - setup devices and filesystems, mount root filesystem

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       [[deprecated]] int setup(void);

DESCRIPTION
       setup()	is  called  once  from within linux/init/main.c.  It calls initialization functions for devices and filesystems configured into the kernel and
       then mounts the root filesystem.

       No user process may call setup().  Any user process, even a process with superuser permission, will receive EPERM.

RETURN VALUE
       setup() always returns -1 for a user process.

ERRORS
       EPERM  Always, for a user process.

STANDARDS
       Linux.

VERSIONS
       Removed in Linux 2.1.121.

       The calling sequence varied: at some times setup() has had a single argument void *BIOS and at other times a single argument int magic.

Linux man-pages 6.7							  2023-10-31								      setup(2)
