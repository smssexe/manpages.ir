MULTIPATH(8)							    System Manager's Manual							  MULTIPATH(8)

NAME
       multipath - Device mapper target autoconfig.

SYNOPSIS
       multipath [-v level] [-B|-d|-i|-q|-r] [-b file] [-p policy] [device]

       multipath [-v level] [-R retries] -f device

       multipath [-v level] [-R retries] -F

       multipath [-v level] [-l|-ll] [device]

       multipath [-v level] [-a|-w] device

       multipath [-v level] -W

       multipath [-v level] [-i] [-c|-C] device

       multipath [-v level] [-i] [-u|-U]

       multipath [-h|-t|-T]

DESCRIPTION
       multipath is used to detect and coalesce multiple paths to devices, for fail-over or performance reasons.

ARGUMENTS
       The  device  argument  restricts multipath's operation to devices matching the given expression. The argument may refer either to a multipath map or to
       its components ("paths"). The expression may be in one of the following formats:

       device node   file name of a device node, e.g. /dev/dm-10 or /dev/sda. If the node refers to an existing device mapper device representing a  multipath
		     map, this selects the map or its paths, depending on the operation mode. Otherwise, it selects a path device.

       device ID     kernel device number specified by major:minor numbers, e.g. 65:16. This format can only be used for path devices.

       WWID	     a World Wide Identifier matching a multipath map or its paths. To list WWIDs of devices present in the system, use e.g. the command "mul‐
		     tipath -d -v3 2>/dev/null".

OPERATION MODES
       The  default operation mode is to detect and set up multipath maps from the devices found in the system.	 Other operation modes are chosen by using one
       of the following command line switches:

       -f     Flush (remove) a multipath device map specified as parameter, if unused. This operation is delegated to the multipathd daemon if it's running.

       -F     Flush (remove) all unused multipath device maps. This operation is delegated to the multipathd daemon if it's running.

       -l     Show ("list") the current multipath topology from information fetched in sysfs and the device mapper.

       -ll    Show ("list") the current multipath topology from all available information (sysfs, the device mapper, path checkers ...).

       -a     Add the WWID for the specified device to the WWIDs file.

       -w     Remove the WWID for the specified device from the WWIDs file.

       -W     Reset the WWIDs file to only include the current multipath devices.

       -c     Check if a block device should be a path in a multipath device.

       -C     Check if a multipath device has usable paths. This can be used to test whether or not I/O on this device is likely to succeed. The  command  it‐
	      self doesn't attempt to do I/O on the device.

       -u     Check if the device specified in the program environment should be a path in a multipath device.

       -U     Check if the device specified in the program environment is a multipath device with usable paths. See -C.

       -h     Print usage text.

       -t     Display the currently used multipathd configuration.

       -T     Display  the  currently  used  multipathd configuration, limiting the output to those devices actually present in the system. This can be used a
	      template for creating multipath.conf.

OPTIONS
       -v level
	      Verbosity of information printed to stdout in default and "list" operation modes. The default level is -v 2.

		   0	       Nothing is printed.

		   1	       In default mode, Names/WWIDs of created or modified multipath maps are printed. In list mode, WWIDs of all multipath  maps  are
			       printed.

		   2	       In  default  mode,  Topology of created or modified multipath maps is printed.  In list mode, topology of all multipath maps is
			       printed.

		   3	       All detected paths and the topology of all multipath maps are printed.

		   The verbosity level also controls the level of log and debug messages printed to stderr. The default level corresponds to  LOG_NOTICE  (im‐
		   portant messages that shouldn't be missed in normal operation).

       -d     Dry run, do not create or update devmaps.

       -e     Enable all foreign libraries. This overrides the enable_foreign option from multipath.conf(5).

       -i     Ignore  WWIDs  file  when processing devices. If find_multipaths strict or find_multipaths no is set in multipath.conf, multipath only considers
	      devices that are listed in the WWIDs file. This option overrides that behavior. For other values of find_multipaths, this option has no  effect.
	      See the description of find_multipaths in multipath.conf(5).  This option should only be used in rare circumstances.

       -B     Treat the bindings file as read only.

       -b file
	      Set user_friendly_names bindings file location. The default is /etc/multipath/bindings.

       -q     Don't unset the device mapper feature queue_if_no_path for multipath maps. Normally, multipath would do so if multipathd is not running, because
	      only a running multipath daemon guarantees that unusable paths are reinstated when they become usable again.

       -p policy
	      Force  new  maps	to use the specified policy, overriding the configuration in multipath.conf(5). The possible values for policy are the same as
	      the values for path_grouping_policy in multipath.conf(5). Existing maps are not modified.

       -r     Force a reload of all existing multipath maps. This command is delegated to the multipathd daemon if it's running. In this case,	other  command
	      line switches of the multipath command have no effect.

       -R retries
	      Number of times to retry flushing multipath devices that are in use. The default is 0.

SEE ALSO
       multipathd(8), multipath.conf(5), kpartx(8), udev(8), dmsetup(8), hotplug(8).

AUTHORS
       multipath-tools was developed by Christophe Varoqui <christophe.varoqui@opensvc.com> and others.

Linux									  2021-11-12								  MULTIPATH(8)
