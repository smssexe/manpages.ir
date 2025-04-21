proc_interrupts(5)						      File Formats Manual						    proc_interrupts(5)

NAME
       /proc/interrupts - number of interrupts

DESCRIPTION
       /proc/interrupts
	      This  is	used  to  record the number of interrupts per CPU per IO device.  Since Linux 2.6.24, for the i386 and x86-64 architectures, at least,
	      this also includes interrupts internal to the system (that is, not associated with a device as such), such as NMI (nonmaskable  interrupt),  LOC
	      (local timer interrupt), and for SMP systems, TLB (TLB flush interrupt), RES (rescheduling interrupt), CAL (remote function call interrupt), and
	      possibly others.	Very easy to read formatting, done in ASCII.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_interrupts(5)
