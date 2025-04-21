SYSTEMD-UDEV-SETTLE.SERVICE(8)					  systemd-udev-settle.service					SYSTEMD-UDEV-SETTLE.SERVICE(8)

NAME
       systemd-udev-settle.service - Wait for all pending udev events to be handled

SYNOPSIS
       systemd-udev-settle.service

DESCRIPTION
       This service calls udevadm settle to wait until all events that have been queued by udev(7) have been processed. It is a crude way to wait until "all"
       hardware has been discovered. Services may pull in this service and order themselves after it to wait for the udev queue to be empty.

       Using this service is not recommended.  There can be no guarantee that hardware is fully discovered at any specific time, because the kernel does
       hardware detection asynchronously, and certain buses and devices take a very long time to become ready, and also additional hardware may be plugged in
       at any time. Instead, services should subscribe to udev events and react to any new hardware as it is discovered. Services that, based on
       configuration, expect certain devices to appear, may warn or report failure after a timeout. This timeout should be tailored to the hardware type.
       Waiting for systemd-udev-settle.service usually slows boot significantly, because it means waiting for all unrelated events too.

SEE ALSO
       udev(7), udevadm(8)

systemd 255															SYSTEMD-UDEV-SETTLE.SERVICE(8)
