SWAPON(8)							     System Administration							     SWAPON(8)

NAME
       swapon, swapoff - enable/disable devices and files for paging and swapping

SYNOPSIS
       swapon [options] [specialfile...]

       swapoff [-va] [specialfile...]

DESCRIPTION
       swapon is used to specify devices on which paging and swapping are to take place.

       The device or file used is given by the specialfile parameter. It may be of the form -L label or -U uuid to indicate a device by label or uuid.

       Calls to swapon normally occur in the system boot scripts making all swap devices available, so that the paging and swapping activity is interleaved
       across several devices and files.

       swapoff disables swapping on the specified devices and files. When the -a flag is given, swapping is disabled on all known swap devices and files (as
       found in /proc/swaps or /etc/fstab).

OPTIONS
       -a, --all
	   All devices marked as "swap" in /etc/fstab are made available, except for those with the "noauto" option. Devices that are already being used as
	   swap are silently skipped.

       -T, --fstab path
	   Specifies an alternative fstab file for compatibility with mount(8). If path is a directory, then the files in the directory are sorted by
	   strverscmp(3); files that start with "." or without an .fstab extension are ignored. The option can be specified more than once. This option is
	   mostly designed for initramfs or chroot scripts where additional configuration is specified beyond standard system configuration.

       -d, --discard[=policy]
	   Enable swap discards, if the swap backing device supports the discard or trim operation. This may improve performance on some Solid State Devices,
	   but often it does not. The option allows one to select between two available swap discard policies:

	   --discard=once
	       to perform a single-time discard operation for the whole swap area at swapon; or

	   --discard=pages
	       to asynchronously discard freed swap pages before they are available for reuse.

	   If no policy is selected, the default behavior is to enable both discard types. The /etc/fstab mount options discard, discard=once, or
	   discard=pages may also be used to enable discard flags.

       -e, --ifexists
	   Silently skip devices that do not exist. The /etc/fstab mount option nofail may also be used to skip non-existing device.

       -f, --fixpgsz
	   Reinitialize (exec mkswap) the swap space if its page size does not match that of the current running kernel. mkswap(8) initializes the whole
	   device and does not check for bad blocks.

       -L label
	   Use the partition that has the specified label. (For this, access to /proc/partitions is needed.)

       -o, --options opts
	   Specify swap options by an fstab-compatible comma-separated string. For example:

	   swapon -o pri=1,discard=pages,nofail /dev/sda2

	   The opts string is evaluated last and overrides all other command line options.

       -p, --priority priority
	   Specify the priority of the swap device. priority is a value between -1 and 32767. Higher numbers indicate higher priority. See swapon(2) for a
	   full description of swap priorities. Add pri=value to the option field of /etc/fstab for use with swapon -a. When no priority is defined, it
	   defaults to -1.

       -s, --summary
	   Display swap usage summary by device. Equivalent to cat /proc/swaps. This output format is DEPRECATED in favour of --show that provides better
	   control on output data.

       --show[=column...]
	   Display a definable table of swap areas. See the --help output for a list of available columns.

       --output-all
	   Output all available columns.

       --noheadings
	   Do not print headings when displaying --show output.

       --raw
	   Display --show output without aligning table columns.

       --bytes
	   Display swap size in bytes in --show output instead of in user-friendly units.

       -U uuid
	   Use the partition that has the specified uuid.

       -v, --verbose
	   Be verbose.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       swapoff has the following exit status values since v2.36:

       0
	   success

       2
	   system has insufficient memory to stop swapping (OOM)

       4
	   swapoff(2) syscall failed for another reason

       8
	   non-swapoff(2) syscall system error (out of memory, ...)

       16
	   usage or syntax error

       32
	   all swapoff failed on --all

       64
	   some swapoff succeeded on --all

       The command swapoff --all returns 0 (all succeeded), 32 (all failed), or 64 (some failed, some succeeded).

       + The old versions before v2.36 has no documented exit status, 0 means success in all versions.

ENVIRONMENT
       LIBMOUNT_DEBUG=all
	   enables libmount debug output.

       LIBBLKID_DEBUG=all
	   enables libblkid debug output.

FILES
       /dev/sd??
	   standard paging devices

       /etc/fstab
	   ascii filesystem description table

NOTES
   Files with holes
       The swap file implementation in the kernel expects to be able to write to the file directly, without the assistance of the filesystem. This is a
       problem on files with holes or on copy-on-write files on filesystems like Btrfs.

       Commands like cp(1) or truncate(1) create files with holes. These files will be rejected by swapon.

       Preallocated files created by fallocate(1) may be interpreted as files with holes too depending of the filesystem. Preallocated swap files are
       supported on XFS since Linux 4.18.

       The most portable solution to create a swap file is to use dd(1) and /dev/zero.

   Btrfs
       Swap files on Btrfs are supported since Linux 5.0 on files with nocow attribute. See the btrfs(5) manual page for more details.

   NFS
       Swap over NFS may not work.

   Suspend
       swapon automatically detects and rewrites a swap space signature with old software suspend data (e.g., S1SUSPEND, S2SUSPEND, ...). The problem is that
       if we don’t do it, then we get data corruption the next time an attempt at unsuspending is made.

HISTORY
       The swapon command appeared in 4.0BSD.

SEE ALSO
       swapoff(2), swapon(2), fstab(5), init(8), fallocate(1), mkswap(8), mount(8), rc(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The swapon command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-12-01								     SWAPON(8)
