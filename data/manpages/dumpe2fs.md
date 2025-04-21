DUMPE2FS(8)							    System Manager's Manual							   DUMPE2FS(8)

NAME
       dumpe2fs - dump ext2/ext3/ext4 file system information

SYNOPSIS
       dumpe2fs [ -bfghixV ] [ -o superblock=superblock ] [ -o blocksize=blocksize ] device

DESCRIPTION
       dumpe2fs prints the super block and blocks group information for the file system present on device.

       Note: When used with a mounted file system, the printed information may be old or inconsistent.

OPTIONS
       -b     print the blocks which are reserved as bad in the file system.

       -o superblock=superblock
	      use  the block superblock when examining the file system.	 This option is not usually needed except by a file system wizard who is examining the
	      remains of a very badly corrupted file system.

       -o blocksize=blocksize
	      use blocks of blocksize bytes when examining the file system.  This option is not usually needed except by a file system wizard who is examining
	      the remains of a very badly corrupted file system.

       -f     force dumpe2fs to display a file system even though it may have some file system feature flags which dumpe2fs may not understand (and which  can
	      cause some of dumpe2fs's display to be suspect).

       -g     display  the  group  descriptor  information in a machine readable colon-separated value format.	The fields displayed are the group number; the
	      number of the first block in the group; the superblock location (or -1 if not present); the range of blocks used by the group descriptors (or -1
	      if not present); the block bitmap location; the inode bitmap location; and the range of blocks used by the inode table.

       -h     only display the superblock information and not any of the block group descriptor detail information.

       -i     display the file system data from an image file created by e2image, using device as the pathname to the image file.

       -m     If the mmp feature is enabled on the file system, check if device is in use by another node, see e2mmpstatus(8) for full details.	 If  used  to‐
	      gether with the -i option, only the MMP block information is printed.

       -x     print the detailed group information block numbers in hexadecimal format

       -V     print the version number of dumpe2fs and exit.

EXIT CODE
       dumpe2fs	 exits	with  a return code of 0 if the operation completed without errors.  It will exit with a non-zero return code if there are any errors,
       such as problems reading a valid superblock, bad checksums, or if the device is in use by another node and -m is specified.

BUGS
       You may need to know the physical file system structure to understand the output.

AUTHOR
       dumpe2fs was written by Remy Card <Remy.Card@linux.org>.	 It is currently being maintained by Theodore Ts'o <tytso@alum.mit.edu>.

AVAILABILITY
       dumpe2fs is part of the e2fsprogs package and is available from http://e2fsprogs.sourceforge.net.

SEE ALSO
       e2fsck(8), e2mmpstatus(8), mke2fs(8), tune2fs(8).  ext4(5)

E2fsprogs version 1.47.0						 February 2023								   DUMPE2FS(8)
