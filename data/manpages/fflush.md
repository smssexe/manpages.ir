fflush(3)							   Library Functions Manual							     fflush(3)

NAME
       fflush - flush a stream

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>

       int fflush(FILE *_Nullable stream);

DESCRIPTION
       For  output  streams,  fflush()	forces a write of all user-space buffered data for the given output or update stream via the stream's underlying write
       function.

       For input streams associated with seekable files (e.g., disk files, but not pipes or terminals), fflush() discards any  buffered	 data  that  has  been
       fetched from the underlying file, but has not been consumed by the application.

       The open status of the stream is unaffected.

       If the stream argument is NULL, fflush() flushes all open output streams.

       For a nonlocking counterpart, see unlocked_stdio(3).

RETURN VALUE
       Upon successful completion 0 is returned.  Otherwise, EOF is returned and errno is set to indicate the error.

ERRORS
       EBADF  stream is not an open stream, or is not open for writing.

       The function fflush() may also fail and set errno for any of the errors specified for write(2).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ fflush()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001, POSIX.1-2008.

       POSIX.1-2001 did not specify the behavior for flushing of input streams, but the behavior is specified in POSIX.1-2008.

NOTES
       Note  that  fflush()  flushes  only  the user-space buffers provided by the C library.  To ensure that the data is physically stored on disk the kernel
       buffers must be flushed too, for example, with sync(2) or fsync(2).

SEE ALSO
       fsync(2), sync(2), write(2), fclose(3), fileno(3), fopen(3), fpurge(3), setbuf(3), unlocked_stdio(3)

Linux man-pages 6.7							  2023-10-31								     fflush(3)
