DELPART(8)							     System Administration							    DELPART(8)

NAME
       delpart - tell the kernel to forget about a partition

SYNOPSIS
       delpart device partition

DESCRIPTION
       delpart asks the Linux kernel to forget about the specified partition (a number) on the specified device. The command is a simple wrapper around the
       "del partition" ioctl.

       This command doesn’t manipulate partitions on a block device.

OPTIONS
       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

SEE ALSO
       addpart(8), fdisk(8), parted(8), partprobe(8), partx(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The delpart command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								    DELPART(8)
