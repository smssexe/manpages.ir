size_t(3type)																	 size_t(3type)

NAME
       size_t, ssize_t - count of bytes

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <stddef.h>

       typedef /* ... */  size_t;

       #include <sys/types.h>

       typedef /* ... */  ssize_t;

DESCRIPTION
       size_t Used  for	 a  count of bytes.  It is the result of the sizeof() operator.	 It is an unsigned integer type capable of storing values in the range
	      [0, SIZE_MAX].

       ssize_t
	      Used for a count of bytes or an error indication.	 It is a signed integer type capable of storing values at least in the range [-1, SSIZE_MAX].

   Use with printf(3) and scanf(3)
       size_t The length modifier for size_t for the printf(3) and the scanf(3) families of functions is z, resulting commonly in  %zu	or  %zx	 for  printing
	      size_t values.

       ssize_t
	      glibc and most other implementations provide a length modifier for ssize_t for the printf(3) and the scanf(3) families of functions, which is z;
	      resulting	 commonly  in  %zd  or %zi for printing ssize_t values.	 Although z works for ssize_t on most implementations, portable POSIX programs
	      should avoid using it—for example, by converting the value to intmax_t and using its length modifier (j).

STANDARDS
       size_t C11, POSIX.1-2008.

       ssize_t
	      POSIX.1-2008.

HISTORY
       size_t C89, POSIX.1-2001.

       ssize_t
	      POSIX.1-2001.

       <aio.h>, <glob.h>, <grp.h>, <iconv.h>, <mqueue.h>, <pwd.h>, <signal.h>, and <sys/socket.h> define size_t since POSIX.1-2008.

       <aio.h>, <mqueue.h>, and <sys/socket.h> define ssize_t since POSIX.1-2008.

NOTES
       size_t The following headers also provide size_t: <aio.h>, <glob.h>,  <grp.h>,  <iconv.h>,  <monetary.h>,  <mqueue.h>,  <ndbm.h>,  <pwd.h>,  <regex.h>,
	      <search.h>,  <signal.h>,	<stdio.h>,  <stdlib.h>,	 <string.h>, <strings.h>, <sys/mman.h>, <sys/msg.h>, <sys/sem.h>, <sys/shm.h>, <sys/socket.h>,
	      <sys/types.h>, <sys/uio.h>, <time.h>, <unistd.h>, <wchar.h>, and <wordexp.h>.

       ssize_t
	      The following headers also provide  ssize_t:  <aio.h>,  <monetary.h>,  <mqueue.h>,  <stdio.h>,  <sys/msg.h>,  <sys/socket.h>,  <sys/uio.h>,  and
	      <unistd.h>.

SEE ALSO
       read(2), readlink(2), readv(2), recv(2), send(2), write(2), fread(3), fwrite(3), memcmp(3), memcpy(3), memset(3), offsetof(3), ptrdiff_t(3type)

Linux man-pages 6.7							  2023-10-31								 size_t(3type)
