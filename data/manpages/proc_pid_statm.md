proc_pid_statm(5)						      File Formats Manual						     proc_pid_statm(5)

NAME
       /proc/pid/statm - memory usage information

DESCRIPTION
       /proc/pid/statm
	      Provides information about memory usage, measured in pages.  The columns are:

		  size	     (1) total program size
			     (same as VmSize in /proc/pid/status)
		  resident   (2) resident set size
			     (inaccurate; same as VmRSS in /proc/pid/status)
		  shared     (3) number of resident shared pages
			     (i.e., backed by a file)
			     (inaccurate; same as RssFile+RssShmem in
			     /proc/pid/status)
		  text	     (4) text (code)
		  lib	     (5) library (unused since Linux 2.6; always 0)
		  data	     (6) data + stack
		  dt	     (7) dirty pages (unused since Linux 2.6; always 0)

	      Some of these values are inaccurate because of a kernel-internal scalability optimization.  If accurate values are required, use /proc/pid/smaps
	      or /proc/pid/smaps_rollup instead, which are much slower but provide accurate, detailed information.

SEE ALSO
       proc(5), proc_pid_status(5)

Linux man-pages 6.7							  2023-08-15							     proc_pid_statm(5)
