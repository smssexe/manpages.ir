proc_pid_exe(5)							      File Formats Manual						       proc_pid_exe(5)

NAME
       /proc/pid/exe - symbolic link to program pathname

DESCRIPTION
       /proc/pid/exe
	      Under  Linux  2.2	 and  later,  this  file is a symbolic link containing the actual pathname of the executed command.  This symbolic link can be
	      dereferenced normally; attempting to open it will open the executable.  You can even type /proc/pid/exe to run another copy  of  the  same  exe‐
	      cutable that is being run by process pid.	 If the pathname has been unlinked, the symbolic link will contain the string ' (deleted)' appended to
	      the  original  pathname.	In a multithreaded process, the contents of this symbolic link are not available if the main thread has already termi‐
	      nated (typically by calling pthread_exit(3)).

	      Permission to dereference or read (readlink(2)) this symbolic link is governed by a  ptrace  access  mode	 PTRACE_MODE_READ_FSCREDS  check;  see
	      ptrace(2).

	      Under Linux 2.0 and earlier, /proc/pid/exe is a pointer to the binary which was executed, and appears as a symbolic link.	 A readlink(2) call on
	      this file under Linux 2.0 returns a string in the format:

		  [device]:inode

	      For example, [0301]:1502 would be inode 1502 on device major 03 (IDE, MFM, etc. drives) minor 01 (first partition on the first drive).

	      find(1) with the -inum option can be used to locate the file.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_pid_exe(5)
