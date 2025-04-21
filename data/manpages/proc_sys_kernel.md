proc_sys_kernel(5)						      File Formats Manual						    proc_sys_kernel(5)

NAME
       /proc/sys/kernel/ - control a range of kernel parameters

DESCRIPTION
       /proc/sys/kernel/
	      This directory contains files controlling a range of kernel parameters, as described below.

       /proc/sys/kernel/acct
	      This  file contains three numbers: highwater, lowwater, and frequency.  If BSD-style process accounting is enabled, these values control its be‐
	      havior.  If free space on filesystem where the log lives goes below lowwater percent, accounting suspends.  If free space gets  above  highwater
	      percent,	accounting  resumes.  frequency determines how often the kernel checks the amount of free space (value is in seconds).	Default values
	      are 4, 2, and 30.	 That is, suspend accounting if 2% or less space is free; resume it if 4% or more space is free;  consider  information	 about
	      amount of free space valid for 30 seconds.

       /proc/sys/kernel/auto_msgmni (Linux 2.6.27 to Linux 3.18)
	      From  Linux 2.6.27 to Linux 3.18, this file was used to control recomputing of the value in /proc/sys/kernel/msgmni upon the addition or removal
	      of memory or upon IPC namespace creation/removal.	 Echoing "1" into this file enabled msgmni automatic recomputing (and triggered	 a  recomputa‐
	      tion of msgmni based on the current amount of available memory and number of IPC namespaces).  Echoing "0" disabled automatic recomputing.  (Au‐
	      tomatic recomputing was also disabled if a value was explicitly assigned to /proc/sys/kernel/msgmni.)  The default value in auto_msgmni was 1.

	      Since  Linux 3.19, the content of this file has no effect (because msgmni defaults to near the maximum value possible), and reads from this file
	      always return the value "0".

       /proc/sys/kernel/cap_last_cap (since Linux 3.2)
	      See capabilities(7).

       /proc/sys/kernel/cap-bound (from Linux 2.2 to Linux 2.6.24)
	      This file holds the value of the kernel capability bounding set (expressed as a signed decimal number).  This set is ANDed against the capabili‐
	      ties permitted to a process during execve(2).  Starting with Linux 2.6.25, the system-wide capability bounding set disappeared, and was replaced
	      by a per-thread bounding set; see capabilities(7).

       /proc/sys/kernel/core_pattern
	      See core(5).

       /proc/sys/kernel/core_pipe_limit
	      See core(5).

       /proc/sys/kernel/core_uses_pid
	      See core(5).

       /proc/sys/kernel/ctrl-alt-del
	      This file controls the handling of Ctrl-Alt-Del from the keyboard.  When the value in this file is 0, Ctrl-Alt-Del is trapped and	 sent  to  the
	      init(1) program to handle a graceful restart.  When the value is greater than zero, Linux's reaction to a Vulcan Nerve Pinch (tm) will be an im‐
	      mediate  reboot, without even syncing its dirty buffers.	Note: when a program (like dosemu) has the keyboard in "raw" mode, the Ctrl-Alt-Del is
	      intercepted by the program before it ever reaches the kernel tty layer, and it's up to the program to decide what to do with it.

       /proc/sys/kernel/dmesg_restrict (since Linux 2.6.37)
	      The value in this file determines who can see kernel syslog contents.  A value of 0 in this file imposes no restrictions.	 If the	 value	is  1,
	      only  privileged	users can read the kernel syslog.  (See syslog(2) for more details.)  Since Linux 3.4, only users with the CAP_SYS_ADMIN capa‐
	      bility may change the value in this file.

       /proc/sys/kernel/domainname and /proc/sys/kernel/hostname
	      can be used to set the NIS/YP domainname and the hostname of your box in exactly the same way as the  commands  domainname(1)  and  hostname(1),
	      that is:

		  # echo 'darkstar' > /proc/sys/kernel/hostname
		  # echo 'mydomain' > /proc/sys/kernel/domainname

	      has the same effect as

		  # hostname 'darkstar'
		  # domainname 'mydomain'

	      Note,  however,  that the classic darkstar.frop.org has the hostname "darkstar" and DNS (Internet Domain Name Server) domainname "frop.org", not
	      to be confused with the NIS (Network Information Service) or YP (Yellow Pages) domainname.  These two domain names  are  in  general  different.
	      For a detailed discussion see the hostname(1) man page.

       /proc/sys/kernel/hotplug
	      This file contains the pathname for the hotplug policy agent.  The default value in this file is /sbin/hotplug.

       /proc/sys/kernel/htab-reclaim (before Linux 2.4.9.2)
	      (PowerPC only) If this file is set to a nonzero value, the PowerPC htab (see kernel file Documentation/powerpc/ppc_htab.txt) is pruned each time
	      the system hits the idle loop.

       /proc/sys/kernel/keys/
	      This  directory  contains	 various  files	 that  define  parameters  and	limits	for the key-management facility.  These files are described in
	      keyrings(7).

       /proc/sys/kernel/kptr_restrict (since Linux 2.6.38)
	      The value in this file determines whether kernel addresses are exposed via /proc files and other interfaces.  A value of 0 in this file  imposes
	      no  restrictions.	 If the value is 1, kernel pointers printed using the %pK format specifier will be replaced with zeros unless the user has the
	      CAP_SYSLOG capability.  If the value is 2, kernel pointers printed using the %pK format specifier will be replaced with zeros regardless of  the
	      user's  capabilities.   The  initial default value for this file was 1, but the default was changed to 0 in Linux 2.6.39.	 Since Linux 3.4, only
	      users with the CAP_SYS_ADMIN capability can change the value in this file.

       /proc/sys/kernel/l2cr
	      (PowerPC only) This file contains a flag that controls the L2 cache of G3 processor boards.  If 0, the cache is disabled.	 Enabled if nonzero.

       /proc/sys/kernel/modprobe
	      This file contains the pathname for the kernel module loader.  The default value is /sbin/modprobe.  The file is present only if the  kernel  is
	      built  with  the CONFIG_MODULES (CONFIG_KMOD in Linux 2.6.26 and earlier) option enabled.	 It is described by the Linux kernel source file Docu‐
	      mentation/kmod.txt (present only in Linux 2.4 and earlier).

       /proc/sys/kernel/modules_disabled (since Linux 2.6.31)
	      A toggle value indicating if modules are allowed to be loaded in an otherwise modular kernel.  This toggle defaults to off (0), but can  be  set
	      true  (1).   Once true, modules can be neither loaded nor unloaded, and the toggle cannot be set back to false.  The file is present only if the
	      kernel is built with the CONFIG_MODULES option enabled.

       /proc/sys/kernel/msgmax (since Linux 2.2)
	      This file defines a system-wide limit specifying the maximum number of bytes in a single message written on a System V message queue.

       /proc/sys/kernel/msgmni (since Linux 2.4)
	      This file defines the system-wide limit on the number of message queue identifiers.  See also /proc/sys/kernel/auto_msgmni.

       /proc/sys/kernel/msgmnb (since Linux 2.2)
	      This file defines a system-wide parameter used to initialize the msg_qbytes setting for subsequently created  message  queues.   The  msg_qbytes
	      setting specifies the maximum number of bytes that may be written to the message queue.

       /proc/sys/kernel/ngroups_max (since Linux 2.6.4)
	      This is a read-only file that displays the upper limit on the number of a process's group memberships.

       /proc/sys/kernel/ns_last_pid (since Linux 3.3)
	      See pid_namespaces(7).

       /proc/sys/kernel/ostype and /proc/sys/kernel/osrelease
	      These files give substrings of /proc/version.

       /proc/sys/kernel/overflowgid and /proc/sys/kernel/overflowuid
	      These files duplicate the files /proc/sys/fs/overflowgid and /proc/sys/fs/overflowuid.

       /proc/sys/kernel/panic
	      This  file gives read/write access to the kernel variable panic_timeout.	If this is zero, the kernel will loop on a panic; if nonzero, it indi‐
	      cates that the kernel should autoreboot after this number of seconds.  When you use the software watchdog device driver, the recommended setting
	      is 60.

       /proc/sys/kernel/panic_on_oops (since Linux 2.5.68)
	      This file controls the kernel's behavior when an oops or BUG is encountered.  If this file contains 0, then the system tries to continue	opera‐
	      tion.   If  it  contains	1,  then  the  system  delays  a  few  seconds (to give klogd time to record the oops output) and then panics.	If the
	      /proc/sys/kernel/panic file is also nonzero, then the machine will be rebooted.

       /proc/sys/kernel/pid_max (since Linux 2.5.34)
	      This file specifies the value at which PIDs wrap around (i.e., the value in this file is one greater than the maximum PID).  PIDs	 greater  than
	      this  value  are not allocated; thus, the value in this file also acts as a system-wide limit on the total number of processes and threads.  The
	      default value for this file, 32768, results in the same range of PIDs as on earlier kernels.  On 32-bit platforms, 32768 is  the	maximum	 value
	      for pid_max.  On 64-bit systems, pid_max can be set to any value up to 2^22 (PID_MAX_LIMIT, approximately 4 million).

       /proc/sys/kernel/powersave-nap (PowerPC only)
	      This file contains a flag.  If set, Linux-PPC will use the "nap" mode of powersaving, otherwise the "doze" mode will be used.

       /proc/sys/kernel/printk
	      See syslog(2).

       /proc/sys/kernel/pty (since Linux 2.6.4)
	      This directory contains two files relating to the number of UNIX 98 pseudoterminals (see pts(4)) on the system.

       /proc/sys/kernel/pty/max
	      This file defines the maximum number of pseudoterminals.

       /proc/sys/kernel/pty/nr
	      This read-only file indicates how many pseudoterminals are currently in use.

       /proc/sys/kernel/random/
	      This directory contains various parameters controlling the operation of the file /dev/random.  See random(4) for further information.

       /proc/sys/kernel/random/uuid (since Linux 2.4)
	      Each read from this read-only file returns a randomly generated 128-bit UUID, as a string in the standard UUID format.

       /proc/sys/kernel/randomize_va_space (since Linux 2.6.12)
	      Select the address space layout randomization (ASLR) policy for the system (on architectures that support ASLR).	Three values are supported for
	      this file:

	      0	     Turn  ASLR off.  This is the default for architectures that don't support ASLR, and when the kernel is booted with the norandmaps parame‐
		     ter.

	      1	     Make the addresses of mmap(2) allocations, the stack, and the VDSO page randomized.  Among other things, this means that shared libraries
		     will be loaded at randomized addresses.  The text segment of PIE-linked binaries will also be loaded at a randomized address.  This value
		     is the default if the kernel was configured with CONFIG_COMPAT_BRK.

	      2	     (Since Linux 2.6.25) Also support heap randomization.  This value is the default if the kernel was not configured with CONFIG_COMPAT_BRK.

       /proc/sys/kernel/real-root-dev
	      This file is documented in the Linux kernel source file Documentation/admin-guide/initrd.rst (or Documentation/initrd.txt before Linux 4.10).

       /proc/sys/kernel/reboot-cmd (Sparc only)
	      This file seems to be a way to give an argument to the SPARC ROM/Flash boot loader.  Maybe to tell it what to do after rebooting?

       /proc/sys/kernel/rtsig-max
	      (Up to and including Linux 2.6.7; see setrlimit(2)) This file can be used to tune the maximum number of POSIX real-time  (queued)	 signals  that
	      can be outstanding in the system.

       /proc/sys/kernel/rtsig-nr
	      (Up to and including Linux 2.6.7.)  This file shows the number of POSIX real-time signals currently queued.

       /proc/pid/sched_autogroup_enabled (since Linux 2.6.38)
	      See sched(7).

       /proc/sys/kernel/sched_child_runs_first (since Linux 2.6.23)
	      If  this	file  contains the value zero, then, after a fork(2), the parent is first scheduled on the CPU.	 If the file contains a nonzero value,
	      then the child is scheduled first on the CPU.  (Of course, on a multiprocessor system, the parent and the child might both immediately be sched‐
	      uled on a CPU.)

       /proc/sys/kernel/sched_rr_timeslice_ms (since Linux 3.9)
	      See sched_rr_get_interval(2).

       /proc/sys/kernel/sched_rt_period_us (since Linux 2.6.25)
	      See sched(7).

       /proc/sys/kernel/sched_rt_runtime_us (since Linux 2.6.25)
	      See sched(7).

       /proc/sys/kernel/seccomp/ (since Linux 4.14)
	      This directory provides additional seccomp information and configuration.	 See seccomp(2) for further details.

       /proc/sys/kernel/sem (since Linux 2.4)
	      This file contains 4 numbers defining limits for System V IPC semaphores.	 These fields are, in order:

	      SEMMSL The maximum semaphores per semaphore set.

	      SEMMNS A system-wide limit on the number of semaphores in all semaphore sets.

	      SEMOPM The maximum number of operations that may be specified in a semop(2) call.

	      SEMMNI A system-wide limit on the maximum number of semaphore identifiers.

       /proc/sys/kernel/sg-big-buff
	      This file shows the size of the generic SCSI device (sg) buffer.	You can't tune it just yet, but you could change it at compile time by editing
	      include/scsi/sg.h and changing the value of SG_BIG_BUFF.	However, there shouldn't be any reason to change this value.

       /proc/sys/kernel/shm_rmid_forced (since Linux 3.1)
	      If this file is set to 1, all System V shared memory segments will be marked for destruction as soon as the number of attached  processes	 falls
	      to zero; in other words, it is no longer possible to create shared memory segments that exist independently of any attached process.

	      The  effect  is  as  though a shmctl(2) IPC_RMID is performed on all existing segments as well as all segments created in the future (until this
	      file is reset to 0).  Note that existing segments that are attached to no process will be immediately destroyed when this	 file  is  set	to  1.
	      Setting  this  option will also destroy segments that were created, but never attached, upon termination of the process that created the segment
	      with shmget(2).

	      Setting this file to 1 provides a way of ensuring that all System V shared memory segments are counted against the resource usage	 and  resource
	      limits (see the description of RLIMIT_AS in getrlimit(2)) of at least one process.

	      Because  setting this file to 1 produces behavior that is nonstandard and could also break existing applications, the default value in this file
	      is 0.  Set this file to 1 only if you have a good understanding of the semantics of the applications using System V shared memory on  your  sys‐
	      tem.

       /proc/sys/kernel/shmall (since Linux 2.2)
	      This file contains the system-wide limit on the total number of pages of System V shared memory.

       /proc/sys/kernel/shmmax (since Linux 2.2)
	      This  file can be used to query and set the run-time limit on the maximum (System V IPC) shared memory segment size that can be created.	Shared
	      memory segments up to 1 GB are now supported in the kernel.  This value defaults to SHMMAX.

       /proc/sys/kernel/shmmni (since Linux 2.4)
	      This file specifies the system-wide maximum number of System V shared memory segments that can be created.

       /proc/sys/kernel/sysctl_writes_strict (since Linux 3.16)
	      The value in this file determines how the file offset affects the behavior of updating entries in files under /proc/sys.	 The  file  has	 three
	      possible values:

	      -1  This	provides  legacy  handling, with no printk warnings.  Each write(2) must fully contain the value to be written, and multiple writes on
		  the same file descriptor will overwrite the entire value, regardless of the file position.

	      0	  (default) This provides the same behavior as for -1, but printk warnings are written for processes that perform writes when the file	offset
		  is not 0.

	      1	  Respect  the	file offset when writing strings into /proc/sys files.	Multiple writes will append to the value buffer.  Anything written be‐
		  yond the maximum length of the value buffer will be ignored.	Writes to numeric /proc/sys entries must always be at file offset  0  and  the
		  value must be fully contained in the buffer provided to write(2).

       /proc/sys/kernel/sysrq
	      This  file controls the functions allowed to be invoked by the SysRq key.	 By default, the file contains 1 meaning that every possible SysRq re‐
	      quest is allowed (in older kernel versions, SysRq was disabled by default, and you were required to specifically enable it at run-time, but this
	      is not the case any more).  Possible values in this file are:

	      0	   Disable sysrq completely

	      1	   Enable all functions of sysrq

	      > 1  Bit mask of allowed sysrq functions, as follows:
		     2	Enable control of console logging level
		     4	Enable control of keyboard (SAK, unraw)
		     8	Enable debugging dumps of processes etc.
		    16	Enable sync command
		    32	Enable remount read-only
		    64	Enable signaling of processes (term, kill, oom-kill)
		   128	Allow reboot/poweroff
		   256	Allow nicing of all real-time tasks

	      This file is present only if the CONFIG_MAGIC_SYSRQ kernel configuration option is enabled.  For further details see  the	 Linux	kernel	source
	      file Documentation/admin-guide/sysrq.rst (or Documentation/sysrq.txt before Linux 4.10).

       /proc/sys/kernel/version
	      This file contains a string such as:

		  #5 Wed Feb 25 21:49:24 MET 1998

	      The "#5" means that this is the fifth kernel built from this source base and the date following it indicates the time the kernel was built.

       /proc/sys/kernel/threads-max (since Linux 2.3.11)
	      This file specifies the system-wide limit on the number of threads (tasks) that can be created on the system.

	      Since  Linux 4.1, the value that can be written to threads-max is bounded.  The minimum value that can be written is 20.	The maximum value that
	      can be written is given by the constant FUTEX_TID_MASK (0x3fffffff).  If a value outside of this range is written to threads-max, the error EIN‐
	      VAL occurs.

	      The value written is checked against the available RAM pages.  If the thread structures would occupy too much (more than 1/8th) of the available
	      RAM pages, threads-max is reduced accordingly.

       /proc/sys/kernel/yama/ptrace_scope (since Linux 3.5)
	      See ptrace(2).

       /proc/sys/kernel/zero-paged (PowerPC only)
	      This file contains a flag.  When enabled (nonzero), Linux-PPC will pre-zero pages in the idle loop, possibly speeding up get_free_pages.

SEE ALSO
       proc(5), proc_sys(5)

Linux man-pages 6.7							  2023-09-30							    proc_sys_kernel(5)
