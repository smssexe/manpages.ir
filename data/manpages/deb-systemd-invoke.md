DEB-SYSTEMD-INVOKE(1p)						      init-system-helpers						DEB-SYSTEMD-INVOKE(1p)

NAME
       deb-systemd-invoke - wrapper around systemctl, respecting policy-rc.d

SYNOPSIS
       deb-systemd-invoke [--user] start|stop|restart unit file ...  deb-systemd-invoke [--user] [--no-dbus] daemon-reload|daemon-reexec

DESCRIPTION
       deb-systemd-invoke is a Debian-specific helper script which asks /usr/sbin/policy-rc.d before performing a systemctl call.

       deb-systemd-invoke is intended to be used from maintscripts to manage systemd unit files. It is specifically NOT intended to be used interactively by
       users. Instead, users should run systemd and use systemctl, or not bother about the systemd enabled state in case they are not running systemd.

1.66ubuntu1								  2023-12-06							DEB-SYSTEMD-INVOKE(1p)
