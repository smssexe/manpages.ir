proc_cmdline(5)							      File Formats Manual						       proc_cmdline(5)

NAME
       /proc/cmdline - kernel boot arguments

DESCRIPTION
       /proc/cmdline
	      Arguments	 passed	 to  the  Linux kernel at boot time.  Often done via a boot manager such as lilo(8) or grub(8).	 Any arguments embedded in the
	      kernel image or initramfs via CONFIG_BOOT_CONFIG will also be displayed.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_cmdline(5)
