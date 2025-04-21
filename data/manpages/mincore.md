mincore(2)							      System Calls Manual							    mincore(2)

NAME
       mincore - determine whether pages are resident in memory

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/mman.h>

       int mincore(void addr[.length], size_t length, unsigned char *vec);

   Feature Test Macro Requirements for glibc (see feature_test_macros(7)):

       mincore():
	   Since glibc 2.19:
	       _DEFAULT_SOURCE
	   glibc 2.19 and earlier:
	       _BSD_SOURCE || _SVID_SOURCE

DESCRIPTION
       mincore()  returns  a  vector  that indicates whether pages of the calling process's virtual memory are resident in core (RAM), and so will not cause a
       disk access (page fault) if referenced.	The kernel returns residency information about the pages starting at the  address  addr,  and  continuing  for
       length bytes.

       The  addr argument must be a multiple of the system page size.  The length argument need not be a multiple of the page size, but since residency infor‐
       mation is returned for whole pages, length is effectively rounded up to the next multiple of the page size.  One may obtain the page  size  (PAGE_SIZE)
       using sysconf(_SC_PAGESIZE).

       The  vec argument must point to an array containing at least (length+PAGE_SIZE-1) / PAGE_SIZE bytes.  On return, the least significant bit of each byte
       will be set if the corresponding page is currently resident in memory, and be clear otherwise.  (The settings of the other bits in each byte are	 unde‐
       fined;  these  bits  are	 reserved for possible later use.)  Of course the information returned in vec is only a snapshot: pages that are not locked in
       memory can come and go at any moment, and the contents of vec may already be stale by the time this call returns.

RETURN VALUE
       On success, mincore() returns zero.  On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EAGAIN kernel is temporarily out of resources.

       EFAULT vec points to an invalid address.

       EINVAL addr is not a multiple of the page size.

       ENOMEM length is greater than (TASK_SIZE - addr).  (This could occur if a negative value is specified for length, since that value will be  interpreted
	      as a large unsigned integer.)  In Linux 2.6.11 and earlier, the error EINVAL was returned for this condition.

       ENOMEM addr to addr + length contained unmapped memory.

STANDARDS
       None.

HISTORY
       Linux 2.3.99pre1, glibc 2.2.

       First appeared in 4.4BSD.

       NetBSD, FreeBSD, OpenBSD, Solaris 8, AIX 5.1, SunOS 4.1.

BUGS
       Before  Linux  2.6.21,  mincore()  did  not  return  correct  information  for  MAP_PRIVATE  mappings,  or  for	nonlinear  mappings (established using
       remap_file_pages(2)).

SEE ALSO
       fincore(1), madvise(2), mlock(2), mmap(2), posix_fadvise(2), posix_madvise(3)

Linux man-pages 6.7							  2023-10-31								    mincore(2)
