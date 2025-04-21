E2MMPSTATUS(8)							    System Manager's Manual							E2MMPSTATUS(8)

NAME
       e2mmpstatus - Check MMP status of an ext4 file system

SYNOPSIS
       e2mmpstatus [-i] <filesystem>

OPTIONS
       -i     prints out the MMP information rather than check it.

DESCRIPTION
       e2mmpstatus is used to check Multiple-Mount Protection (MMP) status of an ext4 file system with the mmp feature enabled.	 The specified file system can
       be  a  device  name  (e.g.   /dev/hdc1,	/dev/sdb2), or an ext4 file system label or UUID, for example UUID=8868abf6-88c5-4a83-98b8-bfc24057f7bd or LA‐
       BEL=root.  By default, the e2mmpstatus program checks whether it is safe to mount the file system without taking the risk  of  mounting	it  more  than
       once.

       MMP  (multiple-mount  protection) is a feature that adds protection against the file system being modified simultaneously by more than one node.	 It is
       NOT safe to mount a file system when one of the following conditions is true:
	    1. e2fsck is running on the file system.
	    2. the file system is in use by another node.
	    3. The MMP block is corrupted or cannot be read for some reason.
       The e2mmpstatus program might wait for some time to see whether the MMP block is being updated by any node during this period.  The time taken  depends
       on how frequently the MMP block is being written by the other node.

EXIT CODE
       The  exit  code	returned by e2mmpstatus is 0 when it is safe to mount the file system, 1 when the MMP block shows the file system is in use on another
       node and it is NOT safe to mount the file system, and 2 if some other failure occurred that prevents the check from properly detecting the current  MMP
       status.

SEE ALSO
       dumpe2fs(8), e2fsck(8), fstab(5), fsck(8),

E2fsprogs version 1.47.0						 February 2023								E2MMPSTATUS(8)
