off_t(3type)																	  off_t(3type)

NAME
       off_t, off64_t, loff_t - file sizes

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <sys/types.h>

       typedef /* ... */  off_t;

       #define _LARGEFILE64_SOURCE
       #include <sys/types.h>

       typedef /* ... */  off64_t;

       #define _GNU_SOURCE
       #include <sys/types.h>

       typedef /* ... */  loff_t;

DESCRIPTION
       off_t is used for describing file sizes.	 It is a signed integer type.

       off64_t is a 64-bit version of the type, used in glibc.

       loff_t is a 64-bit version of the type, introduced by the Linux kernel.

STANDARDS
       off_t  POSIX.1-2008.

       off64_t
	      GNU and some BSDs.

       loff_t Linux.

VERSIONS
       off_t  POSIX.1-2001.

       <aio.h> and <stdio.h> define off_t since POSIX.1-2008.

NOTES
       On some architectures, the width of off_t can be controlled with the feature test macro _FILE_OFFSET_BITS.

       The following headers also provide off_t: <aio.h>, <fcntl.h>, <stdio.h>, <sys/mman.h>, <sys/stat.h>, and <unistd.h>.

SEE ALSO
       copy_file_range(2),  llseek(2),	lseek(2),  mmap(2),  posix_fadvise(2),	pread(2),  readahead(2), sync_file_range(2), truncate(2), fseeko(3), lockf(3),
       lseek64(3), posix_fallocate(3), feature_test_macros(7)

Linux man-pages 6.7							  2023-10-31								  off_t(3type)
