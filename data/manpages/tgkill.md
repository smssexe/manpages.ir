tkill(2)							      System Calls Manual							      tkill(2)

NAME
       tkill, tgkill - send a signal to a thread

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <signal.h>	     /* Definition of SIG* constants */
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       [[deprecated]] int syscall(SYS_tkill, pid_t tid, int sig);

       #include <signal.h>

       int tgkill(pid_t tgid, pid_t tid, int sig);

       Note: glibc provides no wrapper for tkill(), necessitating the use of syscall(2).

DESCRIPTION
       tgkill()	 sends	the signal sig to the thread with the thread ID tid in the thread group tgid.  (By contrast, kill(2) can be used to send a signal only
       to a process (i.e., thread group) as a whole, and the signal will be delivered to an arbitrary thread within that process.)

       tkill() is an obsolete predecessor to tgkill().	It allows only the target thread ID to be specified, which may result in the wrong thread  being  sig‐
       naled if a thread terminates and its thread ID is recycled.  Avoid using this system call.

       These are the raw system call interfaces, meant for internal thread library use.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EAGAIN The RLIMIT_SIGPENDING resource limit was reached and sig is a real-time signal.

       EAGAIN Insufficient kernel memory was available and sig is a real-time signal.

       EINVAL An invalid thread ID, thread group ID, or signal was specified.

       EPERM  Permission denied.  For the required permissions, see kill(2).

       ESRCH  No process with the specified thread ID (and thread group ID) exists.

STANDARDS
       Linux.

HISTORY
       tkill()
	      Linux 2.4.19 / 2.5.4.

       tgkill()
	      Linux 2.5.75, glibc 2.30.

NOTES
       See the description of CLONE_THREAD in clone(2) for an explanation of thread groups.

SEE ALSO
       clone(2), gettid(2), kill(2), rt_sigqueueinfo(2)

Linux man-pages 6.7							  2023-10-31								      tkill(2)
