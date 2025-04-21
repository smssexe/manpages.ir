SYSTEMD-HOSTNAMED.SERVICE(8)					   systemd-hostnamed.service					  SYSTEMD-HOSTNAMED.SERVICE(8)

NAME
       systemd-hostnamed.service, systemd-hostnamed - Daemon to control system hostname from programs

SYNOPSIS
       systemd-hostnamed.service

       /usr/lib/systemd/systemd-hostnamed

DESCRIPTION
       systemd-hostnamed.service is a system service that may be used to change the system's hostname and related machine metadata from user programs. It is
       automatically activated on request and terminates itself when unused.

       It currently offers access to five variables:

       •   The current hostname (Example: "dhcp-192-168-47-11")

       •   The static (configured) hostname (Example: "lennarts-computer")

       •   The pretty hostname (Example: "Lennart's Computer")

       •   A suitable icon name for the local host (Example: "computer-laptop")

       •   A chassis type (Example: "tablet")

       The static hostname is stored in /etc/hostname, see hostname(5) for more information. The pretty hostname, chassis type, and icon name are stored in
       /etc/machine-info, see machine-info(5).

       The tool hostnamectl(1) is a command line client to this service.

       See org.freedesktop.hostname1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

SEE ALSO
       systemd(1), hostname(5), machine-info(5), hostnamectl(1), sethostname(2)

systemd 255															  SYSTEMD-HOSTNAMED.SERVICE(8)
