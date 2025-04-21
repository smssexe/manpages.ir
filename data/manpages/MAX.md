MAX(3)								   Library Functions Manual								MAX(3)

NAME
       MAX, MIN - maximum or minimum of two values

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/param.h>

       MAX(a, b);
       MIN(a, b);

DESCRIPTION
       These macros return the maximum or minimum of a and b.

RETURN VALUE
       These macros return the value of one of their arguments, possibly converted to a different type (see BUGS).

ERRORS
       These macros may raise the "invalid" floating-point exception when any of the arguments is NaN.

STANDARDS
       GNU, BSD.

NOTES
       If either of the arguments is of a floating-point type, you might prefer to use fmax(3) or fmin(3), which can handle NaN.

       The arguments may be evaluated more than once, or not at all.

       Some UNIX systems might provide these macros in a different header, or not at all.

BUGS
       Due  to	the  usual  arithmetic conversions, the result of these macros may be very different from either of the arguments.  To avoid this, ensure that
       both arguments have the same type.

EXAMPLES
       #include <stdio.h>
       #include <stdlib.h>
       #include <sys/param.h>

       int
       main(int argc, char *argv[])
       {
	   int a, b, x;

	   if (argc != 3) {
	       fprintf(stderr, "Usage: %s <num> <num>\n", argv[0]);
	       exit(EXIT_FAILURE);
	   }

	   a = atoi(argv[1]);
	   b = atoi(argv[2]);
	   x = MAX(a, b);
	   printf("MAX(%d, %d) is %d\n", a, b, x);

	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       fmax(3), fmin(3)

Linux man-pages 6.7							  2023-10-31									MAX(3)
