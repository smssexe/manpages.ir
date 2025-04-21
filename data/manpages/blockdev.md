BLOCKDEV(8)							     System Administration							   BLOCKDEV(8)

NAME
       blockdev - call block device ioctls from the command line

SYNOPSIS
       blockdev [-q] [-v] command [command...] device [device...]

       blockdev --report [device...]

       blockdev -h|-V

DESCRIPTION
       The utility blockdev allows one to call block device ioctls from the command line.

OPTIONS
       -q
	   Be quiet.

       -v
	   Be verbose.

       --report
	   Print a report for the specified device. It is possible to give multiple devices. If none is given, all devices which appear in /proc/partitions
	   are shown. Note that the partition StartSec is in 512-byte sectors.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

COMMANDS
       It is possible to give multiple devices and multiple commands.

       --flushbufs
	   Flush buffers.

       --getalignoff
	   Get alignment offset.

       --getbsz
	   Print the blocksize in bytes. This size does not describe device topology. It’s the size used internally by the kernel and it may be modified (for
	   example) by filesystem driver on mount.

       --getdiscardzeroes
	   Get discard zeroes support status.

       --getdiskseq
	   Get disk sequence number.

       --getfra
	   Get filesystem readahead in 512-byte sectors.

       --getiomin
	   Get minimum I/O size.

       --getioopt
	   Get optimal I/O size.

       --getmaxsect
	   Get max sectors per request.

       --getpbsz
	   Get physical block (sector) size.

       --getra
	   Print readahead (in 512-byte sectors).

       --getro
	   Get read-only. Print 1 if the device is read-only, 0 otherwise.

       --getsize64
	   Print device size in bytes.

       --getsize
	   Print device size (32-bit!) in sectors. Deprecated in favor of the --getsz option.

       --getss
	   Print logical sector size in bytes - usually 512.

       --getsz
	   Get size in 512-byte sectors.

       --rereadpt
	   Reread partition table

       --setbsz bytes
	   Set blocksize. Note that the block size is specific to the current file descriptor opening the block device, so the change of block size only
	   persists for as long as blockdev has the device open, and is lost once blockdev exits.

       --setfra sectors
	   Set filesystem readahead (same as --setra on 2.6 kernels).

       --setra sectors
	   Set readahead (in 512-byte sectors).

       --setro
	   Set read-only. The currently active access to the device may not be affected by the change. For example, a filesystem already mounted in read-write
	   mode will not be affected. The change applies after remount.

       --setrw
	   Set read-write.

AUTHORS
       blockdev was written by Andries E. Brouwer and rewritten by Karel Zak.

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The blockdev command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-12-01								   BLOCKDEV(8)
