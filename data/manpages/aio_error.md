aio_error(3)							   Library Functions Manual							  aio_error(3)

NAME
       aio_error - get error status of asynchronous I/O operation

LIBRARY
       Real-time library (librt, -lrt)

SYNOPSIS
       #include <aio.h>

       int aio_error(const struct aiocb *aiocbp);

DESCRIPTION
       The aio_error() function returns the error status for the asynchronous I/O request with control block pointed to by aiocbp.  (See aio(7) for a descrip‐
       tion of the aiocb structure.)

RETURN VALUE
       This function returns one of the following:

       EINPROGRESS
	      if the request has not been completed yet.

       ECANCELED
	      if the request was canceled.

       0      if the request completed successfully.

       > 0    A	 positive error number, if the asynchronous I/O operation failed.  This is the same value that would have been stored in the errno variable in
	      the case of a synchronous read(2), write(2), fsync(2), or fdatasync(2) call.

ERRORS
       EINVAL aiocbp does not point at a control block for an asynchronous I/O request of which the return status (see aio_return(3)) has not  been  retrieved
	      yet.

       ENOSYS aio_error() is not implemented.

ATTRIBUTES
       For an explanation of the terms used in this section, see attributes(7).
       ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
       │ Interface														   │ Attribute	   │ Value   │
       ├───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
       │ aio_error()														   │ Thread safety │ MT-Safe │
       └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘

STANDARDS
       POSIX.1-2008.

HISTORY
       glibc 2.1.  POSIX.1-2001.

EXAMPLES
       See aio(7).

SEE ALSO
       aio_cancel(3), aio_fsync(3), aio_read(3), aio_return(3), aio_suspend(3), aio_write(3), lio_listio(3), aio(7)

Linux man-pages 6.7							  2023-10-31								  aio_error(3)
