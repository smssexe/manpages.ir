proc_sys(5)							      File Formats Manual							   proc_sys(5)

NAME
       /proc/sys/ - system information, and sysctl pseudo-filesystem

DESCRIPTION
       /proc/sys/
	      This  directory  (present	 since Linux 1.3.57) contains a number of files and subdirectories corresponding to kernel variables.  These variables
	      can be read and in some cases modified using the /proc filesystem, and the (deprecated) sysctl(2) system call.

	      String values may be terminated by either '\0' or '\n'.

	      Integer and long values may be written either in decimal or in hexadecimal notation (e.g., 0x3FFF).  When writing multiple integer or long  val‐
	      ues,  these  may be separated by any of the following whitespace characters: ' ', '\t', or '\n'.	Using other separators leads to the error EIN‐
	      VAL.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-09-30								   proc_sys(5)
