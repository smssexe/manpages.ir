fenv_t(3type)																	 fenv_t(3type)

NAME
       fenv_t, fexcept_t - floating-point environment

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <fenv.h>

       typedef /* ... */ fenv_t;
       typedef /* ... */ fexcept_t;

DESCRIPTION
       fenv_t represents the entire floating-point environment, including control modes and status flags.

       fexcept_t represents the floating-point status flags collectively.

       For further details see fenv(3).

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C99, POSIX.1-2001.

SEE ALSO
       fenv(3)

Linux man-pages 6.7							  2023-10-31								 fenv_t(3type)
