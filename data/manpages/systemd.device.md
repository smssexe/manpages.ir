SYSTEMD.DEVICE(5)							systemd.device							     SYSTEMD.DEVICE(5)

NAME
       systemd.device - Device unit configuration

SYNOPSIS
       device.device

DESCRIPTION
       A unit configuration file whose name ends in ".device" encodes information about a device unit as exposed in the sysfs/udev(7) device tree. This may be
       used to define dependencies between devices and other units.

       This unit type has no specific options. See systemd.unit(5) for the common options of all unit configuration files. The common configuration items are
       configured in the generic [Unit] and [Install] sections. A separate [Device] section does not exist, since no device-specific options may be
       configured.

       systemd will dynamically create device units for all kernel devices that are marked with the "systemd" udev tag (by default all block and network
       devices, and a few others). Note that if systemd-udevd.service is not running, no device units will be available (for example in a typical container).

       Device units are named after the /sys/ and /dev/ paths they control. Example: the device /dev/sda5 is exposed in systemd as dev-sda5.device. For
       details about the escaping logic used to convert a file system path to a unit name see systemd.unit(5).

       To tag a udev device, use "TAG+="systemd"" in the udev rules file, see udev(7) for details.

       Device units will be reloaded by systemd whenever the corresponding device generates a "changed" event. Other units can use ReloadPropagatedFrom= to
       react to that event.

AUTOMATIC DEPENDENCIES
   Implicit Dependencies
       Many unit types automatically acquire dependencies on device units of devices they require. For example, .socket unit acquire dependencies on the
       device units of the network interface specified in BindToDevice=. Similar, swap and mount units acquire dependencies on the units encapsulating their
       backing block devices.

   Default Dependencies
       There are no default dependencies for device units.

THE UDEV DATABASE
       Unit settings of device units may either be configured via unit files, or directly from the udev database. The following udev device properties are
       understood by the service manager:

       SYSTEMD_WANTS=, SYSTEMD_USER_WANTS=
	   Adds dependencies of type Wants= from the device unit to the specified units.  SYSTEMD_WANTS= is read by the system service manager,
	   SYSTEMD_USER_WANTS= by user service manager instances. These properties may be used to activate arbitrary units when a specific device becomes
	   available.

	   Note that this and the other udev device properties are not taken into account unless the device is tagged with the "systemd" tag in the udev
	   database, because otherwise the device is not exposed as a systemd unit (see above).

	   Note that systemd will only act on Wants= dependencies when a device first becomes active. It will not act on them if they are added to devices
	   that are already active. Use SYSTEMD_READY= (see below) to configure when a udev device shall be considered active, and thus when to trigger the
	   dependencies.

	   The specified property value should be a space-separated list of valid unit names. If a unit template name is specified (that is, a unit name
	   containing an "@" character indicating a unit name to use for multiple instantiation, but with an empty instance name following the "@"), it will
	   be automatically instantiated by the device's "sysfs" path (that is: the path is escaped and inserted as instance name into the template unit
	   name). This is useful in order to instantiate a specific template unit once for each device that appears and matches specific properties.

       SYSTEMD_ALIAS=
	   Adds an additional alias name to the device unit. This must be an absolute path that is automatically transformed into a unit name. (See above.)

       SYSTEMD_READY=
	   If set to 0, systemd will consider this device unplugged even if it shows up in the udev tree. If this property is unset or set to 1, the device
	   will be considered plugged if it is visible in the udev tree.

	   This option is useful for devices that initially show up in an uninitialized state in the tree, and for which a "changed" event is generated the
	   moment they are fully set up. Note that SYSTEMD_WANTS= (see above) is not acted on as long as SYSTEMD_READY=0 is set for a device.

       ID_MODEL_FROM_DATABASE=, ID_MODEL=
	   If set, this property is used as description string for the device unit.

OPTIONS
       Device unit files may include [Unit] and [Install] sections, which are described in systemd.unit(5). No options specific to this file type are
       supported.

SEE ALSO
       systemd(1), systemctl(1), systemd.unit(5), udev(7), systemd.directives(7)

systemd 255																     SYSTEMD.DEVICE(5)
