UDEV.CONF(5)								   udev.conf								  UDEV.CONF(5)

NAME
       udev.conf - Configuration for device event managing daemon

SYNOPSIS
       /etc/udev/udev.conf

DESCRIPTION
       systemd-udevd(8) expects its main configuration file at /etc/udev/udev.conf. It consists of a set of variables allowing the user to override default
       udev values. All empty lines or lines beginning with '#' are ignored. The following variables can be set:

       udev_log=
	   The log level. Valid values are the numerical syslog priorities or their textual representations: err, info and debug.

	   Added in version 216.

       children_max=
	   An integer. The maximum number of events executed in parallel. When unspecified or 0 is specified, the maximum is determined based on the system
	   resources.

	   This is the same as the --children-max= option.

	   Added in version 240.

       exec_delay=
	   An integer. Delay the execution of each RUN{program} parameter by the given number of seconds. This option might be useful when debugging system
	   crashes during coldplug caused by loading non-working kernel modules.

	   This is the same as the --exec-delay= option.

	   Added in version 240.

       event_timeout=
	   An integer. The number of seconds to wait for events to finish. After this time, the event will be terminated. The default is 180 seconds.

	   This is the same as the --event-timeout= option.

	   Added in version 240.

       resolve_names=
	   Specifies when systemd-udevd should resolve names of users and groups. When set to early (the default), names will be resolved when the rules are
	   parsed. When set to late, names will be resolved for every event. When set to never, names will never be resolved and all devices will be owned by
	   root.

	   This is the same as the --resolve-names= option.

	   Added in version 240.

       timeout_signal=
	   Specifies a signal that systemd-udevd will send on worker timeouts. Note that both workers and spawned processes will be killed using this signal.
	   Defaults to SIGKILL.

	   Added in version 246.

       In addition, systemd-udevd can be configured by command line options and the kernel command line (see systemd-udevd(8)).

SEE ALSO
       systemd-udevd(8), udev(7), udevadm(8)

systemd 255																	  UDEV.CONF(5)
