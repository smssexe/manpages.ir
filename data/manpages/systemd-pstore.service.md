SYSTEMD-PSTORE.SERVICE(8)					    systemd-pstore.service					     SYSTEMD-PSTORE.SERVICE(8)

NAME
       systemd-pstore.service, systemd-pstore - A service to archive contents of pstore

SYNOPSIS
       /usr/lib/systemd/systemd-pstore

       systemd-pstore.service

DESCRIPTION
       systemd-pstore.service is a system service that archives the contents of the Linux persistent storage filesystem, pstore, to other storage, thus
       preserving the existing information contained in the pstore, and clearing pstore storage for future error events.

       Linux provides a persistent storage file system, pstore, that can store error records when the kernel dies (or reboots or powers-off). These records in
       turn can be referenced to debug kernel problems (currently the kernel stores the tail of the kernel log, which also contains a stack backtrace, into
       pstore).

       The pstore file system supports a variety of backends that map onto persistent storage, such as the ACPI ERST and UEFI variables. The pstore backends
       typically offer a relatively small amount of persistent storage, e.g. 64KiB, which can quickly fill up and thus prevent subsequent kernel crashes from
       recording errors. Thus there is a need to monitor and extract the pstore contents so that future kernel problems can also record information in the
       pstore.

       The pstore service is independent of the kdump service. In cloud environments specifically, host and guest filesystems are on remote filesystems (e.g.
       iSCSI or NFS), thus kdump relies (implicitly and/or explicitly) upon proper operation of networking software *and* hardware *and* infrastructure. Thus
       it may not be possible to capture a kernel coredump to a file since writes over the network may not be possible.

       The pstore backend, on the other hand, is completely local and provides a path to store error records which will survive a reboot and aid in
       post-mortem debugging.

       The systemd-pstore executable does the actual work. Upon starting, the pstore.conf file is read and the /sys/fs/pstore/ directory contents are
       processed according to the options. Pstore files are written to the journal, and optionally saved into /var/lib/systemd/pstore/.

CONFIGURATION
       The behavior of systemd-pstore is configured through the configuration file /etc/systemd/pstore.conf and corresponding snippets
       /etc/systemd/pstore.conf.d/*.conf, see pstore.conf(5).

   Disabling pstore processing
       To disable pstore processing by systemd-pstore, set

	   Storage=none

       in pstore.conf(5).

   Kernel parameters
       The kernel has two parameters, /sys/module/kernel/parameters/crash_kexec_post_notifiers and /sys/module/printk/parameters/always_kmsg_dump, that
       control writes into pstore. The first enables storing of the kernel log (including stack trace) into pstore upon a panic or crash, and the second
       enables storing of the kernel log upon a normal shutdown (shutdown, reboot, halt). These parameters can be managed via the tmpfiles.d(5) mechanism,
       specifically the file /usr/lib/tmpfiles/systemd-pstore.conf.

USAGE
       Data stored in the journal can be viewed with journalctl(1) as usual.

SEE ALSO
       pstore.conf(5)

systemd 255															     SYSTEMD-PSTORE.SERVICE(8)
