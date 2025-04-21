pthread_attr_setschedparam(3)					   Library Functions Manual					 pthread_attr_setschedparam(3)

NAME
       pthread_attr_setschedparam, pthread_attr_getschedparam - set/get scheduling parameter attributes in thread attributes object

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       int pthread_attr_setschedparam(pthread_attr_t *restrict attr,
				     const struct sched_param *restrict param);
       int pthread_attr_getschedparam(const pthread_attr_t *restrict attr,
				     struct sched_param *restrict param);

DESCRIPTION
       The  pthread_attr_setschedparam()  function  sets the scheduling parameter attributes of the thread attributes object referred to by attr to the values
       specified in the buffer pointed to by param.  These attributes determine the scheduling parameters of a thread created using the thread attributes  ob‐
       ject attr.

       The pthread_attr_getschedparam() returns the scheduling parameter attributes of the thread attributes object attr in the buffer pointed to by param.

       Scheduling parameters are maintained in the following structure:

	   struct sched_param {
	       int sched_priority;     /* Scheduling priority */
	   };

       As  can	be seen, only one scheduling parameter is supported.  For details of the permitted ranges for scheduling priorities in each scheduling policy,
       see sched(7).

       In order for the parameter setting  made	 by  pthread_attr_setschedparam()  to  have  effect  when  calling  pthread_create(3),	the  caller  must  use
       pthread_attr_setinheritsched(3) to set the inherit-scheduler attribute of the attributes object attr to PTHREAD_EXPLICIT_SCHED.

RETURN VALUE
       On success, these functions return 0; on error, they return a nonzero error number.

ERRORS
       pthread_attr_setschedparam() can fail with the following error:

       EINVAL The priority specified in param does not make sense for the current scheduling policy of attr.

       POSIX.1	also documents an ENOTSUP error for pthread_attr_setschedparam().  This value is never returned on Linux (but portable and future-proof appli‐
       cations should nevertheless handle this error return value).

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ pthread_attr_setschedparam(), pthread_attr_getschedparam()								   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.  glibc 2.0.

NOTES
       See pthread_attr_setschedpolicy(3) for a list of the thread scheduling policies supported on Linux.

EXAMPLES
       See pthread_setschedparam(3).

SEE ALSO
       sched_get_priority_min(2), pthread_attr_init(3), pthread_attr_setinheritsched(3), pthread_attr_setschedpolicy(3), pthread_create(3),
       pthread_setschedparam(3), pthread_setschedprio(3), pthreads(7), sched(7)

Linux man-pages 6.7							  2023-10-31						 pthread_attr_setschedparam(3)
