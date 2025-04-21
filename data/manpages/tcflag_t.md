cc_t(3type)																	   cc_t(3type)

NAME
       cc_t, speed_t, tcflag_t - terminal special characters, baud rates, modes

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <termios.h>

       typedef /* ... */ cc_t;
       typedef /* ... */ speed_t;
       typedef /* ... */ tcflag_t;

DESCRIPTION
       cc_t is used for terminal special characters, speed_t for baud rates, and tcflag_t for modes.

       All are unsigned integer types.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       termios(3)

Linux man-pages 6.7							  2023-10-31								   cc_t(3type)
