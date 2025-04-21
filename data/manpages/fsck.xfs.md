fsck.xfs(8)							    System Manager's Manual							   fsck.xfs(8)

NAME
       fsck.xfs - do nothing, successfully

SYNOPSIS
       fsck.xfs [ filesys ... ]

DESCRIPTION
       fsck.xfs	 is called by the generic Linux fsck(8) program at startup to check and repair an XFS filesystem.  XFS is a journaling filesystem and performs
       recovery at mount(8) time if necessary, so fsck.xfs simply exits with a zero exit status.

       If you wish to check the consistency of an XFS filesystem, or repair a damaged or corrupt XFS filesystem, see xfs_repair(8).

       However, the system administrator can force fsck.xfs to run xfs_repair(8) at boot time by creating  a  /forcefsck  file	or  booting  the  system  with
       "fsck.mode=force" on the kernel command line.

FILES
       /etc/fstab.

SEE ALSO
       fsck(8), fstab(5), xfs(5), xfs_repair(8).

																		   fsck.xfs(8)
