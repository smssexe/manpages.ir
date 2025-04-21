proc_kpagecount(5)						      File Formats Manual						    proc_kpagecount(5)

NAME
       /proc/kpagecount - count of mappings of physical pages

DESCRIPTION
       /proc/kpagecount (since Linux 2.6.25)
	      This file contains a 64-bit count of the number of times each physical page frame is mapped, indexed by page frame number (see the discussion of
	      /proc/pid/pagemap).

	      The /proc/kpagecount file is present only if the CONFIG_PROC_PAGE_MONITOR kernel configuration option is enabled.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_kpagecount(5)
