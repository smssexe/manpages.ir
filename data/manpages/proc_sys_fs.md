proc_sys_fs(5)							      File Formats Manual							proc_sys_fs(5)

NAME
       /proc/sys/fs/ - kernel variables related to filesystems

DESCRIPTION
       /proc/sys/fs/
	      This directory contains the files and subdirectories for kernel variables related to filesystems.

       /proc/sys/fs/aio-max-nr and /proc/sys/fs/aio-nr (since Linux 2.6.4)
	      aio-nr  is  the  running	total of the number of events specified by io_setup(2) calls for all currently active AIO contexts.  If aio-nr reaches
	      aio-max-nr, then io_setup(2) will fail with the error EAGAIN.  Raising aio-max-nr does not result in the preallocation or resizing of any kernel
	      data structures.

       /proc/sys/fs/binfmt_misc
	      Documentation for files in this directory can be found in the Linux kernel source in the file Documentation/admin-guide/binfmt-misc.rst  (or  in
	      Documentation/binfmt_misc.txt on older kernels).

       /proc/sys/fs/dentry-state (since Linux 2.2)
	      This file contains information about the status of the directory cache (dcache).	The file contains six numbers, nr_dentry, nr_unused, age_limit
	      (age in seconds), want_pages (pages requested by system) and two dummy values.

	      •	 nr_dentry is the number of allocated dentries (dcache entries).  This field is unused in Linux 2.2.

	      •	 nr_unused is the number of unused dentries.

	      •	 age_limit is the age in seconds after which dcache entries can be reclaimed when memory is short.

	      •	 want_pages is nonzero when the kernel has called shrink_dcache_pages() and the dcache isn't pruned yet.

       /proc/sys/fs/dir-notify-enable
	      This  file  can be used to disable or enable the dnotify interface described in fcntl(2) on a system-wide basis.	A value of 0 in this file dis‐
	      ables the interface, and a value of 1 enables it.

       /proc/sys/fs/dquot-max
	      This file shows the maximum number of cached disk quota entries.	On some (2.4) systems, it is not present.  If the number of free  cached  disk
	      quota entries is very low and you have some awesome number of simultaneous system users, you might want to raise the limit.

       /proc/sys/fs/dquot-nr
	      This file shows the number of allocated disk quota entries and the number of free disk quota entries.

       /proc/sys/fs/epoll/ (since Linux 2.6.28)
	      This  directory contains the file max_user_watches, which can be used to limit the amount of kernel memory consumed by the epoll interface.  For
	      further details, see epoll(7).

       /proc/sys/fs/file-max
	      This file defines a system-wide limit on the number of open files for all processes.  System calls that fail when encountering this  limit  fail
	      with  the	 error	ENFILE.	  (See also setrlimit(2), which can be used by a process to set the per-process limit, RLIMIT_NOFILE, on the number of
	      files it may open.)  If you get lots of error messages in the kernel log about running out of file handles (open file  descriptions)  (look  for
	      "VFS: file-max limit <number> reached"), try increasing this value:

		  echo 100000 > /proc/sys/fs/file-max

	      Privileged processes (CAP_SYS_ADMIN) can override the file-max limit.

       /proc/sys/fs/file-nr
	      This  (read-only)	 file  contains three numbers: the number of allocated file handles (i.e., the number of open file descriptions; see open(2));
	      the number of free file handles; and the maximum number of file handles (i.e., the same value as /proc/sys/fs/file-max).	If the number of allo‐
	      cated file handles is close to the maximum, you should consider increasing the maximum.  Before Linux 2.6, the kernel allocated file handles dy‐
	      namically, but it didn't free them again.	 Instead the free file handles were kept in a list for reallocation; the "free file handles" value in‐
	      dicates the size of that list.  A large number of free file handles indicates that there was a past peak in the  usage  of  open	file  handles.
	      Since Linux 2.6, the kernel does deallocate freed file handles, and the "free file handles" value is always zero.

       /proc/sys/fs/inode-max (only present until Linux 2.2)
	      This  file contains the maximum number of in-memory inodes.  This value should be 3–4 times larger than the value in file-max, since stdin, std‐
	      out and network sockets also need an inode to handle them.  When you regularly run out of inodes, you need to increase this value.

	      Starting with Linux 2.4, there is no longer a static limit on the number of inodes, and this file is removed.

       /proc/sys/fs/inode-nr
	      This file contains the first two values from inode-state.

       /proc/sys/fs/inode-state
	      This file contains seven numbers: nr_inodes, nr_free_inodes, preshrink, and four dummy values (always zero).

	      nr_inodes is the number of inodes the system has allocated.  nr_free_inodes represents the number of free inodes.

	      preshrink is nonzero when the nr_inodes > inode-max and the system needs to prune the inode list instead of allocating more;  since  Linux  2.4,
	      this field is a dummy value (always zero).

       /proc/sys/fs/inotify/ (since Linux 2.6.13)
	      This directory contains files max_queued_events, max_user_instances, and max_user_watches, that can be used to limit the amount of kernel memory
	      consumed by the inotify interface.  For further details, see inotify(7).

       /proc/sys/fs/lease-break-time
	      This  file  specifies  the  grace	 period that the kernel grants to a process holding a file lease (fcntl(2)) after it has sent a signal to that
	      process notifying it that another process is waiting to open the file.  If the lease holder does not remove or downgrade the lease  within  this
	      grace period, the kernel forcibly breaks the lease.

       /proc/sys/fs/leases-enable
	      This  file  can  be used to enable or disable file leases (fcntl(2)) on a system-wide basis.  If this file contains the value 0, leases are dis‐
	      abled.  A nonzero value enables leases.

       /proc/sys/fs/mount-max (since Linux 4.9)
	      The value in this file specifies the maximum number of mounts that may exist in a mount namespace.  The default value in this file is 100,000.

       /proc/sys/fs/mqueue/ (since Linux 2.6.6)
	      This directory contains files msg_max, msgsize_max, and queues_max, controlling the resources used by POSIX message queues.  See	mq_overview(7)
	      for details.

       /proc/sys/fs/nr_open (since Linux 2.6.25)
	      This  file  imposes a ceiling on the value to which the RLIMIT_NOFILE resource limit can be raised (see getrlimit(2)).  This ceiling is enforced
	      for both unprivileged and privileged process.  The default value in this file is 1048576.	 (Before Linux 2.6.25, the ceiling  for	 RLIMIT_NOFILE
	      was hard-coded to the same value.)

       /proc/sys/fs/overflowgid and /proc/sys/fs/overflowuid
	      These  files allow you to change the value of the fixed UID and GID.  The default is 65534.  Some filesystems support only 16-bit UIDs and GIDs,
	      although in Linux UIDs and GIDs are 32 bits.  When one of these filesystems is mounted with writes enabled, any UID or  GID  that	 would	exceed
	      65535 is translated to the overflow value before being written to disk.

       /proc/sys/fs/pipe-max-size (since Linux 2.6.35)
	      See pipe(7).

       /proc/sys/fs/pipe-user-pages-hard (since Linux 4.5)
	      See pipe(7).

       /proc/sys/fs/pipe-user-pages-soft (since Linux 4.5)
	      See pipe(7).

       /proc/sys/fs/protected_fifos (since Linux 4.19)
	      The value in this file is/can be set to one of the following:

	      0	  Writing to FIFOs is unrestricted.

	      1	  Don't allow O_CREAT open(2) on FIFOs that the caller doesn't own in world-writable sticky directories, unless the FIFO is owned by the owner
		  of the directory.

	      2	  As for the value 1, but the restriction also applies to group-writable sticky directories.

	      The  intent of the above protections is to avoid unintentional writes to an attacker-controlled FIFO when a program expected to create a regular
	      file.

       /proc/sys/fs/protected_hardlinks (since Linux 3.6)
	      When the value in this file is 0, no restrictions are placed on the creation of hard links (i.e., this is the historical behavior	 before	 Linux
	      3.6).  When the value in this file is 1, a hard link can be created to a target file only if one of the following conditions is true:

	      •	 The calling process has the CAP_FOWNER capability in its user namespace and the file UID has a mapping in the namespace.

	      •	 The  filesystem  UID of the process creating the link matches the owner (UID) of the target file (as described in credentials(7), a process's
		 filesystem UID is normally the same as its effective UID).

	      •	 All of the following conditions are true:

		  •  the target is a regular file;

		  •  the target file does not have its set-user-ID mode bit enabled;

		  •  the target file does not have both its set-group-ID and group-executable mode bits enabled; and

		  •  the caller has permission to read and write the target file (either via the file's permissions mask or because it has suitable  capabili‐
		     ties).

	      The default value in this file is 0.  Setting the value to 1 prevents a longstanding class of security issues caused by hard-link-based time-of-
	      check,  time-of-use races, most commonly seen in world-writable directories such as /tmp.	 The common method of exploiting this flaw is to cross
	      privilege boundaries when following a given hard link (i.e., a root process follows a hard link created by another user).	 Additionally, on sys‐
	      tems without separated partitions, this stops unauthorized users from "pinning" vulnerable set-user-ID and set-group-ID files against being  up‐
	      graded by the administrator, or linking to special files.

       /proc/sys/fs/protected_regular (since Linux 4.19)
	      The value in this file is/can be set to one of the following:

	      0	  Writing to regular files is unrestricted.

	      1	  Don't	 allow	O_CREAT	 open(2) on regular files that the caller doesn't own in world-writable sticky directories, unless the regular file is
		  owned by the owner of the directory.

	      2	  As for the value 1, but the restriction also applies to group-writable sticky directories.

	      The intent of the above protections is similar to protected_fifos, but allows an application to avoid writes to an  attacker-controlled  regular
	      file, where the application expected to create one.

       /proc/sys/fs/protected_symlinks (since Linux 3.6)
	      When  the	 value	in  this file is 0, no restrictions are placed on following symbolic links (i.e., this is the historical behavior before Linux
	      3.6).  When the value in this file is 1, symbolic links are followed only in the following circumstances:

	      •	 the filesystem UID of the process following the link matches the owner (UID)  of  the	symbolic  link	(as  described	in  credentials(7),  a
		 process's filesystem UID is normally the same as its effective UID);

	      •	 the link is not in a sticky world-writable directory; or

	      •	 the symbolic link and its parent directory have the same owner (UID)

	      A system call that fails to follow a symbolic link because of the above restrictions returns the error EACCES in errno.

	      The  default value in this file is 0.  Setting the value to 1 avoids a longstanding class of security issues based on time-of-check, time-of-use
	      races when accessing symbolic links.

       /proc/sys/fs/suid_dumpable (since Linux 2.6.13)
	      The value in this file is assigned to a process's "dumpable" flag in the circumstances described in prctl(2).  In effect, the value in this file
	      determines whether core dump files are produced for set-user-ID or otherwise protected/tainted binaries.	The "dumpable"	setting	 also  affects
	      the ownership of files in a process's /proc/pid directory, as described above.

	      Three different integer values can be specified:

	      0 (default)
		     This  provides the traditional (pre-Linux 2.6.13) behavior.  A core dump will not be produced for a process which has changed credentials
		     (by calling seteuid(2), setgid(2), or similar, or by executing a set-user-ID or set-group-ID program) or whose binary does not have  read
		     permission enabled.

	      1 ("debug")
		     All processes dump core when possible.  (Reasons why a process might nevertheless not dump core are described in core(5).)	 The core dump
		     is	 owned	by the filesystem user ID of the dumping process and no security is applied.  This is intended for system debugging situations
		     only: this mode is insecure because it allows unprivileged users to examine the memory contents of privileged processes.

	      2 ("suidsafe")
		     Any binary which normally would not be dumped (see "0" above) is dumped readable by root only.  This allows the user to remove  the  core
		     dump  file but not to read it.  For security reasons core dumps in this mode will not overwrite one another or other files.  This mode is
		     appropriate when administrators are attempting to debug problems in a normal environment.

		     Additionally, since Linux 3.6, /proc/sys/kernel/core_pattern must either be an absolute pathname  or  a  pipe  command,  as  detailed  in
		     core(5).  Warnings will be written to the kernel log if core_pattern does not follow these rules, and no core dump will be produced.

	      For details of the effect of a process's "dumpable" setting on ptrace access mode checking, see ptrace(2).

       /proc/sys/fs/super-max
	      This file controls the maximum number of superblocks, and thus the maximum number of mounted filesystems the kernel can have.  You need increase
	      only super-max if you need to mount more filesystems than the current value in super-max allows you to.

       /proc/sys/fs/super-nr
	      This file contains the number of filesystems currently mounted.

SEE ALSO
       proc(5), proc_sys(5)

Linux man-pages 6.7							  2023-09-30								proc_sys_fs(5)
