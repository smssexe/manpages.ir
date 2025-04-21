aio_return(3)							   Library Functions Manual							 aio_return(3)

NAME
       aio_return - get return status of asynchronous I/O operation

LIBRARY
       Real-time library (librt, -lrt)

SYNOPSIS
       #include <aio.h>

       ssize_t aio_return(struct aiocb *aiocbp);

DESCRIPTION
       The  aio_return() function returns the final return status for the asynchronous I/O request with control block pointed to by aiocbp.  (See aio(7) for a
       description of the aiocb structure.)

       This function should be called only once for any given request, after aio_error(3) returns something other than EINPROGRESS.

RETURN VALUE
       If the asynchronous I/O operation has completed, this function returns the value that would have been  returned	in  case  of  a	 synchronous  read(2),
       write(2), fsync(2), or fdatasync(2), call.  On error, -1 is returned, and errno is set to indicate the error.

       If the asynchronous I/O operation has not yet completed, the return value and effect of aio_return() are undefined.

ERRORS
       EINVAL aiocbp does not point at a control block for an asynchronous I/O request of which the return status has not been retrieved yet.

       ENOSYS aio_return() is not implemented.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ aio_return()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

EXAMPLES
       See aio(7).

SEE ALSO
       aio_cancel(3), aio_error(3), aio_fsync(3), aio_read(3), aio_suspend(3), aio_write(3), lio_listio(3), aio(7)

Linux man-pages 6.7							  2023-10-31								 aio_return(3)
