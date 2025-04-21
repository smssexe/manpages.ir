SWAPLABEL(8)							     System Administration							  SWAPLABEL(8)

NAME
       swaplabel - print or change the label or UUID of a swap area

SYNOPSIS
       swaplabel [-L label] [-U UUID] device

DESCRIPTION
       swaplabel will display or change the label or UUID of a swap partition located on device (or regular file).

       If the optional arguments -L and -U are not given, swaplabel will simply display the current swap-area label and UUID of device.

       If an optional argument is present, then swaplabel will change the appropriate value on device. These values can also be set during swap creation using
       mkswap(8). The swaplabel utility allows changing the label or UUID on an actively used swap device.

OPTIONS
       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

       -L, --label label
	   Specify a new label for the device. Swap partition labels can be at most 16 characters long. If label is longer than 16 characters, swaplabel will
	   truncate it and print a warning message.

       -U, --uuid UUID
	   Specify a new UUID for the device. The UUID must be in the standard 8-4-4-4-12 character format, such as is output by uuidgen(1).

ENVIRONMENT
       LIBBLKID_DEBUG=all
	   enables libblkid debug output.

AUTHORS
       swaplabel was written by Jason Borden <jborden@bluehost.com> and Karel Zak <kzak@redhat.com>.

SEE ALSO
       uuidgen(1), mkswap(8), swapon(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The swaplabel command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								  SWAPLABEL(8)
