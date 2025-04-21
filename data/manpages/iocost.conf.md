IOCOST.CONF(5)								  iocost.conf								IOCOST.CONF(5)

NAME
       iocost.conf - Configuration files for the iocost solution manager

SYNOPSIS
       /etc/systemd/iocost.conf /etc/systemd/iocost.conf.d/*.conf

DESCRIPTION
       This file configures the behavior of "iocost", a tool mostly used by systemd-udevd(8) rules to automatically apply I/O cost solutions to
       /sys/fs/cgroup/io.cost.*.

       The qos and model values are calculated based on benchmarks collected on the iocost-benchmark[1] project and turned into a set of solutions that go
       from most to least isolated. Isolation allows the system to remain responsive in face of high I/O load. Which solutions are available for a device can
       be queried from the udev metadata attached to it. By default the naive solution is used, which provides the most bandwidth.

CONFIGURATION DIRECTORIES AND PRECEDENCE
       The default configuration is set during compilation, so configuration is only needed when it is necessary to deviate from those defaults. The main
       configuration file is either in /usr/lib/systemd/ or /etc/systemd/ and contains commented out entries showing the defaults as a guide to the
       administrator. Local overrides can be created by creating drop-ins, as described below. The main configuration file can also be edited for this purpose
       (or a copy in /etc/ if it's shipped in /usr/) however using drop-ins for local configuration is recommended over modifications to the main
       configuration file.

       In addition to the "main" configuration file, drop-in configuration snippets are read from /usr/lib/systemd/*.conf.d/,
       /usr/local/lib/systemd/*.conf.d/, and /etc/systemd/*.conf.d/. Those drop-ins have higher precedence and override the main configuration file. Files in
       the *.conf.d/ configuration subdirectories are sorted by their filename in lexicographic order, regardless of in which of the subdirectories they
       reside. When multiple files specify the same option, for options which accept just a single value, the entry in the file sorted last takes precedence,
       and for options which accept a list of values, entries are collected as they occur in the sorted files.

       When packages need to customize the configuration, they can install drop-ins under /usr/. Files in /etc/ are reserved for the local administrator, who
       may use this logic to override the configuration files installed by vendor packages. Drop-ins have to be used to override package drop-ins, since the
       main configuration file has lower precedence. It is recommended to prefix all filenames in those subdirectories with a two-digit number and a dash, to
       simplify the ordering of the files. This also defined a concept of drop-in priority to allow distributions to ship drop-ins within a specific range
       lower than the range used by users. This should lower the risk of package drop-ins overriding accidentally drop-ins defined by users.

       To disable a configuration file supplied by the vendor, the recommended way is to place a symlink to /dev/null in the configuration directory in /etc/,
       with the same filename as the vendor configuration file.

OPTIONS
       All options are configured in the [IOCost] section:

       TargetSolution=
	   Chooses which I/O cost solution (identified by named string) should be used for the devices in this system. The known solutions can be queried from
	   the udev metadata attached to the devices. If a device does not have the specified solution, the first one listed in IOCOST_SOLUTIONS is used
	   instead.

	   E.g.	 "TargetSolution=isolated-bandwidth".

	   Added in version 254.

SEE ALSO
       udevadm(8), The iocost-benchmarks github project[1], The resctl-bench documentation details how the values are obtained[2]

NOTES
	1. iocost-benchmark
	   https://github.com/iocost-benchmark/iocost-benchmarks

	2. The resctl-bench documentation details how the values are obtained
	   https://github.com/facebookexperimental/resctl-demo/tree/main/resctl-bench/doc

systemd 255																	IOCOST.CONF(5)
