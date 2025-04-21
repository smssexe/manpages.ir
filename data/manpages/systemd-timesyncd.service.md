SYSTEMD-TIMESYNCD.SERVICE(8)					   systemd-timesyncd.service					  SYSTEMD-TIMESYNCD.SERVICE(8)

NAME
       systemd-timesyncd.service, systemd-timesyncd - Network Time Synchronization

SYNOPSIS
       systemd-timesyncd.service

       /usr/lib/systemd/systemd-timesyncd

DESCRIPTION
       systemd-timesyncd is a system service that may be used to synchronize the local system clock with a remote Network Time Protocol (NTP) server. It also
       saves the local time to disk every time the clock has been synchronized and uses this to possibly advance the system realtime clock on subsequent
       reboots to ensure it (roughly) monotonically advances even if the system lacks a battery-buffered RTC chip.

       The systemd-timesyncd service implements SNTP only. This minimalistic service will step the system clock for large offsets or slowly adjust it for
       smaller deltas. Complex use cases that require full NTP support (and where SNTP is not sufficient) are not covered by systemd-timesyncd.

       The NTP servers contacted are determined from the global settings in timesyncd.conf(5), the per-link static settings in .network files, and the
       per-link dynamic settings received over DHCP. See systemd.network(5) for further details.

       timedatectl(1)'s set-ntp command may be used to enable and start, or disable and stop this service.

       timedatectl(1)'s timesync-status or show-timesync command can be used to show the current status of this service.

       systemd-timesyncd initialization delays the start of units that are ordered after time-set.target (see systemd.special(7) for details) until the local
       time has been updated from /var/lib/systemd/timesync/clock (see below) in order to make it roughly monotonic. It does not delay other units until
       synchronization with an accurate reference time sources has been reached. Use systemd-time-wait-sync.service(8) to achieve that, which will delay start
       of units that are ordered after time-sync.target until synchronization to an accurate reference clock is reached.

FILES
       /var/lib/systemd/timesync/clock
	   The modification time ("mtime") of this file is updated on each successful NTP synchronization or after each SaveIntervalSec= time interval, as
	   specified in timesyncd.conf(5).

	   When initializing, the local clock is advanced to the modification time of this file (if the file timestamp is in the past this adjustment is not
	   made). If the file does not exist yet, the clock is instead advanced to the modification time of /usr/lib/clock-epoch – if it exists – or to a time
	   derived from the source tree at build time. This mechanism is used to ensure that the system clock remains somewhat reasonably initialized and
	   roughly monotonic across reboots, in case no battery-buffered local RTC is available.

	   Added in version 219.

       /usr/lib/clock-epoch
	   The modification time ("mtime") of this file is used for advancing the system clock in case /var/lib/systemd/timesync/clock does not exist yet, see
	   above.

	   Added in version 254.

       /run/systemd/timesync/synchronized
	   A file that is touched on each successful synchronization, to assist systemd-time-wait-sync and other applications to detecting synchronization
	   with accurate reference clocks.

	   Added in version 239.

SEE ALSO
       systemd(1), timesyncd.conf(5), systemd.network(5), systemd-networkd.service(8), systemd-time-wait-sync.service(8), systemd.special(7), timedatectl(1),
       localtime(5), hwclock(8)

systemd 255															  SYSTEMD-TIMESYNCD.SERVICE(8)
