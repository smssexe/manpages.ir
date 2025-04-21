proc_kpageflags(5)						      File Formats Manual						    proc_kpageflags(5)

NAME
       /proc/kpageflags - physical pages frame masks

DESCRIPTION
       /proc/kpageflags (since Linux 2.6.25)
	      This  file  contains  64-bit  masks  corresponding  to  each  physical  page  frame;  it	is indexed by page frame number (see the discussion of
	      /proc/pid/pagemap).  The bits are as follows:

		      0	  -   KPF_LOCKED
		      1	  -   KPF_ERROR
		      2	  -   KPF_REFERENCED
		      3	  -   KPF_UPTODATE
		      4	  -   KPF_DIRTY
		      5	  -   KPF_LRU
		      6	  -   KPF_ACTIVE
		      7	  -   KPF_SLAB
		      8	  -   KPF_WRITEBACK
		      9	  -   KPF_RECLAIM
		     10	  -   KPF_BUDDY
		     11	  -   KPF_MMAP		  (since Linux 2.6.31)
		     12	  -   KPF_ANON		  (since Linux 2.6.31)
		     13	  -   KPF_SWAPCACHE	  (since Linux 2.6.31)
		     14	  -   KPF_SWAPBACKED	  (since Linux 2.6.31)
		     15	  -   KPF_COMPOUND_HEAD	  (since Linux 2.6.31)
		     16	  -   KPF_COMPOUND_TAIL	  (since Linux 2.6.31)
		     17	  -   KPF_HUGE		  (since Linux 2.6.31)
		     18	  -   KPF_UNEVICTABLE	  (since Linux 2.6.31)
		     19	  -   KPF_HWPOISON	  (since Linux 2.6.31)
		     20	  -   KPF_NOPAGE	  (since Linux 2.6.31)
		     21	  -   KPF_KSM		  (since Linux 2.6.32)
		     22	  -   KPF_THP		  (since Linux 3.4)
		     23	  -   KPF_BALLOON	  (since Linux 3.18)
		     24	  -   KPF_ZERO_PAGE	  (since Linux 4.0)
		     25	  -   KPF_IDLE		  (since Linux 4.3)
		     26	  -   KPF_PGTABLE	  (since Linux 4.18)

	      For further details on the meanings of these bits, see the kernel source file Documentation/admin-guide/mm/pagemap.rst.	Before	Linux  2.6.29,
	      KPF_WRITEBACK, KPF_RECLAIM, KPF_BUDDY, and KPF_LOCKED did not report correctly.

	      The /proc/kpageflags file is present only if the CONFIG_PROC_PAGE_MONITOR kernel configuration option is enabled.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_kpageflags(5)
