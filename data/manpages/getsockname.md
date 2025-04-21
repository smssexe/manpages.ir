getsockname(2)							      System Calls Manual							getsockname(2)

NAME
       getsockname - get socket name

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/socket.h>

       int getsockname(int sockfd, struct sockaddr *restrict addr,
		       socklen_t *restrict addrlen);

DESCRIPTION
       getsockname()  returns  the current address to which the socket sockfd is bound, in the buffer pointed to by addr.  The addrlen argument should be ini‐
       tialized to indicate the amount of space (in bytes) pointed to by addr.	On return it contains the actual size of the socket address.

       The returned address is truncated if the buffer provided is too small; in this case, addrlen will return a value greater than was supplied to the call.

RETURN VALUE
       On success, zero is returned.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EBADF  The argument sockfd is not a valid file descriptor.

       EFAULT The addr argument points to memory not in a valid part of the process address space.

       EINVAL addrlen is invalid (e.g., is negative).

       ENOBUFS
	      Insufficient resources were available in the system to perform the operation.

       ENOTSOCK
	      The file descriptor sockfd does not refer to a socket.

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001, SVr4, 4.4BSD (first appeared in 4.2BSD).

SEE ALSO
       bind(2), socket(2), getifaddrs(3), ip(7), socket(7), unix(7)

Linux man-pages 6.7							  2023-10-31								getsockname(2)
