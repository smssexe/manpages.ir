proc_kpagecgroup(5)						      File Formats Manual						   proc_kpagecgroup(5)

NAME
       /proc/kpagecgroup - memory cgroups

DESCRIPTION
       /proc/kpagecgroup (since Linux 4.3)
	      This  file  contains  a  64-bit  inode  number of the memory cgroup each page is charged to, indexed by page frame number (see the discussion of
	      /proc/pid/pagemap).

	      The /proc/kpagecgroup file is present only if the CONFIG_MEMCG kernel configuration option is enabled.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_kpagecgroup(5)
