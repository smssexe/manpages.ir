raise(3)							   Library Functions Manual							      raise(3)

NAME
       raise - send a signal to the caller

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <signal.h>

       int raise(int sig);

DESCRIPTION
       The raise() function sends a signal to the calling process or thread.  In a single-threaded program it is equivalent to

	   kill(getpid(), sig);

       In a multithreaded program it is equivalent to

	   pthread_kill(pthread_self(), sig);

       If the signal causes a handler to be called, raise() will return only after the signal handler has returned.

RETURN VALUE
       raise() returns 0 on success, and nonzero for failure.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ raise()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       POSIX.1-2001, C89.

       Since  glibc 2.3.3, raise() is implemented by calling tgkill(2), if the kernel supports that system call.  Older glibc versions implemented raise() us‐
       ing kill(2).

SEE ALSO
       getpid(2), kill(2), sigaction(2), signal(2), pthread_kill(3), signal(7)

Linux man-pages 6.7							  2023-10-31								      raise(3)
