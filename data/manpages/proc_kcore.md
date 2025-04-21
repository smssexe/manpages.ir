proc_kcore(5)							      File Formats Manual							 proc_kcore(5)

NAME
       /proc/kcore - physical memory

DESCRIPTION
       /proc/kcore
	      This file represents the physical memory of the system and is stored in the ELF core file format.	 With this pseudo-file, and an unstripped ker‐
	      nel (/usr/src/linux/vmlinux) binary, GDB can be used to examine the current state of any kernel data structures.

	      The total length of the file is the size of physical memory (RAM) plus 4 KiB.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								 proc_kcore(5)
