MKFS.BFS(8)							     System Administration							   MKFS.BFS(8)

NAME
       mkfs.bfs - make an SCO bfs filesystem

SYNOPSIS
       mkfs.bfs [options] device [block-count]

DESCRIPTION
       mkfs.bfs creates an SCO bfs filesystem on a block device (usually a disk partition or a file accessed via the loop device).

       The block-count parameter is the desired size of the filesystem, in blocks. If nothing is specified, the entire partition will be used.

OPTIONS
       -N, --inodes number
	   Specify the desired number of inodes (at most 512). If nothing is specified, some default number in the range 48-512 is picked depending on the
	   size of the partition.

       -V, --vname label
	   Specify the volume label. I have no idea if/where this is used.

       -F, --fname name
	   Specify the filesystem name. I have no idea if/where this is used.

       --lock[=mode]
	   Use exclusive BSD lock for device or file it operates. The optional argument mode can be yes, no (or 1 and 0) or nonblock. If the mode argument is
	   omitted, it defaults to yes. This option overwrites environment variable $LOCK_BLOCK_DEVICE. The default is not to use any lock at all, but it’s
	   recommended to avoid collisions with systemd-udevd(8) or other tools.

       -v, --verbose
	   Explain what is being done.

       -c
	   This option is silently ignored.

       -l
	   This option is silently ignored.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit. Option -V only works as --version when it is the only option.

EXIT STATUS
       The exit status returned by mkfs.bfs is 0 when all went well, and 1 when something went wrong.

SEE ALSO
       mkfs(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The mkfs.bfs command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								   MKFS.BFS(8)
