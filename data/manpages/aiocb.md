aiocb(3type)																	  aiocb(3type)

NAME
       aiocb - asynchronous I/O control block

LIBRARY
       Standard C library (libc)

SYNOPSIS
       #include <aio.h>

       struct aiocb {
	   int		   aio_fildes;	   /* File descriptor */
	   off_t	   aio_offset;	   /* File offset */
	   volatile void  *aio_buf;	   /* Location of buffer */
	   size_t	   aio_nbytes;	   /* Length of transfer */
	   int		   aio_reqprio;	   /* Request priority offset */
	   struct sigevent aio_sigevent;   /* Signal number and value */
	   int		   aio_lio_opcode; /* Operation to be performed */
       };

DESCRIPTION
       For further information about this structure, see aio(7).

STANDARDS
       POSIX.1-2008.

HISTORY
       POSIX.1-2001.

SEE ALSO
       aio_cancel(3), aio_error(3), aio_fsync(3), aio_read(3), aio_return(3), aio_suspend(3), aio_write(3), lio_listio(3)

Linux man-pages 6.7							  2023-10-31								  aiocb(3type)
