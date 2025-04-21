iovec(3type)																	  iovec(3type)

NAME
       iovec - Vector I/O data structure

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/uio.h>

       struct iovec {
	   void	  *iov_base;  /* Starting address */
	   size_t  iov_len;   /* Size of the memory pointed to by iov_base. */
       };

DESCRIPTION
       Describes  a region of memory, beginning at iov_base address and with the size of iov_len bytes.	 System calls use arrays of this structure, where each
       element of the array represents a memory region, and the whole array represents a vector of memory regions.  The maximum number of iovec structures  in
       that array is limited by IOV_MAX (defined in <limits.h>, or accessible via the call sysconf(_SC_IOV_MAX)).

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

NOTES
       The following header also provides this type: <sys/socket.h>.

SEE ALSO
       process_madvise(2), readv(2)

Linux man-pages 6.7							  2023-10-31								  iovec(3type)
