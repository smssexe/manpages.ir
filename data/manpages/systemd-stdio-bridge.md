SYSTEMD-STDIO-BRIDGE(1)						     systemd-stdio-bridge					       SYSTEMD-STDIO-BRIDGE(1)

NAME
       systemd-stdio-bridge - D-Bus proxy

SYNOPSIS

       systemd-stdio-bridge [OPTIONS...]

DESCRIPTION
       systemd-stdio-bridge implements a proxy between STDIN/STDOUT and a D-Bus bus. It expects to receive an open connection via STDIN/STDOUT when started,
       and will create a new connection to the specified bus. It will then forward messages between the two connections. This program is suitable for socket
       activation: the first connection may be a pipe or a socket and must be passed as either standard input, or as an open file descriptor according to the
       protocol described in sd_listen_fds(3). The second connection will be made by default to the local system bus, but this can be influenced by the
       --user, --system, --machine=, and --bus-path= options described below.

       sd-bus(3) uses systemd-stdio-bridge to forward D-Bus connections over ssh(1), or to connect to the bus of a different user, see sd_bus_set_address(3).

OPTIONS
       The following options are understood:

       --user
	   Talk to the service manager of the calling user, rather than the service manager of the system.

       --system
	   Talk to the service manager of the system. This is the implied default.

       -M, --machine=
	   Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating
	   "@" character. If the special string ".host" is used in place of the container name, a connection to the local system is made (which is useful to
	   connect to a specific user's user bus: "--user --machine=lennart@.host"). If the "@" syntax is not used, the connection is made as root user. If
	   the "@" syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and ".host"
	   are implied.

       -p PATH, --bus-path=PATH
	   Path to the bus address. Default: "unix:path=/run/dbus/system_bus_socket"

	   Added in version 251.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise.

SEE ALSO
       dbus-daemon(1), dbus-broker(1), D-Bus[1], systemd(1)

NOTES
	1. D-Bus
	   https://www.freedesktop.org/wiki/Software/dbus

systemd 255															       SYSTEMD-STDIO-BRIDGE(1)
