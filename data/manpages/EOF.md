EOF(3const)																	   EOF(3const)

NAME
       EOF - end of file or error indicator

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdio.h>

       #define EOF  /* ... */

DESCRIPTION
       EOF represents the end of an input file, or an error indication.	 It is a negative value, of type int.

       EOF is not a character (it can't be represented by unsigned char).  It is instead a sentinel value outside of the valid range for valid characters.

CONFORMING TO
       C99 and later; POSIX.1-2001 and later.

CAVEATS
       Programs	 can't	pass this value to an output function to "write" the end of a file.  That would likely result in undefined behavior.  Instead, closing
       the writing stream or file descriptor that refers to such file is the way to signal the end of that file.

SEE ALSO
       feof(3), fgetc(3)

Linux man-pages 6.7							  2023-10-31								   EOF(3const)
