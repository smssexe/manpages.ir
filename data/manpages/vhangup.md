vhangup(2)							      System Calls Manual							    vhangup(2)

NAME
       vhangup - virtually hangup the current terminal

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       int vhangup(void);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       vhangup():
	   Since glibc 2.21:
	       _DEFAULT_SOURCE
	   In glibc 2.19 and 2.20:
	       _DEFAULT_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)
	   Up to and including glibc 2.19:
	       _BSD_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)

DESCRIPTION
       vhangup() simulates a hangup on the current terminal.  This call arranges for other users to have a “clean” terminal at login time.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EPERM  The calling process has insufficient privilege to call vhangup(); the CAP_SYS_TTY_CONFIG capability is required.

STANDARDS
       Linux.

SEE ALSO
       init(1), capabilities(7)

Linux man-pages 6.7							  2023-10-31								    vhangup(2)
