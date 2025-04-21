pause(2)							      System Calls Manual							      pause(2)

NAME
       pause - wait for signal

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       int pause(void);

DESCRIPTION
       pause()	causes	the  calling process (or thread) to sleep until a signal is delivered that either terminates the process or causes the invocation of a
       signal-catching function.

RETURN VALUE
       pause() returns only when a signal was caught and the signal-catching function returned.	 In this case, pause() returns -1, and errno is set to EINTR.

ERRORS
       EINTR  a signal was caught and the signal-catching function returned.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.3BSD.

SEE ALSO
       kill(2), select(2), signal(2), sigsuspend(2)

Linux man-pages 6.7							  2023-10-31								      pause(2)
