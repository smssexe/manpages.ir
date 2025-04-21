SYSTEMD-REMOUNT-FS.SERVICE(8)					  systemd-remount-fs.service					 SYSTEMD-REMOUNT-FS.SERVICE(8)

NAME
       systemd-remount-fs.service, systemd-remount-fs - Remount root and kernel file systems

SYNOPSIS
       systemd-remount-fs.service

       /usr/lib/systemd/systemd-remount-fs

DESCRIPTION
       systemd-remount-fs.service is an early boot service that applies mount options listed in fstab(5), or gathered from the partition table (when systemd-
       gpt-auto-generator(8) is active) to the root file system, the /usr/ file system, and the kernel API file systems. This is required so that the mount
       options of these file systems — which are pre-mounted by the kernel, the initrd, container environments or system manager code — are updated to those
       configured in /etc/fstab and the other sources. This service ignores normal file systems and only changes the root file system (i.e.  /), /usr/, and
       the virtual kernel API file systems such as /proc/, /sys/ or /dev/. This service executes no operation if no configuration is found (/etc/fstab does
       not exist or lists no entries for the mentioned file systems, or the partition table does not contain relevant entries).

       For a longer discussion of kernel API file systems see API File Systems[1].

       Note: systemd-remount-fs.service is usually pulled in by systemd-fstab-generator(8), hence it is also affected by the kernel command line option
       fstab=, which may be used to disable the generator. It may also pulled in by systemd-gpt-auto-generator(8), which is affected by systemd.gpt_auto and
       other options.

SEE ALSO
       systemd(1), fstab(5), mount(8), systemd-fstab-generator(8), systemd-gpt-auto-generator(8)

NOTES
	1. API File Systems
	   https://www.freedesktop.org/wiki/Software/systemd/APIFileSystems

systemd 255															 SYSTEMD-REMOUNT-FS.SERVICE(8)
