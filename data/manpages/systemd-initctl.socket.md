SYSTEMD-INITCTL.SERVICE(8)					    systemd-initctl.service					    SYSTEMD-INITCTL.SERVICE(8)

NAME
       systemd-initctl.service, systemd-initctl.socket, systemd-initctl - /dev/initctl compatibility

SYNOPSIS
       systemd-initctl.service

       systemd-initctl.socket

       /usr/lib/systemd/systemd-initctl

DESCRIPTION
       systemd-initctl is a system service that implements compatibility with the /dev/initctl FIFO file system object, as implemented by the SysV init
       system.	systemd-initctl is automatically activated on request and terminates itself when it is unused.

SEE ALSO
       systemd(1)

systemd 255															    SYSTEMD-INITCTL.SERVICE(8)
