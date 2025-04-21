ipc(2)								      System Calls Manual								ipc(2)

NAME
       ipc - System V IPC system calls

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <linux/ipc.h>	     /* Definition of needed constants */
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_ipc, unsigned int call, int first,
		   unsigned long second, unsigned long third, void *ptr,
		   long fifth);

       Note: glibc provides no wrapper for ipc(), necessitating the use of syscall(2).

DESCRIPTION
       ipc() is a common kernel entry point for the System V IPC calls for messages, semaphores, and shared memory.  call determines which IPC function to in‐
       voke; the other arguments are passed through to the appropriate call.

       User-space  programs  should  call  the appropriate functions by their usual names.  Only standard library implementors and kernel hackers need to know
       about ipc().

VERSIONS
       On some architectures—for example x86-64 and ARM—there is no ipc() system call; instead, msgctl(2), semctl(2), shmctl(2), and so on really  are	imple‐
       mented as separate system calls.

STANDARDS
       Linux.

SEE ALSO
       msgctl(2), msgget(2), msgrcv(2), msgsnd(2), semctl(2), semget(2), semop(2), semtimedop(2), shmat(2), shmctl(2), shmdt(2), shmget(2), sysvipc(7)

Linux man-pages 6.7							  2023-10-31									ipc(2)
