FILEFRAG(8)							    System Manager's Manual							   FILEFRAG(8)

NAME
       filefrag - report on file fragmentation

SYNOPSIS
       filefrag [ -bblocksize ] [ -BeEkPsvVxX ] [ files...  ]

DESCRIPTION
       filefrag	 reports  on how badly fragmented a particular file might be.  It makes allowances for indirect blocks for ext2 and ext3 file systems, but can
       be used on files for any file system.

       The filefrag program initially attempts to get the extent information using FIEMAP ioctl which is more efficient and faster.  If	 FIEMAP	 is  not  sup‐
       ported then filefrag will fall back to using FIBMAP.

OPTIONS
       -B     Force the use of the older FIBMAP ioctl instead of the FIEMAP ioctl for testing purposes.

       -bblocksize
	      Use  blocksize  in  bytes, or with [KMG] suffix, up to 1GB for output instead of the file system blocksize.  For compatibility with earlier ver‐
	      sions of filefrag, if blocksize is unspecified it defaults to 1024 bytes.	 Since blocksize is an optional argument, it must be added without any
	      space after -b.

       -e     Print output in extent format, even for block-mapped files.

       -E     Display the contents of ext4's extent status cache.  This feature is not supported on all kernels, and is only supported on ext4 file systems.

       -k     Use 1024-byte blocksize for output (identical to '-b1024').

       -P     Pre-load the ext4 extent status cache for the file.  This is not supported on all kernels, and is only supported on ext4 file systems.

       -s     Sync the file before requesting the mapping.

       -v     Be verbose when checking for file fragmentation.

       -V     Print version number of program and library.  If given twice, also print the FIEMAP flags that are understood by the current version.

       -x     Display mapping of extended attributes.

       -X     Display extent block numbers in hexadecimal format.

AUTHOR
       filefrag was written by Theodore Ts'o <tytso@mit.edu>.

E2fsprogs version 1.47.0						 February 2023								   FILEFRAG(8)
