proc_pid_map_files(5)						      File Formats Manual						 proc_pid_map_files(5)

NAME
       /proc/pid/map_files/ - memory-mapped files

DESCRIPTION
       /proc/pid/map_files/ (since Linux 3.3)
	      This subdirectory contains entries corresponding to memory-mapped files (see mmap(2)).  Entries are named by memory region start and end address
	      pair (expressed as hexadecimal numbers), and are symbolic links to the mapped files themselves.  Here is an example, with the output wrapped and
	      reformatted to fit on an 80-column display:

		  # ls -l /proc/self/map_files/
		  lr--------. 1 root root 64 Apr 16 21:31
			      3252e00000-3252e20000 -> /usr/lib64/ld-2.15.so
		  ...

	      Although	these entries are present for memory regions that were mapped with the MAP_FILE flag, the way anonymous shared memory (regions created
	      with the MAP_ANON | MAP_SHARED flags) is implemented in Linux means that such regions also appear on this directory.  Here is an	example	 where
	      the target file is the deleted /dev/zero one:

		  lrw-------. 1 root root 64 Apr 16 21:33
			      7fc075d2f000-7fc075e6f000 -> /dev/zero (deleted)

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

	      Until Linux 4.3, this directory appeared only if the CONFIG_CHECKPOINT_RESTORE kernel configuration option was enabled.

	      Capabilities  are	 required  to  read  the  contents  of	the  symbolic  links in this directory: before Linux 5.9, the reading process requires
	      CAP_SYS_ADMIN in the initial user namespace; since Linux 5.9, the reading process must have either CAP_SYS_ADMIN	or  CAP_CHECKPOINT_RESTORE  in
	      the initial (i.e. root) user namespace.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							 proc_pid_map_files(5)
