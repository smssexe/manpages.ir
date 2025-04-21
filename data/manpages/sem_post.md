sem_post(3)							   Library Functions Manual							   sem_post(3)

NAME
       sem_post - unlock a semaphore

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <semaphore.h>

       int sem_post(sem_t *sem);

DESCRIPTION
       sem_post() increments (unlocks) the semaphore pointed to by sem.	 If the semaphore's value consequently becomes greater than zero, then another process
       or thread blocked in a sem_wait(3) call will be woken up and proceed to lock the semaphore.

RETURN VALUE
       sem_post() returns 0 on success; on error, the value of the semaphore is left unchanged, -1 is returned, and errno is set to indicate the error.

ERRORS
       EINVAL sem is not a valid semaphore.

       EOVERFLOW
	      The maximum allowable value for a semaphore would be exceeded.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ sem_post()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       sem_post() is async-signal-safe: it may be safely called within a signal handler.

EXAMPLES
       See sem_wait(3) and shm_open(3).

SEE ALSO
       sem_getvalue(3), sem_wait(3), sem_overview(7), signal-safety(7)

Linux man-pages 6.7							  2023-10-31								   sem_post(3)
