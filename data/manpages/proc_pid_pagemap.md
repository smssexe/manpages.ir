proc_pid_pagemap(5)						      File Formats Manual						   proc_pid_pagemap(5)

NAME
       /proc/pid/pagemap - mapping of virtual pages

DESCRIPTION
       /proc/pid/pagemap (since Linux 2.6.25)
	      This  file  shows	 the  mapping of each of the process's virtual pages into physical page frames or swap area.  It contains one 64-bit value for
	      each virtual page, with the bits set as follows:

	      63     If set, the page is present in RAM.

	      62     If set, the page is in swap space

	      61 (since Linux 3.5)
		     The page is a file-mapped page or a shared anonymous page.

	      60–58 (since Linux 3.11)
		     Zero

	      57 (since Linux 5.14)
		     If set, the page is write-protected through userfaultfd(2).

	      56 (since Linux 4.2)
		     The page is exclusively mapped.

	      55 (since Linux 3.11)
		     PTE is soft-dirty (see the kernel source file Documentation/admin-guide/mm/soft-dirty.rst).

	      54–0   If the page is present in RAM (bit 63), then these bits provide the page frame number, which can be used to  index	 /proc/kpageflags  and
		     /proc/kpagecount.	If the page is present in swap (bit 62), then bits 4–0 give the swap type, and bits 54–5 encode the swap offset.

	      Before Linux 3.11, bits 60–55 were used to encode the base-2 log of the page size.

	      To  employ  /proc/pid/pagemap  efficiently,  use /proc/pid/maps to determine which areas of memory are actually mapped and seek to skip over un‐
	      mapped regions.

	      The /proc/pid/pagemap file is present only if the CONFIG_PROC_PAGE_MONITOR kernel configuration option is enabled.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_pid_pagemap(5)
