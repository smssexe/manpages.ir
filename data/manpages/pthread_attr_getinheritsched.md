pthread_attr_setinheritsched(3)					   Library Functions Manual				       pthread_attr_setinheritsched(3)

NAME
       pthread_attr_setinheritsched, pthread_attr_getinheritsched - set/get inherit-scheduler attribute in thread attributes object

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       int pthread_attr_setinheritsched(pthread_attr_t *attr,
					int inheritsched);
       int pthread_attr_getinheritsched(const pthread_attr_t *restrict attr,
					int *restrict inheritsched);

DESCRIPTION
       The pthread_attr_setinheritsched() function sets the inherit-scheduler attribute of the thread attributes object referred to by attr to the value spec‐
       ified  in  inheritsched.	  The inherit-scheduler attribute determines whether a thread created using the thread attributes object attr will inherit its
       scheduling attributes from the calling thread or whether it will take them from attr.

       The following scheduling attributes are affected by the inherit-scheduler attribute:  scheduling	 policy	 (pthread_attr_setschedpolicy(3)),  scheduling
       priority (pthread_attr_setschedparam(3)), and contention scope (pthread_attr_setscope(3)).

       The following values may be specified in inheritsched:

       PTHREAD_INHERIT_SCHED
	      Threads that are created using attr inherit scheduling attributes from the creating thread; the scheduling attributes in attr are ignored.

       PTHREAD_EXPLICIT_SCHED
	      Threads that are created using attr take their scheduling attributes from the values specified by the attributes object.

       The default setting of the inherit-scheduler attribute in a newly initialized thread attributes object is PTHREAD_INHERIT_SCHED.

       The  pthread_attr_getinheritsched()  returns  the  inherit-scheduler  attribute of the thread attributes object attr in the buffer pointed to by inher‐
       itsched.

RETURN VALUE
       On success, these functions return 0; on error, they return a nonzero error number.

ERRORS
       pthread_attr_setinheritsched() can fail with the following error:

       EINVAL Invalid value in inheritsched.

       POSIX.1 also documents an optional ENOTSUP error ("attempt was made to set the attribute to an unsupported value") for pthread_attr_setinheritsched().

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ pthread_attr_setinheritsched(), pthread_attr_getinheritsched()								   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.0.  POSIX.1-2001.

BUGS
       As at glibc 2.8, if a thread attributes object is initialized using pthread_attr_init(3), then the scheduling policy of the attributes object is set to
       SCHED_OTHER and the scheduling priority is set to 0.  However, if the inherit-scheduler attribute is then set to PTHREAD_EXPLICIT_SCHED, then a	thread
       created using the attribute object wrongly inherits its scheduling attributes from the creating thread.	This bug does not occur if either the schedul‐
       ing policy or scheduling priority attribute is explicitly set in the thread attributes object before calling pthread_create(3).

EXAMPLES
       See pthread_setschedparam(3).

SEE ALSO
       pthread_attr_init(3), pthread_attr_setschedparam(3), pthread_attr_setschedpolicy(3), pthread_attr_setscope(3), pthread_create(3),
       pthread_setschedparam(3), pthread_setschedprio(3), pthreads(7), sched(7)

Linux man-pages 6.7							  2023-10-31					       pthread_attr_setinheritsched(3)
