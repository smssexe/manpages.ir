MKFS.MINIX(8)							     System Administration							 MKFS.MINIX(8)

NAME
       mkfs.minix - make a Minix filesystem

SYNOPSIS
       mkfs.minix [options] device [size-in-blocks]

DESCRIPTION
       mkfs.minix creates a Linux MINIX filesystem on a device (usually a disk partition).

       The device is usually of the following form:

	   /dev/hda[1-8] (IDE disk 1)
	   /dev/hdb[1-8] (IDE disk 2)
	   /dev/sda[1-8] (SCSI disk 1)
	   /dev/sdb[1-8] (SCSI disk 2)

       The device may be a block device or an image file of one, but this is not enforced. Expect not much fun on a character device :-).

       The size-in-blocks parameter is the desired size of the file system, in blocks. It is present only for backwards compatibility. If omitted the size
       will be determined automatically. Only block counts strictly greater than 10 and strictly less than 65536 are allowed.

OPTIONS
       -c, --check
	   Check the device for bad blocks before creating the filesystem. If any are found, the count is printed.

       -n, --namelength length
	   Specify the maximum length of filenames. Currently, the only allowable values are 14 and 30 for file system versions 1 and 2. Version 3 allows only
	   value 60. The default is 30.

       --lock[=mode]
	   Use exclusive BSD lock for device or file it operates. The optional argument mode can be yes, no (or 1 and 0) or nonblock. If the mode argument is
	   omitted, it defaults to yes. This option overwrites environment variable $LOCK_BLOCK_DEVICE. The default is not to use any lock at all, but it’s
	   recommended to avoid collisions with systemd-udevd(8) or other tools.

       -i, --inodes number
	   Specify the number of inodes for the filesystem.

       -l, --badblocks filename
	   Read the list of bad blocks from filename. The file has one bad-block number per line. The count of bad blocks read is printed.

       -1
	   Make a Minix version 1 filesystem. This is the default.

       -2, -v
	   Make a Minix version 2 filesystem.

       -3
	   Make a Minix version 3 filesystem.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit. The long option cannot be combined with other options.

ENVIRONMENT
       LOCK_BLOCK_DEVICE=<mode>
	   use exclusive BSD lock. The mode is "1" or "0". See --lock for more details.

EXIT STATUS
       The exit status returned by mkfs.minix is one of the following:

       0
	   No errors

       8
	   Operational error

       16
	   Usage or syntax error

SEE ALSO
       fsck(8), mkfs(8), reboot(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The mkfs.minix command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								 MKFS.MINIX(8)
