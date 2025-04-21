proc_pid_clear_refs(5)						      File Formats Manual						proc_pid_clear_refs(5)

NAME
       /proc/pid/clear_refs - reset the PG_Referenced and ACCESSED/YOUNG bits

DESCRIPTION
       /proc/pid/clear_refs (since Linux 2.6.22)

	      This is a write-only file, writable only by owner of the process.

	      The following values may be written to the file:

	      1 (since Linux 2.6.22)
		     Reset the PG_Referenced and ACCESSED/YOUNG bits for all the pages associated with the process.  (Before Linux 2.6.32, writing any nonzero
		     value to this file had this effect.)

	      2 (since Linux 2.6.32)
		     Reset the PG_Referenced and ACCESSED/YOUNG bits for all anonymous pages associated with the process.

	      3 (since Linux 2.6.32)
		     Reset the PG_Referenced and ACCESSED/YOUNG bits for all file-mapped pages associated with the process.

	      Clearing the PG_Referenced and ACCESSED/YOUNG bits provides a method to measure approximately how much memory a process is using.	 One first in‐
	      spects  the  values in the "Referenced" fields for the VMAs shown in /proc/pid/smaps to get an idea of the memory footprint of the process.  One
	      then clears the PG_Referenced and ACCESSED/YOUNG bits and, after some measured time interval, once again inspects the values in the "Referenced"
	      fields to get an idea of the change in memory footprint of the process during the measured interval.  If one is interested  only	in  inspecting
	      the selected mapping types, then the value 2 or 3 can be used instead of 1.

	      Further values can be written to affect different properties:

	      4 (since Linux 3.11)
		     Clear  the	 soft-dirty  bit  for  all the pages associated with the process.  This is used (in conjunction with /proc/pid/pagemap) by the
		     check-point restore system to discover which pages of a process have been dirtied since the file /proc/pid/clear_refs was written to.

	      5 (since Linux 4.0)
		     Reset the peak resident set size ("high water mark") to the process's current resident set size value.

	      Writing any value to /proc/pid/clear_refs other than those listed above has no effect.

	      The /proc/pid/clear_refs file is present only if the CONFIG_PROC_PAGE_MONITOR kernel configuration option is enabled.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-09-07							proc_pid_clear_refs(5)
