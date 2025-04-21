proc_pid_mounts(5)						      File Formats Manual						    proc_pid_mounts(5)

NAME
       /proc/pid/mounts - mounted filesystems

DESCRIPTION
       /proc/pid/mounts (since Linux 2.4.19)
	      This  file  lists	 all the filesystems currently mounted in the process's mount namespace (see mount_namespaces(7)).  The format of this file is
	      documented in fstab(5).

	      Since Linux 2.6.15, this file is pollable: after opening the file for reading, a change in this file  (i.e.,  a  filesystem  mount  or  unmount)
	      causes  select(2) to mark the file descriptor as having an exceptional condition, and poll(2) and epoll_wait(2) mark the file as having a prior‐
	      ity event (POLLPRI).  (Before Linux 2.6.30, a change in this file was indicated by the file descriptor being marked as readable  for  select(2),
	      and being marked as having an error condition for poll(2) and epoll_wait(2).)

       /proc/mounts
	      Before  Linux  2.4.19,  this file was a list of all the filesystems currently mounted on the system.  With the introduction of per-process mount
	      namespaces in Linux 2.4.19 (see mount_namespaces(7)), this file became a link to /proc/self/mounts, which lists the mounts of the process's  own
	      mount namespace.	The format of this file is documented in fstab(5).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							    proc_pid_mounts(5)
