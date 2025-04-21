pthread_kill_other_threads_np(3)				   Library Functions Manual				      pthread_kill_other_threads_np(3)

NAME
       pthread_kill_other_threads_np - terminate all other threads in process

LIBRARY
       POSIX threads library (libpthread, -lpthread)

SYNOPSIS
       #include <pthread.h>

       void pthread_kill_other_threads_np(void);

DESCRIPTION
       pthread_kill_other_threads_np()	has an effect only in the LinuxThreads threading implementation.  On that implementation, calling this function causes
       the immediate termination of all threads in the application, except the calling thread.	The cancelation state and cancelation type of the to-be-termi‐
       nated threads are ignored, and the cleanup handlers are not called in those threads.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ pthread_kill_other_threads_np()											   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

VERSIONS
       In the NPTL threading implementation, pthread_kill_other_threads_np() exists, but does nothing.	(Nothing needs to be done, because the	implementation
       does the right thing during an execve(2).)

STANDARDS
       GNU; hence the suffix "_np" (nonportable) in the name.

HISTORY
       glibc 2.0

NOTES
       pthread_kill_other_threads_np()	is intended to be called just before a thread calls execve(2) or a similar function.  This function is designed to ad‐
       dress a limitation in the obsolete LinuxThreads implementation whereby the other threads	 of  an	 application  are  not	automatically  terminated  (as
       POSIX.1-2001 requires) during execve(2).

SEE ALSO
       execve(2), pthread_cancel(3), pthread_setcancelstate(3), pthread_setcanceltype(3), pthreads(7)

Linux man-pages 6.7							  2023-10-31					      pthread_kill_other_threads_np(3)
