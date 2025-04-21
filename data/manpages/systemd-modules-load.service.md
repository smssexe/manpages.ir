SYSTEMD-MODULES-LOAD.SERVICE(8)					 systemd-modules-load.service				       SYSTEMD-MODULES-LOAD.SERVICE(8)

NAME
       systemd-modules-load.service, systemd-modules-load - Load kernel modules at boot

SYNOPSIS
       systemd-modules-load.service

       /usr/lib/systemd/systemd-modules-load

DESCRIPTION
       systemd-modules-load.service is an early boot service that loads kernel modules. It reads static configuration from files in /usr/ and /etc/, but also
       runtime configuration from /run/ and the kernel command line (see below).

       See modules-load.d(5) for information about the configuration format of this service and paths where configuration files can be created.

KERNEL COMMAND LINE
       systemd-modules-load.service understands the following kernel command line parameters:

       modules_load=, rd.modules_load=
	   Takes a comma-separated list of kernel modules to statically load during early boot. The option prefixed with "rd."	is read in the initrd only.

	   Added in version 187.

SEE ALSO
       systemd(1), modules-load.d(5),

systemd 255														       SYSTEMD-MODULES-LOAD.SERVICE(8)
