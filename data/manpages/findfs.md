FINDFS(8)							     System Administration							     FINDFS(8)

NAME
       findfs - find a filesystem by label or UUID

SYNOPSIS
       findfs NAME=value

DESCRIPTION
       findfs will search the block devices in the system looking for a filesystem or partition with specified tag. The currently supported tags are:

       LABEL=<label>
	   Specifies filesystem label.

       UUID=<uuid>
	   Specifies filesystem UUID.

       PARTUUID=<uuid>
	   Specifies partition UUID. This partition identifier is supported for example for GUID Partition Table (GPT) partition tables.

       PARTLABEL=<label>
	   Specifies partition label (name). The partition labels are supported for example for GUID Partition Table (GPT) or MAC partition tables.

       If the filesystem or partition is found, the device name will be printed on stdout.

       The complete overview about filesystems and partitions you can get for example by

	  lsblk --fs

	  partx --show <disk>

	  blkid

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       0
	   success

       1
	   label or uuid cannot be found

       2
	   usage error, wrong number of arguments or unknown option

ENVIRONMENT
       LIBBLKID_DEBUG=all
	   enables libblkid debug output.

AUTHORS
       findfs was originally written by Theodore Ts’o <tytso@mit.edu> and re-written for the util-linux package by Karel Zak <kzak@redhat.com>.

SEE ALSO
       blkid(8), lsblk(8), partx(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The findfs command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								     FINDFS(8)
