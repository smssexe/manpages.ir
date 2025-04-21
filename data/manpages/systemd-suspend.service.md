SYSTEMD-SUSPEND.SERVICE(8)					    systemd-suspend.service					    SYSTEMD-SUSPEND.SERVICE(8)

NAME
       systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, systemd-suspend-then-hibernate.service, systemd-sleep - System sleep
       state logic

SYNOPSIS
       systemd-suspend.service

       systemd-hibernate.service

       systemd-hybrid-sleep.service

       systemd-suspend-then-hibernate.service

       /usr/lib/systemd/system-sleep

DESCRIPTION
       systemd-suspend.service is a system service that is pulled in by suspend.target and is responsible for the actual system suspend. Similarly,
       systemd-hibernate.service is pulled in by hibernate.target to execute the actual hibernation. Finally, systemd-hybrid-sleep.service is pulled in by
       hybrid-sleep.target to execute hybrid hibernation with system suspend and pulled in by suspend-then-hibernate.target to execute system suspend with a
       timeout that will activate hibernate later.

       Immediately before entering system suspend and/or hibernation systemd-suspend.service (and the other mentioned units, respectively) will run all
       executables in /usr/lib/systemd/system-sleep/ and pass two arguments to them. The first argument will be "pre", the second either "suspend",
       "hibernate", "hybrid-sleep", or "suspend-then-hibernate" depending on the chosen action. An environment variable called "SYSTEMD_SLEEP_ACTION" will be
       set and contain the sleep action that is processing. This is primarily helpful for "suspend-then-hibernate" where the value of the variable will be
       "suspend", "hibernate", or "suspend-after-failed-hibernate" in cases where hibernation has failed. Immediately after leaving system suspend and/or
       hibernation the same executables are run, but the first argument is now "post". All executables in this directory are executed in parallel, and
       execution of the action is not continued until all executables have finished.

       Note that scripts or binaries dropped in /usr/lib/systemd/system-sleep/ are intended for local use only and should be considered hacks. If applications
       want to react to system suspend/hibernation and resume, they should rather use the Inhibitor interface[1].

       Note that systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, and systemd-suspend-then-hibernate.service should never be
       executed directly. Instead, trigger system sleep with a command such as systemctl suspend or systemctl hibernate.

       Internally, this service will echo a string like "mem" into /sys/power/state, to trigger the actual system suspend. What exactly is written where can
       be configured in the [Sleep] section of /etc/systemd/sleep.conf or a sleep.conf.d file. See systemd-sleep.conf(5).

OPTIONS
       systemd-sleep understands the following commands:

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

       suspend, hibernate, suspend-then-hibernate, hybrid-sleep
	   Suspend, hibernate, suspend then hibernate, or put the system to hybrid sleep.

	   Added in version 203.

SEE ALSO
       systemd-sleep.conf(5), systemd(1), systemctl(1), systemd.special(7), systemd-halt.service(8)

NOTES
	1. Inhibitor interface
	   https://www.freedesktop.org/wiki/Software/systemd/inhibit

systemd 255															    SYSTEMD-SUSPEND.SERVICE(8)
