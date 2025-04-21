SYSTEMD-LOCALED.SERVICE(8)					    systemd-localed.service					    SYSTEMD-LOCALED.SERVICE(8)

NAME
       systemd-localed.service, systemd-localed - Locale bus mechanism

SYNOPSIS
       systemd-localed.service

       /usr/lib/systemd/systemd-localed

DESCRIPTION
       systemd-localed.service is a system service that may be used as mechanism to change the system locale settings, as well as the console key mapping and
       default X11 key mapping.	 systemd-localed is automatically activated on request and terminates itself when it is unused.

       The tool localectl(1) is a command line client to this service.

       See org.freedesktop.locale1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

SEE ALSO
       systemd(1), locale.conf(5), vconsole.conf(5), localectl(1), loadkeys(1)

systemd 255															    SYSTEMD-LOCALED.SERVICE(8)
