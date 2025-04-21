SYSTEMD-IMPORTD.SERVICE(8)					    systemd-importd.service					    SYSTEMD-IMPORTD.SERVICE(8)

NAME
       systemd-importd.service, systemd-importd - VM and container image import and export service

SYNOPSIS
       systemd-importd.service

       /usr/lib/systemd/systemd-importd

DESCRIPTION
       systemd-importd is a system service that allows importing, exporting and downloading of system images suitable for running as VM or containers. It is a
       companion service for systemd-machined.service(8), and provides the implementation for machinectl(1)'s pull-raw, pull-tar, import-raw, import-tar,
       import-fs, export-raw, and export-tar commands.

       See org.freedesktop.import1(5) and org.freedesktop.LogControl1(5) for a description of the D-Bus API.

SEE ALSO
       systemd(1), machinectl(1), systemd-machined.service(8), systemd-nspawn(1)

systemd 255															    SYSTEMD-IMPORTD.SERVICE(8)
