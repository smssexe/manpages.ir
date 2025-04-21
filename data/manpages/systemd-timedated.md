SYSTEMD-TIMEDATED.SERVICE(8)					   systemd-timedated.service					  SYSTEMD-TIMEDATED.SERVICE(8)

NAME
       systemd-timedated.service, systemd-timedated - Time and date bus mechanism

SYNOPSIS
       systemd-timedated.service

       /usr/lib/systemd/systemd-timedated

DESCRIPTION
       systemd-timedated.service is a system service that may be used as a mechanism to change the system clock and timezone, as well as to enable/disable
       network time synchronization.  systemd-timedated is automatically activated on request and terminates itself when it is unused.

       The tool timedatectl(1) is a command line client to this service.

       systemd-timedated currently offers access to the following four settings:

       •   The system time

       •   The system timezone

       •   A boolean controlling whether the system RTC is in local or UTC timezone

       •   Whether the time synchronization service is enabled/started or disabled/stopped, see next section.

       See org.freedesktop.timedate1(5) and org.freedesktop.LogControl1(5) for information about the D-Bus API.

LIST OF NETWORK TIME SYNCHRONIZATION SERVICES
       systemd-timesyncd will look for files with a ".list" extension in ntp-units.d/ directories. Each file is parsed as a list of unit names, one per line.
       Empty lines and lines with comments ("#") are ignored. Files are read from /usr/lib/systemd/ntp-units.d/ and the corresponding directories under /etc/,
       /run/, /usr/local/lib/. Files in /etc/ override files with the same name in /run/, /usr/local/lib/, and /usr/lib/. Files in /run/ override files with
       the same name under /usr/. Packages should install their configuration files in /usr/lib/ (distribution packages) or /usr/local/lib/ (local installs).

       Example 1. ntp-units.d/ entry for systemd-timesyncd

	   # /usr/lib/systemd/ntp-units.d/80-systemd-timesync.list
	   systemd-timesyncd.service

       If the environment variable $SYSTEMD_TIMEDATED_NTP_SERVICES is set, systemd-timesyncd will parse the contents of that variable as a colon-separated
       list of unit names. When set, this variable overrides the file-based list described above.

       Example 2. An override that specifies that chronyd should be used if available

	   SYSTEMD_TIMEDATED_NTP_SERVICES=chronyd.service:systemd-timesyncd.service

SEE ALSO
       systemd(1), timedatectl(1), localtime(5), hwclock(8), systemd-timesyncd(8)

systemd 255															  SYSTEMD-TIMEDATED.SERVICE(8)
