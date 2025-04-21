SYSTEMD-UPDATE-UTMP.SERVICE(8)					  systemd-update-utmp.service					SYSTEMD-UPDATE-UTMP.SERVICE(8)

NAME
       systemd-update-utmp.service, systemd-update-utmp-runlevel.service, systemd-update-utmp - Write audit and utmp updates at bootup, runlevel changes and
       shutdown

SYNOPSIS
       systemd-update-utmp.service

       systemd-update-utmp-runlevel.service

       /usr/lib/systemd/systemd-update-utmp

DESCRIPTION
       systemd-update-utmp-runlevel.service is a service that writes SysV runlevel changes to utmp and wtmp, as well as the audit logs, as they occur.
       systemd-update-utmp.service does the same for system reboots and shutdown requests.

SEE ALSO
       systemd(1), utmp(5), auditd(8)

systemd 255															SYSTEMD-UPDATE-UTMP.SERVICE(8)
