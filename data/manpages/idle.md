idle(2)								      System Calls Manual							       idle(2)

NAME
       idle - make process 0 idle

SYNOPSIS
       #include <unistd.h>

       [[deprecated]] int idle(void);

DESCRIPTION
       idle()  is an internal system call used during bootstrap.  It marks the process's pages as swappable, lowers its priority, and enters the main schedul‐
       ing loop.  idle() never returns.

       Only process 0 may call idle().	Any user process, even a process with superuser permission, will receive EPERM.

RETURN VALUE
       idle() never returns for process 0, and always returns -1 for a user process.

ERRORS
       EPERM  Always, for a user process.

STANDARDS
       Linux.

HISTORY
       Removed in Linux 2.3.13.

Linux man-pages 6.7							  2023-10-31								       idle(2)
