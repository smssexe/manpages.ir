SYSTEMD-FSTAB-GENERATOR(8)					    systemd-fstab-generator					    SYSTEMD-FSTAB-GENERATOR(8)

NAME
       systemd-fstab-generator - Unit generator for /etc/fstab

SYNOPSIS
       /usr/lib/systemd/system-generators/systemd-fstab-generator

DESCRIPTION
       systemd-fstab-generator is a generator that translates /etc/fstab (see fstab(5) for details) into native systemd units early at boot and when
       configuration of the system manager is reloaded. This will instantiate mount and swap units as necessary.

       The passno field is treated like a simple boolean, and the ordering information is discarded. However, if the root file system is checked, it is
       checked before all the other file systems.

       See systemd.mount(5) and systemd.swap(5) for more information about special /etc/fstab mount options this generator understands.

       One special topic is handling of symbolic links. Historical init implementations supported symlinks in /etc/fstab. Because mount units will refuse
       mounts where the target is a symbolic link, this generator will resolve any symlinks as far as possible when processing /etc/fstab in order to enhance
       backwards compatibility. If a symlink target does not exist at the time that this generator runs, it is assumed that the symlink target is the final
       target of the mount.

       systemd-fstab-generator implements systemd.generator(7).

KERNEL COMMAND LINE
       systemd-fstab-generator understands the following kernel command line parameters:

       fstab=, rd.fstab=
	   Takes a boolean argument. Defaults to "yes". If "no", causes the generator to ignore any mounts or swap devices configured in /etc/fstab.
	   rd.fstab= is honored only in the initrd, while fstab= is honored by both the main system and the initrd.

	   Added in version 186.

       root=
	   Configures the operating system's root filesystem to mount when running in the initrd. This accepts a device node path (usually
	   /dev/disk/by-uuid/...  or /dev/disk/by-label/...  or similar), or the special values "gpt-auto", "fstab", and "tmpfs".

	   Use "gpt-auto" to explicitly request automatic root file system discovery via systemd-gpt-auto-generator(8).

	   Use "fstab" to explicitly request automatic root file system discovery via the initrd /etc/fstab rather than via kernel command line.

	   Use "tmpfs" in order to mount a tmpfs(5) file system as root file system of the OS. This is useful in combination with mount.usr= (see below) in
	   order to combine a volatile root file system with a separate, immutable /usr/ file system. Also see systemd.volatile= below.

	   Added in version 217.

       rootfstype=
	   Takes the root filesystem type that will be passed to the mount command.  rootfstype= is honored by the initrd.

	   Added in version 217.

       rootflags=
	   Takes the root filesystem mount options to use.  rootflags= is honored by the initrd.

	   Note that unlike most kernel command line options this setting does not override settings made in configuration files (specifically: the mount
	   option string in /etc/fstab). See systemd-remount-fs.service(8).

	   Added in version 217.

       mount.usr=
	   Takes the /usr/ filesystem to be mounted by the initrd. If mount.usrfstype= or mount.usrflags= is set, then mount.usr= will default to the value
	   set in root=.

	   Otherwise, this parameter defaults to the /usr/ entry found in /etc/fstab on the root filesystem.

	   mount.usr= is honored by the initrd.

	   Added in version 217.

       mount.usrfstype=
	   Takes the /usr/ filesystem type that will be passed to the mount command. If mount.usr= or mount.usrflags= is set, then mount.usrfstype= will
	   default to the value set in rootfstype=.

	   Otherwise, this value will be read from the /usr/ entry in /etc/fstab on the root filesystem.

	   mount.usrfstype= is honored by the initrd.

	   Added in version 217.

       mount.usrflags=
	   Takes the /usr/ filesystem mount options to use. If mount.usr= or mount.usrfstype= is set, then mount.usrflags= will default to the value set in
	   rootflags=.

	   Otherwise, this value will be read from the /usr/ entry in /etc/fstab on the root filesystem.

	   mount.usrflags= is honored by the initrd.

	   Added in version 217.

       roothash=, usrhash=
	   These options are primarily read by systemd-veritysetup-generator(8). When set this indicates that the root file system (or /usr/) shall be mounted
	   from Verity volumes with the specified hashes. If these kernel command line options are set the root (or /usr/) file system is thus mounted from a
	   device mapper volume /dev/mapper/root (or /dev/mapper/usr).

	   Added in version 251.

       systemd.volatile=
	   Controls whether the system shall boot up in volatile mode. Takes a boolean argument or the special value state.

	   If false (the default), this generator makes no changes to the mount tree and the system is booted up in normal mode.

	   If true the generator ensures systemd-volatile-root.service(8) is run in the initrd. This service changes the mount table before transitioning to
	   the host system, so that a volatile memory file system ("tmpfs") is used as root directory, with only /usr/ mounted into it from the configured
	   root file system, in read-only mode. This way the system operates in fully stateless mode, with all configuration and state reset at boot and lost
	   at shutdown, as /etc/ and /var/ will be served from the (initially unpopulated) volatile memory file system.

	   If set to state the generator will leave the root directory mount point unaltered, however will mount a "tmpfs" file system to /var/. In this mode
	   the normal system configuration (i.e. the contents of "/etc/") is in effect (and may be modified during system runtime), however the system state
	   (i.e. the contents of "/var/") is reset at boot and lost at shutdown.

	   If this setting is set to "overlay" the root file system is set up as "overlayfs" mount combining the read-only root directory with a writable
	   "tmpfs", so that no modifications are made to disk, but the file system may be modified nonetheless with all changes being lost at reboot.

	   Note that in none of these modes the root directory, /etc/, /var/ or any other resources stored in the root file system are physically removed.
	   It's thus safe to boot a system that is normally operated in non-volatile mode temporarily into volatile mode, without losing data.

	   Note that with the exception of "overlay" mode, enabling this setting will only work correctly on operating systems that can boot up with only
	   /usr/ mounted, and are able to automatically populate /etc/, and also /var/ in case of "systemd.volatile=yes".

	   Also see root=tmpfs above, for a method to combine a "tmpfs" file system with a regular /usr/ file system (as configured via mount.usr=). The main
	   distinction between systemd.volatile=yes, and root=tmpfs in combination mount.usr= is that the former operates on top of a regular root file system
	   and temporarily obstructs the files and directories above its /usr/ subdirectory, while the latter does not hide any files, but simply mounts a
	   unpopulated tmpfs as root file system and combines it with a user picked /usr/ file system.

	   Added in version 233.

       systemd.swap=
	   Takes a boolean argument or enables the option if specified without an argument. If disabled, causes the generator to ignore any swap devices
	   configured in /etc/fstab. Defaults to enabled.

	   Added in version 246.

       systemd.mount-extra=WHAT:WHERE[:FSTYPE[:OPTIONS]], rd.systemd.mount-extra=WHAT:WHERE[:FSTYPE[:OPTIONS]]
	   Specifies the mount unit. Takes at least two and at most four fields separated with a colon (":"). Each field is handled as the corresponding fstab
	   field. This option can be specified multiple times.	rd.systemd.mount-extra= is honored only in the initrd, while systemd.mount-extra= is honored
	   by both the main system and the initrd. In the initrd, the mount point (and also source path if the mount is bind mount) specified in
	   systemd.mount-extra= is prefixed with /sysroot/.

	   Example:

	       systemd.mount-extra=/dev/sda1:/mount-point:ext4:rw,noatime

	   Added in version 254.

       systemd.swap-extra=WHAT[:OPTIONS], rd.systemd.swap-extra=WHAT[:OPTIONS]
	   Specifies the swap unit. Takes the block device to be used as a swap device, and optionally takes mount options followed by a colon (":"). This
	   option can be specified multiple times.  rd.systemd.swap-extra= is honored only in the initrd, while systemd.swap-extra= is honored by both the
	   main system and the initrd.

	   Example:

	       systemd.swap-extra=/dev/sda2:x-systemd.makefs

	   Added in version 254.

SYSTEM CREDENTIALS
       fstab.extra
	   This credential may contain addition mounts to establish, in the same format as fstab(5), with one mount per line. It is read in addition to
	   /etc/fstab.

	   Added in version 254.

SEE ALSO
       systemd(1), fstab(5), systemd.mount(5), systemd.swap(5), systemd-cryptsetup-generator(8), systemd-gpt-auto-generator(8), kernel-command-line(7), Known
       Environment Variables[1]

NOTES
	1. Known Environment Variables
	   https://systemd.io/ENVIRONMENT/

systemd 255															    SYSTEMD-FSTAB-GENERATOR(8)
