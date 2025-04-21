SYSTEMD-RFKILL.SERVICE(8)					    systemd-rfkill.service					     SYSTEMD-RFKILL.SERVICE(8)

NAME
       systemd-rfkill.service, systemd-rfkill.socket, systemd-rfkill - Load and save the RF kill switch state at boot and change

SYNOPSIS
       systemd-rfkill.service

       systemd-rfkill.socket

       /usr/lib/systemd/systemd-rfkill

DESCRIPTION
       systemd-rfkill.service is a service that restores the RF kill switch state at early boot and saves it on each change. On disk, the RF kill switch state
       is stored in /var/lib/systemd/rfkill/.

KERNEL COMMAND LINE
       systemd-rfkill understands the following kernel command line parameter:

       systemd.restore_state=
	   Takes a boolean argument. Defaults to "1". If "0", does not restore the rfkill settings on boot. However, settings will still be stored on
	   shutdown.

	   Added in version 227.

SEE ALSO
       systemd(1)

systemd 255															     SYSTEMD-RFKILL.SERVICE(8)
