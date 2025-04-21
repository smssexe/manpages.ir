proc_pid_mountstats(5)						      File Formats Manual						proc_pid_mountstats(5)

NAME
       /proc/pid/mountstats - mount statistics

DESCRIPTION
       /proc/pid/mountstats (since Linux 2.6.17)
	      This  file  exports  information	(statistics,  configuration  information)  about  the mounts in the process's mount namespace (see mount_name‐
	      spaces(7)).  Lines in this file have the form:

		  device /dev/sda7 mounted on /home with fstype ext3 [stats]
		  (	  1	 )	      ( 2 )		(3 ) (	4  )

	      The fields in each line are:

	      (1)  The name of the mounted device (or "nodevice" if there is no corresponding device).

	      (2)  The mount point within the filesystem tree.

	      (3)  The filesystem type.

	      (4)  Optional statistics and configuration information.  Currently (as at Linux 2.6.26), only NFS filesystems export information via this field.

	      This file is readable only by the owner of the process.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							proc_pid_mountstats(5)
