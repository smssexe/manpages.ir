proc_kmsg(5)							      File Formats Manual							  proc_kmsg(5)

NAME
       /proc/kmsg - kernel messages

DESCRIPTION
       /proc/kmsg
	      This file can be used instead of the syslog(2) system call to read kernel messages.  A process must have superuser privileges to read this file,
	      and  only	 one  process should read this file.  This file should not be read if a syslog process is running which uses the syslog(2) system call
	      facility to log kernel messages.

	      Information in this file is retrieved with the dmesg(1) program.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								  proc_kmsg(5)
