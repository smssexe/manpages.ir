NETWORKD-DISPATCHER(8)															NETWORKD-DISPATCHER(8)

NAME
       networkd-dispatcher - Dispatcher service for systemd-networkd connection status changes

SYNOPSIS
       networkd-dispatcher [-h] [-S SCRIPT_DIR] [-T] [-v] [-q]

DESCRIPTION
       Dispatcher daemon for systemd-networkd connection status changes. This daemon is similar to NetworkManager-dispatcher, but is much more limited in the
       types of events it supports due to the limited nature of systemd-networkd(8).

       Desired actions (scripts) are placed into directories that reflect systemd-networkd operational states under SCRIPT_DIR and are executed when the
       daemon receives the relevant event from systemd-networkd.

       The daemon listens for signals from systemd-networkd over dbus, so it should be very light on resources (e.g. no polling). It is meant to be run as a
       system-wide daemon (as root). This allows it to be used for tasks such as starting a VPN after a connection is established.

OPTIONS
       -h, --help
	   Print command-line syntax and program options to stdout.

       -S, --script-dir=SCRIPT_DIR
	   Location under which to look for scripts. Like the PATH environment variable, this may contain multiple directories separated by : and in case
	   multiple directories have scripts with the same name, the earliest directory wins. Defaults to
	   /etc/networkd-dispatcher:/usr/lib/networkd-dispatcher.

       -T, --run-startup-triggers
	   Generate events reflecting preexisting state and behavior on startup. This can be used to ensure that triggers are belatedly run even if
	   networkd-dispatcher is invoked after systemd-networkd has already started an interface.

       -v, --verbose
	   Increase verbosity by one level. The default level is WARNING. Each use of -v will increment the log level (towards INFO or DEBUG), and each use of
	   -q will decrement it (towards ERROR or CRITICAL).

       -q, --quiet
	   Decrease verbosity by one level.

CONFIGURATION FILES
       The systemd service reads /etc/default/networkd-dispatcher as an environment file for additional daemon arguments.

       The scripts to be run on network changes are in subdirectories routable.d/, dormant.d/, no-carrier.d/, off.d/, carrier.d/, degraded.d/, configured.d/,
       configuring.d/ inside SCRIPT_DIR. The default value for SCRIPT_DIR is /etc/networkd-dispatcher:/usr/lib/networkd-dispatcher.

       For information about the network operational states exposed by systemd, see networkctl(1).

ENVIRONMENT
       Scripts are executed with some environment variables set. Some of these variables may not be set or may be set to an empty value, dependent upon the
       type of event. These can be used by scripts to conditionally take action based on a specific interface, state, etc.

       •   IFACE - interface that triggered the event

       •   STATE - The destination state change for which a script is currently being invoked. May be any of the values listed as valid for
	   AdministrativeState or OperationalState.

       •   ESSID - for wlan connections, the ESSID the device is connected to

       •   ADDR - the ipv4 address of the device

       •   IP_ADDRS - space-delimited string of ipv4 address(es) assigned to the device (see note below)

       •   IP6_ADDRS - space-delimited string of ipv6 address(es) assigned to the device (see note below)

       •   AdministrativeState - One of pending, configuring, configured, unmanaged, failed or linger.

       •   OperationalState - One of off, no-carrier, dormant, carrier, degraded, routable, configuring, or configured. For more information about the network
	   operational states exposed by systemd, see the networkctl manpage (man networkctl).

RESOURCES
       GitLab: https://gitlab.com/craftyguy/networkd-dispatcher

SEE ALSO
       systemd-networkd(8), networkctl(1)

									  04/24/2023							NETWORKD-DISPATCHER(8)
