outb(2)								      System Calls Manual							       outb(2)

NAME
       outb, outw, outl, outsb, outsw, outsl, inb, inw, inl, insb, insw, insl, outb_p, outw_p, outl_p, inb_p, inw_p, inl_p - port I/O

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <sys/io.h>

       unsigned char inb(unsigned short port);
       unsigned char inb_p(unsigned short port);
       unsigned short inw(unsigned short port);
       unsigned short inw_p(unsigned short port);
       unsigned int inl(unsigned short port);
       unsigned int inl_p(unsigned short port);

       void outb(unsigned char value, unsigned short port);
       void outb_p(unsigned char value, unsigned short port);
       void outw(unsigned short value, unsigned short port);
       void outw_p(unsigned short value, unsigned short port);
       void outl(unsigned int value, unsigned short port);
       void outl_p(unsigned int value, unsigned short port);

       void insb(unsigned short port, void addr[.count],
		  unsigned long count);
       void insw(unsigned short port, void addr[.count],
		  unsigned long count);
       void insl(unsigned short port, void addr[.count],
		  unsigned long count);
       void outsb(unsigned short port, const void addr[.count],
		  unsigned long count);
       void outsw(unsigned short port, const void addr[.count],
		  unsigned long count);
       void outsl(unsigned short port, const void addr[.count],
		  unsigned long count);

DESCRIPTION
       This family of functions is used to do low-level port input and output.	The out* functions do port output, the in* functions do port input; the b-suf‐
       fix functions are byte-width and the w-suffix functions word-width; the _p-suffix functions pause until the I/O completes.

       They are primarily designed for internal kernel use, but can be used from user space.

       You  must  compile with -O or -O2 or similar.  The functions are defined as inline macros, and will not be substituted in without optimization enabled,
       causing unresolved references at link time.

       You use ioperm(2) or alternatively iopl(2) to tell the kernel to allow the user space application to access the I/O ports in question.  Failure	to  do
       this will cause the application to receive a segmentation fault.

VERSIONS
       outb()  and friends are hardware-specific.  The value argument is passed first and the port argument is passed second, which is the opposite order from
       most DOS implementations.

STANDARDS
       None.

SEE ALSO
       ioperm(2), iopl(2)

Linux man-pages 6.7							  2023-10-31								       outb(2)
