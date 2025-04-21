SYSTEMD.SWAP(5)								 systemd.swap							       SYSTEMD.SWAP(5)

NAME
       systemd.swap - Swap unit configuration

SYNOPSIS
       swap.swap

DESCRIPTION
       A unit configuration file whose name ends in ".swap" encodes information about a swap device or file for memory paging controlled and supervised by
       systemd.

       This man page lists the configuration options specific to this unit type. See systemd.unit(5) for the common options of all unit configuration files.
       The common configuration items are configured in the generic [Unit] and [Install] sections. The swap specific configuration options are configured in
       the [Swap] section.

       Additional options are listed in systemd.exec(5), which define the execution environment the swapon(8) program is executed in, in systemd.kill(5),
       which define the way these processes are terminated, and in systemd.resource-control(5), which configure resource control settings for these processes
       of the unit.

       Swap units must be named after the devices or files they control. Example: the swap device /dev/sda5 must be configured in a unit file dev-sda5.swap.
       For details about the escaping logic used to convert a file system path to a unit name, see systemd.unit(5). Note that swap units cannot be templated,
       nor is possible to add multiple names to a swap unit by creating additional symlinks to it.

       Note that swap support on Linux is privileged, swap units are hence only available in the system service manager (and root's user service manager), but
       not in unprivileged user's service manager.

AUTOMATIC DEPENDENCIES
   Implicit Dependencies
       The following dependencies are implicitly added:

       •   All swap units automatically get the BindsTo= and After= dependencies on the device units or the mount units of the files they are activated from.

       Additional implicit dependencies may be added as result of execution and resource control parameters as documented in systemd.exec(5) and
       systemd.resource-control(5).

   Default Dependencies
       The following dependencies are added unless DefaultDependencies=no is set:

       •   Swap units automatically acquire a Conflicts= and a Before= dependency on umount.target so that they are deactivated at shutdown as well as a
	   Before=swap.target dependency.

FSTAB
       Swap units may either be configured via unit files, or via /etc/fstab (see fstab(5) for details). Swaps listed in /etc/fstab will be converted into
       native units dynamically at boot and when the configuration of the system manager is reloaded. See systemd-fstab-generator(8) for details about the
       conversion.

       If a swap device or file is configured in both /etc/fstab and a unit file, the configuration in the latter takes precedence.

       When reading /etc/fstab, a few special options are understood by systemd which influence how dependencies are created for swap units.

       noauto, auto
	   With noauto, the swap unit will not be added as a dependency for swap.target. This means that it will not be activated automatically during boot,
	   unless it is pulled in by some other unit. The auto option has the opposite meaning and is the default.

	   Added in version 218.

       nofail
	   With nofail, the swap unit will be only wanted, not required by swap.target. This means that the boot will continue even if this swap device is not
	   activated successfully.

	   Added in version 218.

       x-systemd.device-timeout=
	   Configure how long systemd should wait for a device to show up before giving up on an entry from /etc/fstab. Specify a time in seconds or
	   explicitly append a unit such as "s", "min", "h", "ms".

	   Note that this option can only be used in /etc/fstab, and will be ignored when part of the Options= setting in a unit file.

	   Added in version 215.

       x-systemd.makefs
	   The swap structure will be initialized on the device. If the device is not "empty", i.e. it contains any signature, the operation will be skipped.
	   It is hence expected that this option remains set even after the device has been initialized.

	   Note that this option can only be used in /etc/fstab, and will be ignored when part of the Options= setting in a unit file.

	   See systemd-mkswap@.service(8) and the discussion of wipefs(8) in systemd.mount(5).

	   Added in version 240.

OPTIONS
       Swap unit files may include [Unit] and [Install] sections, which are described in systemd.unit(5).

       Swap unit files must include a [Swap] section, which carries information about the swap device it supervises. A number of options that may be used in
       this section are shared with other unit types. These options are documented in systemd.exec(5) and systemd.kill(5). The options specific to the [Swap]
       section of swap units are the following:

       What=
	   Takes an absolute path of a device node or file to use for paging. See swapon(8) for details. If this refers to a device node, a dependency on the
	   respective device unit is automatically created. (See systemd.device(5) for more information.) If this refers to a file, a dependency on the
	   respective mount unit is automatically created. (See systemd.mount(5) for more information.) This option is mandatory. Note that the usual
	   specifier expansion is applied to this setting, literal percent characters should hence be written as "%%".

       Priority=
	   Swap priority to use when activating the swap device or file. This takes an integer. This setting is optional and ignored when the priority is set
	   by pri= in the Options= key.

       Options=
	   May contain an option string for the swap device. This may be used for controlling discard options among other functionality, if the swap backing
	   device supports the discard or trim operation. (See swapon(8) for more information.) Note that the usual specifier expansion is applied to this
	   setting, literal percent characters should hence be written as "%%".

	   Added in version 217.

       TimeoutSec=
	   Configures the time to wait for the swapon command to finish. If a command does not exit within the configured time, the swap will be considered
	   failed and be shut down again. All commands still running will be terminated forcibly via SIGTERM, and after another delay of this time with
	   SIGKILL. (See KillMode= in systemd.kill(5).) Takes a unit-less value in seconds, or a time span value such as "5min 20s". Pass "0" to disable the
	   timeout logic. Defaults to DefaultTimeoutStartSec= from the manager configuration file (see systemd-system.conf(5)).

       Check systemd.unit(5), systemd.exec(5), and systemd.kill(5) for more settings.

SEE ALSO
       systemd(1), systemctl(1), systemd-system.conf(5), systemd.unit(5), systemd.exec(5), systemd.kill(5), systemd.resource-control(5), systemd.device(5),
       systemd.mount(5), swapon(8), systemd-fstab-generator(8), systemd.directives(7)

systemd 255																       SYSTEMD.SWAP(5)
