sem_close(3)							   Library Functions Manual							  sem_close(3)

NAME
       sem_close - close a named semaphore

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <semaphore.h>

       int sem_close(sem_t *sem);

DESCRIPTION
       sem_close()  closes  the named semaphore referred to by sem, allowing any resources that the system has allocated to the calling process for this sema‐
       phore to be freed.

RETURN VALUE
       On success sem_close() returns 0; on error, -1 is returned, with errno set to indicate the error.

ERRORS
       EINVAL sem is not a valid semaphore.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ sem_close()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       All open named semaphores are automatically closed on process termination, or upon execve(2).

SEE ALSO
       sem_getvalue(3), sem_open(3), sem_post(3), sem_unlink(3), sem_wait(3), sem_overview(7)

Linux man-pages 6.7							  2023-10-31								  sem_close(3)
