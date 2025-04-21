SYSTEMD-VERITYSETUP@.SERVICE(8)					 systemd-veritysetup@.service				       SYSTEMD-VERITYSETUP@.SERVICE(8)

NAME
       systemd-veritysetup@.service, systemd-veritysetup - Disk verity protection logic

SYNOPSIS
       systemd-veritysetup@.service

       /usr/lib/systemd/systemd-veritysetup

DESCRIPTION
       systemd-veritysetup@.service is a service responsible for setting up verity protection block devices. It should be instantiated for each device that
       requires verity protection.

       At early boot and when the system manager configuration is reloaded kernel command line configuration for verity protected block devices is translated
       into systemd-veritysetup@.service units by systemd-veritysetup-generator(8).

       systemd-veritysetup@.service calls systemd-veritysetup.

COMMANDS
       The following commands are understood by systemd-veritysetup:

       attach volume datadevice hashdevice roothash [option...]
	   Create a block device volume using datadevice and hashdevice as the backing devices.	 roothash forms the root of the tree of hashes stored on
	   hashdevice. See Kernel dm-verity[1] documentation for details.

	   Added in version 250.

       detach volume
	   Detach (destroy) the block device volume.

	   Added in version 250.

       help
	   Print short information about command syntax.

	   Added in version 250.

SEE ALSO
       systemd(1), systemd-veritysetup-generator(8), veritysetup(8)

NOTES
	1. Kernel dm-verity
	   https://docs.kernel.org/admin-guide/device-mapper/verity.html

systemd 255														       SYSTEMD-VERITYSETUP@.SERVICE(8)
