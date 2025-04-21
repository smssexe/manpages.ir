fileno(3)							   Library Functions Manual							     fileno(3)

NAME
       fileno - obtain file descriptor of a stdio stream

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>

       int fileno(FILE *stream);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       fileno():
	   _POSIX_C_SOURCE

DESCRIPTION
       The function fileno() examines the argument stream and returns the integer file descriptor used to implement this stream.  The file descriptor is still
       owned by stream and will be closed when fclose(3) is called.  Duplicate the file descriptor with dup(2) before passing it to code that might close it.

       For the nonlocking counterpart, see unlocked_stdio(3).

RETURN VALUE
       On success, fileno() returns the file descriptor associated with stream.	 On failure, -1 is returned and errno is set to indicate the error.

ERRORS
       EBADF  stream is not associated with a file.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ fileno()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       open(2), fdopen(3), stdio(3), unlocked_stdio(3)

Linux man-pages 6.7							  2023-10-31								     fileno(3)
