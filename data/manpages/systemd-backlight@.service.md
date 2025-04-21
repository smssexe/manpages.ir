SYSTEMD-BACKLIGHT@.SERVICE(8)					  systemd-backlight@.service					 SYSTEMD-BACKLIGHT@.SERVICE(8)

NAME
       systemd-backlight@.service, systemd-backlight - Load and save the display backlight brightness at boot and shutdown

SYNOPSIS
       systemd-backlight@.service

       /usr/lib/systemd/systemd-backlight save [backlight|leds]:DEVICE

       /usr/lib/systemd/systemd-backlight load [backlight|leds]:DEVICE

DESCRIPTION
       systemd-backlight@.service is a service that restores the display backlight brightness at early boot and saves it at shutdown. On disk, the backlight
       brightness is stored in /var/lib/systemd/backlight/. During loading, if the udev property ID_BACKLIGHT_CLAMP is not set to false, the brightness is
       clamped to a value of at least 1 or 5% of maximum brightness, whichever is greater. The percentage can be adjusted by specifying a percentage (needs to
       be suffixed with "%", e.g.  "30%") to the property ID_BACKLIGHT_CLAMP.

KERNEL COMMAND LINE
       systemd-backlight understands the following kernel command line parameter:

       systemd.restore_state=
	   Takes a boolean argument. Defaults to "1". If "0", does not restore the backlight settings on boot. However, settings will still be stored on
	   shutdown.

	   Added in version 209.

SEE ALSO
       systemd(1)

systemd 255															 SYSTEMD-BACKLIGHT@.SERVICE(8)
