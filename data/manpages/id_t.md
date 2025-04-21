id_t(3type)																	   id_t(3type)

NAME
       pid_t, uid_t, gid_t, id_t - process/user/group identifier

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */ pid_t;
       typedef /* ... */ uid_t;
       typedef /* ... */ gid_t;
       typedef /* ... */ id_t;

DESCRIPTION
       pid_t is a type used for storing process IDs, process group IDs, and session IDs.  It is a signed integer type.

       uid_t is a type used to hold user IDs.  It is an integer type.

       gid_t is a type used to hold group IDs.	It is an integer type.

       id_t is a type used to hold a general identifier.  It is an integer type that can be used to contain a pid_t, uid_t, or gid_t.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The  following  headers	also  provide  pid_t:  <fcntl.h>,  <sched.h>,  <signal.h>,  <spawn.h>,	<sys/msg.h>,  <sys/sem.h>,  <sys/shm.h>, <sys/wait.h>,
       <termios.h>, <time.h>, <unistd.h>, and <utmpx.h>.

       The following headers also provide uid_t: <pwd.h>, <signal.h>, <stropts.h>, <sys/ipc.h>, <sys/stat.h>, and <unistd.h>.

       The following headers also provide gid_t: <grp.h>, <pwd.h>, <signal.h>, <stropts.h>, <sys/ipc.h>, <sys/stat.h>, and <unistd.h>.

       The following header also provides id_t: <sys/resource.h>.

SEE ALSO
       chown(2), fork(2), getegid(2), geteuid(2), getgid(2), getgroups(2), getpgid(2), getpid(2), getppid(2), getpriority(2), getpwnam(3),  getresgid(2),  ge‐
       tresuid(2), getsid(2), gettid(2), getuid(2), kill(2), pidfd_open(2), sched_setscheduler(2), waitid(2), getgrnam(3), sigqueue(3), credentials(7)

Linux man-pages 6.7							  2023-10-31								   id_t(3type)
