sched_yield(2)							      System Calls Manual							sched_yield(2)

NAME
       sched_yield - yield the processor

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sched.h>

       int sched_yield(void);

DESCRIPTION
       sched_yield()  causes  the  calling thread to relinquish the CPU.  The thread is moved to the end of the queue for its static priority and a new thread
       gets to run.

RETURN VALUE
       On success, sched_yield() returns 0.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       In the Linux implementation, sched_yield() always succeeds.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001 (but optional).  POSIX.1-2008.

       Before POSIX.1-2008, systems on which sched_yield() is available defined _POSIX_PRIORITY_SCHEDULING in <unistd.h>.

CAVEATS
       sched_yield() is intended for use with real-time scheduling policies (i.e., SCHED_FIFO or SCHED_RR).  Use of sched_yield() with nondeterministic sched‐
       uling policies such as SCHED_OTHER is unspecified and very likely means your application design is broken.

       If the calling thread is the only thread in the highest priority list at that time, it will continue to run after a call to sched_yield().

       Avoid calling sched_yield() unnecessarily or inappropriately (e.g., when resources needed by other schedulable threads are still held by	 the  caller),
       since doing so will result in unnecessary context switches, which will degrade system performance.

SEE ALSO
       sched(7)

Linux man-pages 6.7							  2023-10-31								sched_yield(2)
