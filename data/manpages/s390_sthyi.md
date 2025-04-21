s390_sthyi(2)							      System Calls Manual							 s390_sthyi(2)

NAME
       s390_sthyi - emulate STHYI instruction

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <asm/sthyi.h>	     /* Definition of STHYI_* constants */
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_s390_sthyi, unsigned long function_code,
		   void *resp_buffer, uint64_t *return_code,
		   unsigned long flags);

       Note: glibc provides no wrapper for s390_sthyi(), necessitating the use of syscall(2).

DESCRIPTION
       The  s390_sthyi() system call emulates the STHYI (Store Hypervisor Information) instruction.  It provides hardware resource information for the machine
       and its virtualization levels.  This includes CPU type and capacity, as well as the machine model and other metrics.

       The function_code argument indicates which function to perform.	The following code(s) are supported:

       STHYI_FC_CP_IFL_CAP
	      Return CP (Central Processor) and IFL (Integrated Facility for Linux) capacity information.

       The resp_buffer argument specifies the address of a response buffer.  When the function_code is STHYI_FC_CP_IFL_CAP, the buffer must be one  page  (4K)
       in  size.  If the system call returns 0, the response buffer will be filled with CPU capacity information.  Otherwise, the response buffer's content is
       unchanged.

       The return_code argument stores the return code of the STHYI instruction, using one of the following values:

       0      Success.

       4      Unsupported function code.

       For further details about return_code, function_code, and resp_buffer, see the reference given in NOTES.

       The flags argument is provided to allow for future extensions and currently must be set to 0.

RETURN VALUE
       On success (that is: emulation succeeded), the return value of s390_sthyi() matches the condition code of the STHYI instructions, which is a  value  in
       the  range  [0..3].  A return value of 0 indicates that CPU capacity information is stored in *resp_buffer.  A return value of 3 indicates "unsupported
       function code" and the content of *resp_buffer is unchanged.  The return values 1 and 2 are reserved.

       On error, -1 is returned, and errno is set to indicate the error.

ERRORS
       EFAULT The value specified in resp_buffer or return_code is not a valid address.

       EINVAL The value specified in flags is nonzero.

       ENOMEM Allocating memory for handling the CPU capacity information failed.

       EOPNOTSUPP
	      The value specified in function_code is not valid.

STANDARDS
       Linux on s390.

HISTORY
       Linux 4.15.

NOTES
       For details of the STHYI instruction, see the documentation page.

       When the system call interface is used, the response buffer doesn't have to fulfill alignment requirements described in the STHYI  instruction  defini‐
       tion.

       The kernel caches the response (for up to one second, as of Linux 4.16).	 Subsequent system call invocations may return the cached response.

SEE ALSO
       syscall(2)

Linux man-pages 6.7							  2023-10-31								 s390_sthyi(2)
