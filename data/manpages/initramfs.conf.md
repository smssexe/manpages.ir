INITRAMFS.CONF(5)						      File Formats Manual						     INITRAMFS.CONF(5)

NAME
       initramfs.conf - configuration file for mkinitramfs

DESCRIPTION
       The behaviour of mkinitramfs can be modified by its configuration file.

       Each  line  in  the file can be a configuration variable, a blank line, or a comment. The value of an variable is assigned by an statement of the form:
       name=[value]

       Configuration options can be broken out into configuration snippets and placed in individual files in the /etc/initramfs-tools/conf.d directory.	 Files
       in this directory are always read after the main configuration file, so you can override the settings in the main config file without  editing  it  di‐
       rectly.

GENERAL VARIABLES
	MODULES
	      Specifies the modules for the initramfs image.

	      Modules  listed  in /etc/initramfs-tools/modules and /usr/share/initramfs-tools/modules.d/* are always included in the initramfs, and are loaded
	      early in the boot process.

	      list doesn't load any additional modules at boot time, other than those listed in the above files.

	      most adds most file system, all ata, sata, scsi and usb drivers.

	      dep tries to guess which modules are necessary for the running box and only adds those modules.

	      netboot adds the base and network modules, but skips block devices.

	      The default setting is most.

	BUSYBOX
	      Include busybox utilities for the boot scripts.  If set to 'n' mkinitramfs will build an initramfs  without  busybox.   Beware  that  many  boot
	      scripts need busybox utilities.

	COMPRESS
	      Specifies	 the compression method used for the initramfs image.  mkinitramfs will default to gzip if the kernel lacks support (CONFIG_RD) or the
	      corresponding userspace utility is not present.

	COMPRESSLEVEL
	      Specifies the compression level used for the initramfs image.  mkinitramfs will default to 9 for lz4, 9 for zstd, and the builtin	 defaults  for
	      all others.

	UMASK Set the umask value of the generated initramfs file.  Useful to not disclose eventual keys.

	BOOT  Allows  one  to  use an nfs drive as the root of the drive.  The default is to boot from local media (hard drive, USB stick).  Set to nfs for an
	      NFS root share.

	RUNSIZE
	      The size of the /run tmpfs mount point in bytes (suffixes are supported) or as percentage of your physical RAM. This parameter is	 used  as  the
	      value of the size mount option to tmpfs. See https://www.kernel.org/doc/Documentation/filesystems/tmpfs.txt for details. Can be overridden by an
	      optional initramfs.runsize= bootarg.  The default is 10%.

VARIABLES FOR LOCAL BOOT
	RESUME
	      Specifies	 the device used for suspend-to-disk (hibernation), which the initramfs code should attempt to resume from.  If this is not defined or
	      is set to auto, mkinitramfs will automatically select the largest available swap partition.  Set it to none to disable resume from disk.

	FSTYPE
	      Specifies the filesystem type(s) to support, separated by commas.	 If this is not defined or is set to auto, mkinitramfs will automatically  de‐
	      tect the current root and /usr filesystem types.

VARIABLES FOR NFS BOOT
	DEVICE
	      Specifies the default network interface to use, like eth0.  The ip or BOOTIF bootargs may override this.

	VLAN  Specifies the VLAN tag id to setup, e.g. VLAN=eth0.1:eth0.  The vlan bootarg may override this.

	ROOT  Allows optional root bootarg hardcoding, when no root bootarg can be passed.  A root bootarg overrides that special setting.

	NFSROOT
	      Defaults to auto in order to pick up value from DHCP server.  Otherwise you need to specify HOST:MOUNT.

FILES
       /etc/initramfs-tools/initramfs.conf

AUTHOR
       The  initramfs-tools  are written by Maximilian Attems <maks@debian.org>, Jeff Bailey <jbailey@raspberryginger.com> and numerous others.	 Loosely based
       on mkinitrd.conf by Herbert Xu.

SEE ALSO
       initramfs-tools(7), mkinitramfs(8), update-initramfs(8).

initramfs-tools								  2018/07/18							     INITRAMFS.CONF(5)
