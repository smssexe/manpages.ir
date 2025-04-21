pthread_testcancel(3)						   Library Functions Manual						 pthread_testcancel(3)

NAME
       pthread_testcancel - request delivery of any pending cancelation request

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       void pthread_testcancel(void);

DESCRIPTION
       Calling	pthread_testcancel() creates a cancelation point within the calling thread, so that a thread that is otherwise executing code that contains no
       cancelation points will respond to a cancelation request.

       If cancelability is disabled (using pthread_setcancelstate(3)), or no cancelation request is pending, then a call to pthread_testcancel()  has  no  ef‐
       fect.

RETURN VALUE
       This  function  does not return a value.	 If the calling thread is canceled as a consequence of a call to this function, then the function does not re‐
       turn.

ERRORS
       This function always succeeds.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ pthread_testcancel()													   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.0.  POSIX.1-2001.

EXAMPLES
       See pthread_cleanup_push(3).

SEE ALSO
       pthread_cancel(3), pthread_cleanup_push(3), pthread_setcancelstate(3), pthreads(7)

Linux man-pages 6.7							  2023-10-31							 pthread_testcancel(3)
