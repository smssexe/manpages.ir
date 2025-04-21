MKFS.CRAMFS(8)							     System Administration							MKFS.CRAMFS(8)

NAME
       mkfs.cramfs - make compressed ROM file system

SYNOPSIS
       mkfs.cramfs [options] directory file

DESCRIPTION
       Files on cramfs file systems are zlib-compressed one page at a time to allow random read access. The metadata is not compressed, but is expressed in a
       terse representation that is more space-efficient than conventional file systems.

       The file system is intentionally read-only to simplify its design; random write access for compressed files is difficult to implement. cramfs ships
       with a utility (mkcramfs(8)) to pack files into new cramfs images.

       File sizes are limited to less than 16 MB.

       Maximum file system size is a little under 272 MB. (The last file on the file system must begin before the 256 MB block, but can extend past it.)

ARGUMENTS
       The directory is simply the root of the directory tree that we want to generate a compressed filesystem out of.

       The file will contain the cram file system, which later can be mounted.

OPTIONS
       -v
	   Enable verbose messaging.

       -E
	   Treat all warnings as errors, which are reflected as command exit status.

       -b blocksize
	   Use defined block size, which has to be divisible by page size.

       -e edition
	   Use defined file system edition number in superblock.

       -N big, little, host
	   Use defined endianness. Value defaults to host.

       -i file
	   Insert a file to cramfs file system.

       -n name
	   Set name of the cramfs file system.

       -p
	   Pad by 512 bytes for boot code.

       -s
	   This option is ignored. Originally the -s turned on directory entry sorting.

       -z
	   Make explicit holes.

       -l[=mode]
	   Use exclusive BSD lock for device or file it operates. The optional argument mode can be yes, no (or 1 and 0) or nonblock. If the mode argument is
	   omitted, it defaults to "yes". This option overwrites environment variable $LOCK_BLOCK_DEVICE. The default is not to use any lock at all, but it’s
	   recommended to avoid collisions with udevd or other tools.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       0
	   success

       8
	   operation error, such as unable to allocate memory

SEE ALSO
       fsck.cramfs(8), mount(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The mkfs.cramfs command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								MKFS.CRAMFS(8)
