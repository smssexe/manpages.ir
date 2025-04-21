proc_pid(5)							      File Formats Manual							   proc_pid(5)

NAME
       /proc/pid/, /proc/self/ - process information

DESCRIPTION
       /proc/pid/
	      There  is	 a numerical subdirectory for each running process; the subdirectory is named by the process ID.  Each /proc/pid subdirectory contains
	      the pseudo-files and directories described below.

	      The files inside each /proc/pid directory are normally owned by the effective user and effective group ID of the process.	 However, as  a	 secu‐
	      rity measure, the ownership is made root:root if the process's "dumpable" attribute is set to a value other than 1.

	      Before  Linux  4.11,  root:root meant the "global" root user ID and group ID (i.e., UID 0 and GID 0 in the initial user namespace).  Since Linux
	      4.11, if the process is in a noninitial user namespace that has a valid mapping for user (group) ID  0  inside  the  namespace,  then  the  user
	      (group)  ownership of the files under /proc/pid is instead made the same as the root user (group) ID of the namespace.  This means that inside a
	      container, things work as expected for the container "root" user.

	      The process's "dumpable" attribute may change for the following reasons:

	      •	 The attribute was explicitly set via the prctl(2) PR_SET_DUMPABLE operation.

	      •	 The attribute was reset to the value in the file /proc/sys/fs/suid_dumpable (described below), for the reasons described in prctl(2).

	      Resetting the "dumpable" attribute to 1 reverts the ownership of the /proc/pid/* files to the process's effective UID and GID.   Note,  however,
	      that  if the effective UID or GID is subsequently modified, then the "dumpable" attribute may be reset, as described in prctl(2).	 Therefore, it
	      may be desirable to reset the "dumpable" attribute after making any desired changes to the process's effective UID or GID.

       /proc/self/
	      This directory refers to the process accessing the /proc filesystem, and is identical to the /proc directory named by the process ID of the same
	      process.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								   proc_pid(5)
