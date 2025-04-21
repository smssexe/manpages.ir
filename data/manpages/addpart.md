ADDPART(8)							     System Administration							    ADDPART(8)

NAME
       addpart - tell the kernel about the existence of a partition

SYNOPSIS
       addpart device partition start length

DESCRIPTION
       addpart tells the Linux kernel about the existence of the specified partition. The command is a simple wrapper around the "add partition" ioctl.

       This command doesn’t manipulate partitions on a block device.

PARAMETERS
       device
	   The disk device.

       partition
	   The partition number.

       start
	   The beginning of the partition (in 512-byte sectors).

       length
	   The length of the partition (in 512-byte sectors).

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

SEE ALSO
       delpart(8), fdisk(8), parted(8), partprobe(8), partx(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The addpart command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								    ADDPART(8)
