SYSTEMD-VOLATILE-ROOT.SERVICE(8)				 systemd-volatile-root.service				      SYSTEMD-VOLATILE-ROOT.SERVICE(8)

NAME
       systemd-volatile-root.service, systemd-volatile-root - Make the root file system volatile

SYNOPSIS
       systemd-volatile-root.service

       /usr/lib/systemd/systemd-volatile-root

DESCRIPTION
       systemd-volatile-root.service is a service that replaces the root directory with a volatile memory file system ("tmpfs"), mounting the original
       (non-volatile) /usr/ inside it read-only. This way, vendor data from /usr/ is available as usual, but all configuration data in /etc/, all state data
       in /var/ and all other resources stored directly under the root directory are reset on boot and lost at shutdown, enabling fully stateless systems.

       This service is only enabled if full volatile mode is selected, for example by specifying "systemd.volatile=yes" on the kernel command line. This
       service runs only in the initrd, before the system transitions to the host's root directory. Note that this service is not used if
       "systemd.volatile=state" is used, as in that mode the root directory is non-volatile.

SEE ALSO
       systemd(1), systemd-fstab-generator(8), kernel-command-line(7)

systemd 255														      SYSTEMD-VOLATILE-ROOT.SERVICE(8)
