s390_pci_mmio_write(2)						      System Calls Manual						s390_pci_mmio_write(2)

NAME
       s390_pci_mmio_write, s390_pci_mmio_read - transfer data to/from PCI MMIO memory page

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/syscall.h>	     /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_s390_pci_mmio_write, unsigned long mmio_addr,
			      const void user_buffer[.length], size_t length);
       int syscall(SYS_s390_pci_mmio_read, unsigned long mmio_addr,
			      void user_buffer[.length], size_t length);

       Note: glibc provides no wrappers for these system calls, necessitating the use of syscall(2).

DESCRIPTION
       The  s390_pci_mmio_write()  system call writes length bytes of data from the user-space buffer user_buffer to the PCI MMIO memory location specified by
       mmio_addr.  The s390_pci_mmio_read() system call reads length bytes of data from the PCI MMIO memory location specified by mmio_addr to the  user-space
       buffer user_buffer.

       These  system  calls must be used instead of the simple assignment or data-transfer operations that are used to access the PCI MMIO memory areas mapped
       to user space on the Linux System z platform.  The address specified by mmio_addr must belong to a PCI MMIO memory page mapping in the caller's address
       space, and the data being written or read must not cross a page boundary.  The length value cannot be greater than the system page size.

RETURN VALUE
       On success, s390_pci_mmio_write() and s390_pci_mmio_read() return 0.  On failure, -1 is returned and errno is set to indicate the error.

ERRORS
       EFAULT The address in mmio_addr is invalid.

       EFAULT user_buffer does not point to a valid location in the caller's address space.

       EINVAL Invalid length argument.

       ENODEV PCI support is not enabled.

       ENOMEM Insufficient memory.

STANDARDS
       Linux on s390.

HISTORY
       Linux 3.19.  System z EC12.

SEE ALSO
       syscall(2)

Linux man-pages 6.7							  2023-10-31							s390_pci_mmio_write(2)
