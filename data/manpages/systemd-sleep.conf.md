SYSTEMD-SLEEP.CONF(5)						      systemd-sleep.conf						 SYSTEMD-SLEEP.CONF(5)

NAME
       systemd-sleep.conf, sleep.conf.d - Suspend and hibernation configuration file

SYNOPSIS
       /etc/systemd/sleep.conf

       /etc/systemd/sleep.conf.d/*.conf

       /run/systemd/sleep.conf.d/*.conf

       /usr/lib/systemd/sleep.conf.d/*.conf

DESCRIPTION
       systemd supports four general power-saving modes:

       suspend
	   a low-power state where execution of the OS is paused, and complete power loss might result in lost data, and which is fast to enter and exit. This
	   corresponds to suspend, standby, or freeze states as understood by the kernel.

	   Added in version 203.

       hibernate
	   a low-power state where execution of the OS is paused, and complete power loss does not result in lost data, and which might be slow to enter and
	   exit. This corresponds to the hibernation as understood by the kernel.

	   Added in version 203.

       hybrid-sleep
	   a low-power state where execution of the OS is paused, which might be slow to enter, and on complete power loss does not result in lost data but
	   might be slower to exit in that case. This mode is called suspend-to-both by the kernel.

	   Added in version 203.

       suspend-then-hibernate
	   A low power state where the system is initially suspended (the state is stored in RAM). When the battery level is too low (less than 5%) or a
	   certain timespan has passed, whichever happens first, the system is automatically woken up and then hibernated. This establishes a balance between
	   speed and safety.

	   If the system has no battery, it would be hibernated after HibernateDelaySec= has passed. If not set, then defaults to "2h".

	   If the system has battery and HibernateDelaySec= is not set, low-battery alarms (ACPI _BTP) are tried first for detecting battery percentage and
	   wake up the system for hibernation. If not available, or HibernateDelaySec= is set, the system would regularly wake up to check the time and detect
	   the battery percentage/discharging rate. The rate is used to schedule the next detection. If that is also not available, SuspendEstimationSec= is
	   used as last resort.

	   Added in version 239.

       Settings in these files determine what strings will be written to /sys/power/disk and /sys/power/state by systemd-sleep(8) when systemd(1) attempts to
       suspend or hibernate the machine. See systemd.syntax(7) for a general description of the syntax.

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
       The following options can be configured in the [Sleep] section of /etc/systemd/sleep.conf or a sleep.conf.d file:

       AllowSuspend=, AllowHibernation=, AllowHybridSleep=, AllowSuspendThenHibernate=
	   By default any power-saving mode is advertised if possible (i.e. the kernel supports that mode, the necessary resources are available). Those
	   switches can be used to disable specific modes.

	   If AllowHibernation=no or AllowSuspend=no is used, this implies AllowSuspendThenHibernate=no and AllowHybridSleep=no, since those methods use both
	   suspend and hibernation internally.	AllowSuspendThenHibernate=yes and AllowHybridSleep=yes can be used to override and enable those specific
	   modes.

	   Added in version 240.

       HibernateMode=
	   The string to be written to /sys/power/disk by systemd-hibernate.service(8). More than one value can be specified by separating multiple values
	   with whitespace. They will be tried in turn, until one is written without error. If none of the writes succeed, the operation will be aborted.

	   The allowed set of values is determined by the kernel and is shown in the file itself (use cat /sys/power/disk to display). See the kernel
	   documentation page Basic sysfs Interfaces for System Suspend and Hibernation[1] for more details.

	   systemd-suspend-then-hibernate.service(8) uses the value of HibernateMode= when hibernating.

	   Added in version 203.

       SuspendState=
	   The string to be written to /sys/power/state by systemd-suspend.service(8). More than one value can be specified by separating multiple values with
	   whitespace. They will be tried in turn, until one is written without error. If none of the writes succeed, the operation will be aborted.

	   The allowed set of values is determined by the kernel and is shown in the file itself (use cat /sys/power/state to display). See Basic sysfs
	   Interfaces for System Suspend and Hibernation[1] for more details.

	   systemd-suspend-then-hibernate.service(8) uses this value when suspending.

	   Added in version 203.

       HibernateDelaySec=
	   The amount of time the system spends in suspend mode before the system is automatically put into hibernate mode. Only used by systemd-suspend-then-
	   hibernate.service(8). Refer to suspend-then-hibernate for details on how this option interacts with other options/system battery state.

	   Added in version 239.

       SuspendEstimationSec=
	   The RTC alarm will wake the system after the specified timespan to measure the system battery capacity level and estimate battery discharging rate.
	   Only used by systemd-suspend-then-hibernate.service(8). Refer to suspend-then-hibernate for details on how this option interacts with other
	   options/system battery state.

	   Added in version 253.

EXAMPLE: FREEZE
       Example: to exploit the “freeze” mode added in Linux 3.9, one can use systemctl suspend with

	   [Sleep]
	   SuspendState=freeze

SEE ALSO
       systemd-sleep(8), systemd-suspend.service(8), systemd-hibernate.service(8), systemd-hybrid-sleep.service(8), systemd-suspend-then-hibernate.service(8),
       systemd(1), systemd.directives(7)

NOTES
	1. Basic sysfs Interfaces for System Suspend and Hibernation
	   https://www.kernel.org/doc/html/latest/admin-guide/pm/sleep-states.html#basic-sysfs-interfaces-for-system-suspend-and-hibernation

systemd 255																 SYSTEMD-SLEEP.CONF(5)
