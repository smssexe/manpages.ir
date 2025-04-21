proc_profile(5)							      File Formats Manual						       proc_profile(5)

NAME
       /proc/profile - kernel profiling

DESCRIPTION
       /proc/profile (since Linux 2.4)
	      This  file is present only if the kernel was booted with the profile=1 command-line option.  It exposes kernel profiling information in a binary
	      format for use by readprofile(1).	 Writing (e.g., an empty string) to this file resets the profiling counters; on some architectures, writing  a
	      binary integer "profiling multiplier" of size sizeof(int) sets the profiling interrupt frequency.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_profile(5)
