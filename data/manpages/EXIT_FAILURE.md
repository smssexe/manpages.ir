EXIT_SUCCESS(3const)															  EXIT_SUCCESS(3const)

NAME
       EXIT_SUCCESS, EXIT_FAILURE - termination status constants

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stdlib.h>

       #define EXIT_SUCCESS  0
       #define EXIT_FAILURE  /* nonzero */

DESCRIPTION
       EXIT_SUCCESS and EXIT_FAILURE represent a successful and unsuccessful exit status respectively, and can be used as arguments to the exit(3) function.

CONFORMING TO
       C99 and later; POSIX.1-2001 and later.

EXAMPLES
       #include <stdio.h>
       #include <stdlib.h>

       int
       main(int argc, char *argv[])
       {
	   FILE *fp;

	   if (argc != 2) {
	       fprintf(stderr, "Usage: %s <file>\n", argv[0]);
	       exit(EXIT_FAILURE);
	   }

	   fp = fopen(argv[1], "r");
	   if (fp == NULL) {
	       perror(argv[1]);
	       exit(EXIT_FAILURE);
	   }

	   /* Other code omitted */

	   fclose(fp);
	   exit(EXIT_SUCCESS);
       }

SEE ALSO
       exit(3), sysexits.h(3head)

Linux man-pages 6.7							  2023-10-31							  EXIT_SUCCESS(3const)
