pthread_equal(3)						   Library Functions Manual						      pthread_equal(3)

NAME
       pthread_equal - compare thread IDs

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       int pthread_equal(pthread_t t1, pthread_t t2);

DESCRIPTION
       The pthread_equal() function compares two thread identifiers.

RETURN VALUE
       If the two thread IDs are equal, pthread_equal() returns a nonzero value; otherwise, it returns 0.

ERRORS
       This function always succeeds.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ pthread_equal()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The pthread_equal() function is necessary because thread IDs should be considered opaque: there is no portable way for applications to directly compare
       two pthread_t values.

SEE ALSO
       pthread_create(3), pthread_self(3), pthreads(7)

Linux man-pages 6.7							  2023-10-31							      pthread_equal(3)
