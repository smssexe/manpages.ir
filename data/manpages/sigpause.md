sigpause(3)							   Library Functions Manual							   sigpause(3)

NAME
       sigpause - atomically release blocked signals and wait for interrupt

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <signal.h>

       [[deprecated]] int sigpause(int sigmask);  /* BSD (but see NOTES) */

       [[deprecated]] int sigpause(int sig);	  /* POSIX.1 / SysV / UNIX 95 */

DESCRIPTION
       Don't use this function.	 Use sigsuspend(2) instead.

       The  function sigpause() is designed to wait for some signal.  It changes the process's signal mask (set of blocked signals), and then waits for a sig‐
       nal to arrive.  Upon arrival of a signal, the original signal mask is restored.

RETURN VALUE
       If sigpause() returns, it was interrupted by a signal and the return value is -1 with errno set to EINTR.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ sigpause()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

VERSIONS
       On Linux, this routine is a system call only on the Sparc (sparc64) architecture.

       glibc uses the BSD version if the _BSD_SOURCE feature test macro is defined and none of _POSIX_SOURCE, _POSIX_C_SOURCE, _XOPEN_SOURCE, _GNU_SOURCE,  or
       _SVID_SOURCE is defined.	 Otherwise, the System V version is used, and feature test macros must be defined as follows to obtain the declaration:

       •  Since glibc 2.26: _XOPEN_SOURCE >= 500

       •  glibc 2.25 and earlier: _XOPEN_SOURCE

       Since  glibc 2.19, only the System V version is exposed by <signal.h>; applications that formerly used the BSD sigpause() should be amended to use sig‐
       suspend(2).

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.  Obsoleted in POSIX.1-2008.

       The classical BSD version of this function appeared in 4.2BSD.  It sets the process's signal mask to sigmask.  UNIX 95  standardized  the  incompatible
       System  V version of this function, which removes only the specified signal sig from the process's signal mask.	The unfortunate situation with two in‐
       compatible functions with the same name was solved by the sigsuspend(2) function, that takes a sigset_t * argument (instead of an int).

SEE ALSO
       kill(2), sigaction(2), sigprocmask(2), sigsuspend(2), sigblock(3), sigvec(3), feature_test_macros(7)

Linux man-pages 6.7							  2023-10-31								   sigpause(3)
