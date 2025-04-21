proc_pid_io(5)							      File Formats Manual							proc_pid_io(5)

NAME
       /proc/pid/io - I/O statistics

DESCRIPTION
       /proc/pid/io (since Linux 2.6.20)
	      This file contains I/O statistics for the process and its waited-for children, for example:

		  # cat /proc/3828/io
		  rchar: 323934931
		  wchar: 323929600
		  syscr: 632687
		  syscw: 632675
		  read_bytes: 0
		  write_bytes: 323932160
		  cancelled_write_bytes: 0

	      The fields are as follows:

	      rchar: characters read
		     The number of bytes returned by successful read(2) and similar system calls.

	      wchar: characters written
		     The number of bytes returned by successful write(2) and similar system calls.

	      syscr: read syscalls
		     The  number  of  "file  read"  system  calls—those	 from  the read(2) family, sendfile(2), copy_file_range(2), and ioctl(2) BTRFS_IOC_EN‐
		     CODED_READ[_32] (including when invoked by the kernel as part of other syscalls).

	      syscw: write syscalls
		     The number of "file write" system calls—those from the write(2)  family,  sendfile(2),  copy_file_range(2),  and  ioctl(2)	 BTRFS_IOC_EN‐
		     CODED_WRITE[_32] (including when invoked by the kernel as part of other syscalls).

	      read_bytes: bytes read
		     The number of bytes really fetched from the storage layer.	 This is accurate for block-backed filesystems.

	      write_bytes: bytes written
		     The number of bytes really sent to the storage layer.

	      cancelled_write_bytes:
		     The  above	 statistics fail to account for truncation: if a process writes 1 MB to a regular file and then removes it, said 1 MB will not
		     be written, but will have nevertheless been accounted as a 1 MB write.  This field represents the number of bytes "saved" from I/O write‐
		     back.  This can yield to having done negative I/O if caches dirtied by another process are truncated.  cancelled_write_bytes  applies  to
		     I/O already accounted-for in write_bytes.

	      Permission to access this file is governed by ptrace(2) access mode PTRACE_MODE_READ_FSCREDS.

CAVEATS
       These  counters are not atomic: on systems where 64-bit integer operations may tear, a counter could be updated simultaneously with a read, yielding an
       incorrect intermediate value.

SEE ALSO
       getrusage(2), proc(5)

Linux man-pages 6.7							  2024-03-18								proc_pid_io(5)
