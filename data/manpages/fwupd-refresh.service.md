fwupd-refresh.service(5)					Message Of The Day Integration					      fwupd-refresh.service(5)

NAME
       fwupd-refresh.service — message of the day integration.

DESCRIPTION
       Message on the day integration is used to display the availability of updates when connecting to a remote console.

       It has two elements:

       • Automatic firmware metadata refresh

       • Message of the day display

       This uses a systemd timer to run on a regular cadence. To enable this, run:

	 systemctl enable fwupd-refresh.timer

NOTES
       Motd display is dependent upon the availability of the update-motd snippet consumption service such as pam_motd.

       To enable a proxy, set the systemd global environment in /etc/systemd/system.conf so all the systemd child processes have the proxy settings applied:

       [Manager]
       DefaultEnvironment=http_proxy=“http://internal.corp:3128/ ”https_proxy=“http://internal.corp:3128/”

SEE ALSO
       <fwupdmgr(1)> <fwupd.conf(5)>

1.9.28																      fwupd-refresh.service(5)
