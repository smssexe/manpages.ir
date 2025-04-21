proc_pid_maps(5)						      File Formats Manual						      proc_pid_maps(5)

NAME
       /proc/pid/maps - mapped memory regions

DESCRIPTION
       /proc/pid/maps
	      A	 file containing the currently mapped memory regions and their access permissions.  See mmap(2) for some further information about memory map‐
	      pings.

	      Permission to access this file is governed by a ptrace access mode PTRACE_MODE_READ_FSCREDS check; see ptrace(2).

	      The format of the file is:

		  address	    perms offset  dev	inode	    pathname
		  00400000-00452000 r-xp 00000000 08:02 173521	    /usr/bin/dbus-daemon
		  00651000-00652000 r--p 00051000 08:02 173521	    /usr/bin/dbus-daemon
		  00652000-00655000 rw-p 00052000 08:02 173521	    /usr/bin/dbus-daemon
		  00e03000-00e24000 rw-p 00000000 00:00 0	    [heap]
		  00e24000-011f7000 rw-p 00000000 00:00 0	    [heap]
		  ...
		  35b1800000-35b1820000 r-xp 00000000 08:02 135522  /usr/lib64/ld-2.15.so
		  35b1a1f000-35b1a20000 r--p 0001f000 08:02 135522  /usr/lib64/ld-2.15.so
		  35b1a20000-35b1a21000 rw-p 00020000 08:02 135522  /usr/lib64/ld-2.15.so
		  35b1a21000-35b1a22000 rw-p 00000000 00:00 0
		  35b1c00000-35b1dac000 r-xp 00000000 08:02 135870  /usr/lib64/libc-2.15.so
		  35b1dac000-35b1fac000 ---p 001ac000 08:02 135870  /usr/lib64/libc-2.15.so
		  35b1fac000-35b1fb0000 r--p 001ac000 08:02 135870  /usr/lib64/libc-2.15.so
		  35b1fb0000-35b1fb2000 rw-p 001b0000 08:02 135870  /usr/lib64/libc-2.15.so
		  ...
		  f2c6ff8c000-7f2c7078c000 rw-p 00000000 00:00 0    [stack:986]
		  ...
		  7fffb2c0d000-7fffb2c2e000 rw-p 00000000 00:00 0   [stack]
		  7fffb2d48000-7fffb2d49000 r-xp 00000000 00:00 0   [vdso]

	      The address field is the address space in the process that the mapping occupies.	The perms field is a set of permissions:

		  r = read
		  w = write
		  x = execute
		  s = shared
		  p = private (copy on write)

	      The offset field is the offset into the file/whatever; dev is the device (major:minor); inode is the inode on that device.  0 indicates that  no
	      inode is associated with the memory region, as would be the case with BSS (uninitialized data).

	      The  pathname  field  will  usually  be the file that is backing the mapping.  For ELF files, you can easily coordinate with the offset field by
	      looking at the Offset field in the ELF program headers (readelf -l).

	      There are additional helpful pseudo-paths:

	      [stack]
		     The initial process's (also known as the main thread's) stack.

	      [stack:tid] (from Linux 3.4 to Linux 4.4)
		     A thread's stack (where the tid is a thread ID).  It corresponds to the /proc/pid/task/tid/ path.	This field was removed in  Linux  4.5,
		     since providing this information for a process with large numbers of threads is expensive.

	      [vdso] The virtual dynamically linked shared object.  See vdso(7).

	      [heap] The process's heap.

	      [anon:name] (since Linux 5.17)
		     A named private anonymous mapping.	 Set with prctl(2) PR_SET_VMA_ANON_NAME.

	      [anon_shmem:name] (since Linux 6.2)
		     A named shared anonymous mapping.	Set with prctl(2) PR_SET_VMA_ANON_NAME.

	      If  the  pathname	 field	is  blank,  this  is  an anonymous mapping as obtained via mmap(2).  There is no easy way to coordinate this back to a
	      process's source, short of running it through gdb(1), strace(1), or similar.

	      pathname is shown unescaped except for newline characters, which are replaced with an octal escape sequence.  As a result, it is not possible to
	      determine whether the original pathname contained a newline character or the literal \012 character sequence.

	      If the mapping is file-backed and the file has been deleted, the string " (deleted)" is appended to the pathname.	 Note that this	 is  ambiguous
	      too.

	      Under Linux 2.0, there is no field giving pathname.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-09-07							      proc_pid_maps(5)
