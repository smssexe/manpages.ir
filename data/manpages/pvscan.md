PVSCAN(8)							    System Manager's Manual							     PVSCAN(8)

NAME
       pvscan — List all physical volumes

SYNOPSIS
       pvscan option_args position_args
	   [ option_args ]
	   [ position_args ]

	-a|--activate y|n|ay
	   --autoactivation String
	   --cache
	   --checkcomplete
	   --commandprofile String
	   --config String
	-d|--debug
	   --devices PV
	   --devicesfile String
	   --driverloaded y|n
	-e|--exported
	-h|--help
	   --ignorelockingfailure
	   --journal String
	   --listlvs
	   --listvg
	   --lockopt String
	   --longhelp
	-j|--major Number
	   --minor Number
	   --nohints
	   --nolocking
	   --noudevsync
	-n|--novolumegroup
	   --profile String
	-q|--quiet
	   --reportformat basic|json
	-s|--short
	-t|--test
	   --udevoutput
	-u|--uuid
	-v|--verbose
	   --version
	   --vgonline
	-y|--yes

DESCRIPTION
       When called without the --cache option, pvscan lists PVs on the system, like pvs(8) or pvdisplay(8).

       When --cache is used, pvscan updates runtime lvm state on the system, or with -aay performs autoactivation.

       pvscan --cache device

       If  device  is  present, lvm records that the PV on device is online.  If device is not present, lvm removes the online record for the PV.  pvscan only
       reads the named device.

       pvscan --cache

       Updates the runtime state for all lvm devices.

       pvscan --cache -aay device

       Performs the --cache steps for the device, then checks if the VG using the device is complete.  If so, LVs in the VG are	 autoactivated,	 the  same  as
       vgchange -aay vgname would do.  (A device name may be replaced with major and minor numbers.)

       pvscan --cache -aay

       Performs the --cache steps for all devices, then autoactivates any complete VGs.

       pvscan --cache --listvg|--listlvs device

       Performs	 the  --cache steps for the device, then prints the name of the VG using the device, or the names of LVs using the device.  --checkcomplete is
       usually included to check if all PVs for the VG or LVs are online.  When this command is called by a udev rule, the output must conform	to  udev  rule
       specifications (see --udevoutput.)  The udev rule will use the results to perform autoactivation.

       Autoactivation of VGs or LVs can be enabled/disabled using vgchange or lvchange with --setautoactivation y|n, or by adding names to lvm.conf(5) activa‐
       tion/auto_activation_volume_list

       See lvmautoactivation(7) for more information about how pvscan is used for autoactivation.

USAGE
       Display PV information.

       pvscan
	   [ -e|--exported ]
	   [ -n|--novolumegroup ]
	   [ -s|--short ]
	   [ -u|--uuid ]
	   [	--ignorelockingfailure ]
	   [	--reportformat basic|json ]
	   [ COMMON_OPTIONS ]

       —

       Record that a PV is online or offline.

       pvscan --cache
	   [ -j|--major Number ]
	   [	--ignorelockingfailure ]
	   [	--reportformat basic|json ]
	   [	--minor Number ]
	   [	--noudevsync ]
	   [ COMMON_OPTIONS ]
	   [ String|PV ... ]

       —

       Record that a PV is online and autoactivate the VG if complete.

       pvscan --cache -a|--activate ay
	   [ -j|--major Number ]
	   [	--ignorelockingfailure ]
	   [	--reportformat basic|json ]
	   [	--minor Number ]
	   [	--noudevsync ]
	   [	--autoactivation String ]
	   [ COMMON_OPTIONS ]
	   [ String|PV ... ]

       —

       Record that a PV is online and list the VG using the PV.

       pvscan --cache --listvg PV
	   [	--ignorelockingfailure ]
	   [	--checkcomplete ]
	   [	--vgonline ]
	   [	--udevoutput ]
	   [	--autoactivation String ]
	   [ COMMON_OPTIONS ]

       —

       Record that a PV is online and list LVs using the PV.

       pvscan --cache --listlvs PV
	   [	--ignorelockingfailure ]
	   [	--checkcomplete ]
	   [	--vgonline ]
	   [ COMMON_OPTIONS ]

       —

       List LVs using the PV.

       pvscan --listlvs PV
	   [ COMMON_OPTIONS ]

       —

       List the VG using the PV.

       pvscan --listvg PV
	   [ COMMON_OPTIONS ]

       —

       Common options for lvm:
	   [ -d|--debug ]
	   [ -h|--help ]
	   [ -q|--quiet ]
	   [ -t|--test ]
	   [ -v|--verbose ]
	   [ -y|--yes ]
	   [	--commandprofile String ]
	   [	--config String ]
	   [	--devices PV ]
	   [	--devicesfile String ]
	   [	--driverloaded y|n ]
	   [	--journal String ]
	   [	--lockopt String ]
	   [	--longhelp ]
	   [	--nohints ]
	   [	--nolocking ]
	   [	--profile String ]
	   [	--version ]

OPTIONS

       -a|--activate y|n|ay
	      Auto-activate LVs in a VG when the PVs scanned have completed the VG.  (Only ay is applicable.)

       --autoactivation String
	      Specify if autoactivation is being used from an event.  This allows the command to apply settings that are specific to event activation, such as
	      device scanning optimizations using pvs_online files created by event-based pvscans.

       --cache
	      Scan one or more devices and record that they are online.

       --checkcomplete
	      Check  if all the devices used by a VG or LV are present, and print "complete" or "incomplete" for each listed VG or LV.	This option is used as
	      a part of event-based autoactivation, so pvscan will do nothing if this option is set and event_activation=0 in the config settings.

       --commandprofile String
	      The command profile to use for command configuration.  See lvm.conf(5) for more information about profiles.

       --config String
	      Config settings for the command. These override lvm.conf(5) settings.  The String arg uses the same format  as  lvm.conf(5),  or	may  use  sec‐
	      tion/field syntax.  See lvm.conf(5) for more information about config.

       -d|--debug ...
	      Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).

       --devices PV
	      Restricts	 the  devices  that  are  visible and accessible to the command.  Devices not listed will appear to be missing. This option can be re‐
	      peated, or accepts a comma separated list of devices. This overrides the devices file.

       --devicesfile String
	      A file listing devices that LVM should use.  The file must exist in /etc/lvm/devices/ and is managed with the lvmdevices(8) command.  This over‐
	      rides the lvm.conf(5) devices/devicesfile and devices/use_devicesfile settings.

       --driverloaded y|n
	      If set to no, the command will not attempt to use device-mapper.	For testing and debugging.

       -e|--exported
	      Only show PVs belonging to exported VGs.

       -h|--help
	      Display help text.

       --ignorelockingfailure
	      Allows a command to continue with read-only metadata operations after locking failures.

       --journal String
	      Record information in the systemd journal.  This information is in addition to information enabled by the lvm.conf  log/journal  setting.	  com‐
	      mand: record information about the command.  output: record the default command output.  debug: record full command debugging.

       --listlvs
	      Print a list of LVs that use the device.

       --listvg
	      Print the VG that uses the device.

       --lockopt String
	      Used to pass options for special cases to lvmlockd.  See lvmlockd(8) for more information.

       --longhelp
	      Display long help text.

       -j|--major Number
	      The major number of a device.

       --minor Number
	      The minor number of a device.

       --nohints
	      Do not use the hints file to locate devices for PVs. A command may read more devices to find PVs when hints are not used. The command will still
	      perform standard hint file invalidation where appropriate.

       --nolocking
	      Disable locking. Use with caution, concurrent commands may produce incorrect results.

       --noudevsync
	      Disables udev synchronisation. The process will not wait for notification from udev. It will continue irrespective of any possible udev process‐
	      ing in the background. Only use this if udev is not running or has rules that ignore the devices LVM creates.

       -n|--novolumegroup
	      Only show PVs not belonging to any VG.

       --profile String
	      An alias for --commandprofile or --metadataprofile, depending on the command.

       -q|--quiet ...
	      Suppress output and log messages. Overrides --debug and --verbose.  Repeat once to also suppress any prompts with answer 'no'.

       --reportformat basic|json
	      Overrides current output format for reports which is defined globally by the report/output_format setting in lvm.conf(5).	 basic is the original
	      format  with  columns  and rows.	If there is more than one report per command, each report is prefixed with the report name for identification.
	      json produces report output in JSON format. See lvmreport(7) for more information.

       -s|--short
	      Short listing format.

       -t|--test
	      Run in test mode. Commands will not update metadata.  This is implemented by disabling all metadata writing but nevertheless  returning  success
	      to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes
	      has changed but hasn't.

       --udevoutput
	      Command output is modified to be imported from a udev rule.

       -u|--uuid
	      Show UUIDs in addition to device names.

       -v|--verbose ...
	      Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.

       --version
	      Display version information.

       --vgonline
	      The first command to see a complete VG will report it uniquely.  Other commands to see the complete VG will report it differently.

       -y|--yes
	      Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution.	(For automatic no, see -qq.)

VARIABLES
       PV     Physical Volume name, a device path under /dev.  For commands managing physical extents, a PV positional arg generally accepts a suffix indicat‐
	      ing  a  range (or multiple ranges) of physical extents (PEs). When the first PE is omitted, it defaults to the start of the device, and when the
	      last PE is omitted it defaults to end.  Start and end range (inclusive): PV[:PE-PE]...  Start and length range (counting from 0): PV[:PE+PE]...

       String See the option description for information about the string content.

       Size[UNIT]
	      Size is an input number that accepts an optional unit.  Input units are always treated as base two values, regardless  of	 capitalization,  e.g.
	      'k'  and 'K' both refer to 1024.	The default input unit is specified by letter, followed by |UNIT.  UNIT represents other possible input units:
	      b|B is bytes, s|S is sectors of 512 bytes, k|K is KiB, m|M is MiB, g|G is GiB, t|T is TiB, p|P is PiB, e|E is EiB.  (This should not be confused
	      with the output control --units, where capital letters mean multiple of 1000.)

ENVIRONMENT VARIABLES
       See lvm(8) for information about environment variables used by lvm.  For example, LVM_VG_NAME can generally be substituted for a required VG parameter.

SEE ALSO
       lvm(8), lvm.conf(5), lvmconfig(8), lvmdevices(8),

       pvchange(8), pvck(8), pvcreate(8), pvdisplay(8), pvmove(8), pvremove(8), pvresize(8), pvs(8), pvscan(8),

       vgcfgbackup(8), vgcfgrestore(8), vgchange(8), vgck(8), vgcreate(8), vgconvert(8), vgdisplay(8), vgexport(8), vgextend(8), vgimport(8),
       vgimportclone(8), vgimportdevices(8), vgmerge(8), vgmknodes(8), vgreduce(8), vgremove(8), vgrename(8), vgs(8), vgscan(8), vgsplit(8),

       lvcreate(8), lvchange(8), lvconvert(8), lvdisplay(8), lvextend(8), lvreduce(8), lvremove(8), lvrename(8), lvresize(8), lvs(8), lvscan(8),

       lvm-fullreport(8), lvm-lvpoll(8), blkdeactivate(8), lvmdump(8),

       dmeventd(8), lvmpolld(8), lvmlockd(8), lvmlockctl(8), cmirrord(8), lvmdbusd(8), fsadm(8),

       lvmsystemid(7), lvmreport(7), lvmraid(7), lvmthin(7), lvmcache(7)

Red Hat, Inc.						       LVM TOOLS 2.03.16(2) (2022-05-18)						     PVSCAN(8)
