ferror(3)							   Library Functions Manual							     ferror(3)

NAME
       clearerr, feof, ferror - check and reset stream status

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <stdio.h>

       void clearerr(FILE *stream);
       int feof(FILE *stream);
       int ferror(FILE *stream);

DESCRIPTION
       The function clearerr() clears the end-of-file and error indicators for the stream pointed to by stream.

       The function feof() tests the end-of-file indicator for the stream pointed to by stream, returning nonzero if it is set.	 The end-of-file indicator can
       be cleared only by the function clearerr().

       The  function ferror() tests the error indicator for the stream pointed to by stream, returning nonzero if it is set.  The error indicator can be reset
       only by the clearerr() function.

       For nonlocking counterparts, see unlocked_stdio(3).

RETURN VALUE
       The feof() function returns nonzero if the end-of-file indicator is set for stream; otherwise, it returns zero.

       The ferror() function returns nonzero if the error indicator is set for stream; otherwise, it returns zero.

ERRORS
       These functions should not fail and do not set errno.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ clearerr(), feof(), ferror()												   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       C11, POSIX.1-2008.

HISTORY
       C89, POSIX.1-2001.

NOTES
       POSIX.1-2008 specifies that these functions shall not change the value of errno if stream is valid.

CAVEATS
       Normally, programs should read the return value of an input function, such as fgetc(3), before using functions of the feof(3) family.   Only  when  the
       function returned the sentinel value EOF it makes sense to distinguish between the end of a file or an error with feof(3) or ferror(3).

SEE ALSO
       open(2), fdopen(3), fileno(3), stdio(3), unlocked_stdio(3)

Linux man-pages 6.7							  2023-10-31								     ferror(3)
