_llseek(2)							      System Calls Manual							    _llseek(2)

NAME
       _llseek - reposition read/write file offset

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS__llseek, unsigned int fd, unsigned long offset_high,
		   unsigned long offset_low, loff_t *result,
		   unsigned int whence);

       Note: glibc provides no wrapper for _llseek(), necessitating the use of syscall(2).

DESCRIPTION
       Note: for information about the llseek(3) library function, see lseek64(3).

       The _llseek() system call repositions the offset of the open file description associated with the file descriptor fd to the value

	      (offset_high << 32) | offset_low

       This new offset is a byte offset relative to the beginning of the file, the current file offset, or the end of the file, depending on whether whence is
       SEEK_SET, SEEK_CUR, or SEEK_END, respectively.

       The new file offset is returned in the argument result.	The  type loff_t is a 64-bit signed type.

       This system call exists on various 32-bit platforms to support seeking to large file offsets.

RETURN VALUE
       Upon successful completion, _llseek() returns 0.	 Otherwise, a value of -1 is returned and errno is set to indicate the error.

ERRORS
       EBADF  fd is not an open file descriptor.

       EFAULT Problem with copying results to user space.

       EINVAL whence is invalid.

VERSIONS
       You probably want to use the lseek(2) wrapper function instead.

STANDARDS
       Linux.

SEE ALSO
       lseek(2), open(2), lseek64(3)

Linux man-pages 6.7							  2023-10-31								    _llseek(2)
