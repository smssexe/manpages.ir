sem_unlink(3)							   Library Functions Manual							 sem_unlink(3)

NAME
       sem_unlink - remove a named semaphore

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <semaphore.h>

       int sem_unlink(const char *name);

DESCRIPTION
       sem_unlink()  removes  the  named semaphore referred to by name.	 The semaphore name is removed immediately.  The semaphore is destroyed once all other
       processes that have the semaphore open close it.

RETURN VALUE
       On success sem_unlink() returns 0; on error, -1 is returned, with errno set to indicate the error.

ERRORS
       EACCES The caller does not have permission to unlink this semaphore.

       ENAMETOOLONG
	      name was too long.

       ENOENT There is no semaphore with the given name.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ sem_unlink()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       sem_getvalue(3), sem_open(3), sem_post(3), sem_wait(3), sem_overview(7)

Linux man-pages 6.7							  2023-10-31								 sem_unlink(3)
