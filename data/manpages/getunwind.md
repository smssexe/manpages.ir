getunwind(2)							      System Calls Manual							  getunwind(2)

NAME
       getunwind - copy the unwind data to caller's buffer

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <linux/unwind.h>
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       [[deprecated]] long syscall(SYS_getunwind, void buf[.buf_size],
				   size_t buf_size);

DESCRIPTION
       Note: this system call is obsolete.

       The IA-64-specific getunwind() system call copies the kernel's call frame unwind data into the buffer pointed to by buf and returns the size of the un‐
       wind data; this data describes the gate page (kernel code that is mapped into user space).

       The  size  of the buffer buf is specified in buf_size.  The data is copied only if buf_size is greater than or equal to the size of the unwind data and
       buf is not NULL; otherwise, no data is copied, and the call succeeds, returning the size that would be needed to store the unwind data.

       The first part of the unwind data contains an unwind table.  The rest contains the associated unwind information, in no particular order.   The	unwind
       table contains entries of the following form:

	   u64 start;	   (64-bit address of start of function)
	   u64 end;	   (64-bit address of end of function)
	   u64 info;	   (BUF-relative offset to unwind info)

       An  entry whose start value is zero indicates the end of the table.  For more information about the format, see the IA-64 Software Conventions and Run‐
       time Architecture manual.

RETURN VALUE
       On success, getunwind() returns the size of the unwind data.  On error, -1 is returned and errno is set to indicate the error.

ERRORS
       getunwind() fails with the error EFAULT if the unwind info can't be stored in the space specified by buf.

STANDARDS
       Linux on IA-64.

HISTORY
       Linux 2.4.

       This system call has been deprecated.  The modern way to obtain the kernel's unwind data is via the vdso(7).

SEE ALSO
       getauxval(3)

Linux man-pages 6.7							  2023-10-31								  getunwind(2)
