UUIDD(8)							     System Administration							      UUIDD(8)

NAME
       uuidd - UUID generation daemon

SYNOPSIS
       uuidd [options]

DESCRIPTION
       The uuidd daemon is used by the UUID library to generate universally unique identifiers (UUIDs), especially time-based UUIDs, in a secure and
       guaranteed-unique fashion, even in the face of large numbers of threads running on different CPUs trying to grab UUIDs.

OPTIONS
       -C, --cont-clock[=time]
	   Activate continuous clock handling for time based UUIDs. uuidd could use all possible clock values, beginning with the daemon’s start time. The
	   optional argument can be used to set a value for the max_clock_offset. This gurantees, that a clock value of a UUID will always be within the range
	   of the max_clock_offset.

	   The option '-C' or '--cont-clock' enables the feature with a default max_clock_offset of 2 hours.

	   The option '-C<NUM>[hd]' or '--cont-clock=<NUM>[hd]' enables the feature with a max_clock_offset of NUM seconds. In case of an appended h or d, the
	   NUM value is read in hours or days. The minimum value is 60 seconds, the maximum value is 365 days.

       -d, --debug
	   Run uuidd in debugging mode. This prevents uuidd from running as a daemon.

       -F, --no-fork
	   Do not daemonize using a double-fork.

       -k, --kill
	   If currently a uuidd daemon is running, kill it.

       -n, --uuids number
	   When issuing a test request to a running uuidd, request a bulk response of number UUIDs.

       -P, --no-pid
	   Do not create a pid file.

       -p, --pid path
	   Specify the pathname where the pid file should be written. By default, the pid file is written to {runstatedir}/uuidd/uuidd.pid.

       -q, --quiet
	   Suppress some failure messages.

       -r, --random
	   Test uuidd by trying to connect to a running uuidd daemon and request it to return a random-based UUID.

       -S, --socket-activation
	   Do not create a socket but instead expect it to be provided by the calling process. This implies --no-fork and --no-pid. This option is intended to
	   be used only with systemd(1). It needs to be enabled with a configure option.

       -s, --socket path
	   Make uuidd use this pathname for the unix-domain socket. By default, the pathname used is {runstatedir}/uuidd/request. This option is primarily for
	   debugging purposes, since the pathname is hard-coded in the libuuid library.

       -T, --timeout number
	   Make uuidd exit after number seconds of inactivity.

       -t, --time
	   Test uuidd by trying to connect to a running uuidd daemon and request it to return a time-based UUID.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXAMPLE
       Start up a daemon, print 42 random keys, and then stop the daemon:

	   uuidd -p /tmp/uuidd.pid -s /tmp/uuidd.socket
	   uuidd -d -r -n 42 -s /tmp/uuidd.socket
	   uuidd -d -k -s /tmp/uuidd.socket

AUTHOR
       The uuidd daemon was written by Theodore Ts’o <tytso@mit.edu>.

SEE ALSO
       uuid(3), uuidgen(1)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The uuidd command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								      UUIDD(8)
