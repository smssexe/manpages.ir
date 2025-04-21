sem_getvalue(3)							   Library Functions Manual						       sem_getvalue(3)

NAME
       sem_getvalue - get the value of a semaphore

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <semaphore.h>

       int sem_getvalue(sem_t *restrict sem, int *restrict sval);

DESCRIPTION
       sem_getvalue() places the current value of the semaphore pointed to sem into the integer pointed to by sval.

       If  one	or  more  processes or threads are blocked waiting to lock the semaphore with sem_wait(3), POSIX.1 permits two possibilities for the value re‐
       turned in sval: either 0 is returned; or a negative number whose absolute value is the count of the number of processes and threads  currently  blocked
       in sem_wait(3).	Linux adopts the former behavior.

RETURN VALUE
       sem_getvalue() returns 0 on success; on error, -1 is returned and errno is set to indicate the error.

ERRORS
       EINVAL sem is not a valid semaphore.  (The glibc implementation currently does not check whether sem is valid.)

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ sem_getvalue()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The value of the semaphore may already have changed by the time sem_getvalue() returns.

SEE ALSO
       sem_post(3), sem_wait(3), sem_overview(7)

Linux man-pages 6.7							  2023-10-31							       sem_getvalue(3)
