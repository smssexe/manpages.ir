SYSTEMD-MAKEFS@.SERVICE(8)					    systemd-makefs@.service					    SYSTEMD-MAKEFS@.SERVICE(8)

NAME
       systemd-makefs@.service, systemd-mkswap@.service, systemd-growfs@.service, systemd-growfs-root.service, systemd-makefs, systemd-growfs - Creating and
       growing file systems on demand

SYNOPSIS
       systemd-makefs@device.service

       systemd-mkswap@device.service

       systemd-growfs@mountpoint.service

       systemd-growfs-root.service

       /usr/lib/systemd/systemd-makefs

       /usr/lib/systemd/systemd-growfs

DESCRIPTION
       systemd-makefs@.service, systemd-mkswap@.service, systemd-growfs@.service, and systemd-growfs-root.service are used to implement the x-systemd.makefs
       and x-systemd.growfs options in fstab(5), see systemd.mount(5). They are instantiated for each device for which the file system or swap structure needs
       to be initialized, and for each mount point where the file system needs to be grown.

       These services are started at boot, either right before or right after the mount point or swap device are used.

       systemd-makefs knows very little about specific file systems and swap devices, and after checking that the block device does not already contain a file
       system or other content, it will execute binaries specific to each filesystem type (/sbin/mkfs.type or /sbin/mkswap). For certain file system types
       (currently ext2/ext3/ext4(5), btrfs(5), xfs(5), f2fs, vfat) and for swap devices, it will configure reasonable defaults and set the file system label
       and UUID based on the device name.

       systemd-growfs knows very little about specific file systems and swap devices, and will instruct the kernel to grow the mounted filesystem to full size
       of the underlying block device. Nevertheless, it needs to know the ioctl(2) number specific to each file system, so only certain types are supported.
       Currently: ext4(5), btrfs(5), xfs(5), and dm-crypt partitions (see cryptsetup(8)).

       If the creation of a file system or swap device fails, the mount point or swap is failed too. If the growing of a file system fails, a warning is
       emitted.

SEE ALSO
       systemd(1), systemd.mount(8), systemd-fstab-generator(8), systemd-repart(8), mkfs.btrfs(8), mkfs.cramfs(8), mkfs.ext4(8), mkfs.fat(8), mkfs.hfsplus(8),
       mkfs.minix(8), mkfs.ntfs(8), mkfs.xfs(8)

systemd 255															    SYSTEMD-MAKEFS@.SERVICE(8)
