socketcall(2)							      System Calls Manual							 socketcall(2)

NAME
       socketcall - socket system calls

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <linux/net.h>	     /* Definition of SYS_* constants */
       #include <sys/syscall.h>	     /* Definition of SYS_socketcall */
       #include <unistd.h>

       int syscall(SYS_socketcall, int call, unsigned long *args);

       Note: glibc provides no wrapper for socketcall(), necessitating the use of syscall(2).

DESCRIPTION
       socketcall() is a common kernel entry point for the socket system calls.	 call determines which socket function to invoke.  args points to a block con‐
       taining the actual arguments, which are passed through to the appropriate call.

       User  programs  should  call  the appropriate functions by their usual names.  Only standard library implementors and kernel hackers need to know about
       socketcall().

       call		 Man page
       SYS_SOCKET	 socket(2)
       SYS_BIND		 bind(2)
       SYS_CONNECT	 connect(2)
       SYS_LISTEN	 listen(2)
       SYS_ACCEPT	 accept(2)
       SYS_GETSOCKNAME	 getsockname(2)
       SYS_GETPEERNAME	 getpeername(2)
       SYS_SOCKETPAIR	 socketpair(2)
       SYS_SEND		 send(2)
       SYS_RECV		 recv(2)
       SYS_SENDTO	 sendto(2)
       SYS_RECVFROM	 recvfrom(2)
       SYS_SHUTDOWN	 shutdown(2)
       SYS_SETSOCKOPT	 setsockopt(2)
       SYS_GETSOCKOPT	 getsockopt(2)
       SYS_SENDMSG	 sendmsg(2)
       SYS_RECVMSG	 recvmsg(2)
       SYS_ACCEPT4	 accept4(2)
       SYS_RECVMMSG	 recvmmsg(2)
       SYS_SENDMMSG	 sendmmsg(2)

VERSIONS
       On some architectures—for example, x86-64 and ARM—there is no socketcall() system call; instead socket(2), accept(2), bind(2), and so on really are im‐
       plemented as separate system calls.

STANDARDS
       Linux.

       On x86-32, socketcall() was historically the only entry point for the sockets API.  However, starting in Linux 4.3, direct system calls are provided on
       x86-32 for the sockets API.  This facilitates the creation of seccomp(2) filters that filter sockets system calls (for new user-space binaries that are
       compiled to use the new entry points) and also provides a (very) small performance improvement.

SEE ALSO
       accept(2), bind(2), connect(2), getpeername(2), getsockname(2),	getsockopt(2),	listen(2),  recv(2),  recvfrom(2),  recvmsg(2),	 send(2),  sendmsg(2),
       sendto(2), setsockopt(2), shutdown(2), socket(2), socketpair(2)

Linux man-pages 6.7							  2023-10-31								 socketcall(2)
