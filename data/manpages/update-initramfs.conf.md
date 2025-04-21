UPDATE-INITRAMFS.CONF(5)					      File Formats Manual					      UPDATE-INITRAMFS.CONF(5)

NAME
       update-initramfs.conf - configuration file for update-initramfs

DESCRIPTION
       The configuration file allows one to disable the update action from update-initramfs.

GENERAL VARIABLES
	update_initramfs
	      Default  is  yes	for running the latest initramfs-tools hooks in the newest Linux image.	 Setting it to all updates any known initramfs.	 It is
	      possible to set it to no for remote servers or boxes where conservative manners needs to be applied. This disables the update_initramfs -u call.

	backup_initramfs
	      If set update_initramfs keeps an .bak file of the previous initramfs. If unset the backup initramfs will not be kept.

FILES
       /etc/initramfs-tools/update-initramfs.conf

AUTHOR
       The initramfs-tools are written by Maximilian Attems <maks@debian.org>, Jeff Bailey <jbailey@raspberryginger.com> and numerous others.

SEE ALSO
       initramfs.conf(5), initramfs-tools(7), mkinitramfs(8), update-initramfs(8).

initramfs-tools								  2010/04/05						      UPDATE-INITRAMFS.CONF(5)
