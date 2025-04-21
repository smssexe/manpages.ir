VGCFGRESTORE(8)							    System Manager's Manual						       VGCFGRESTORE(8)

NAME
       vgcfgrestore — Restore volume group configuration

SYNOPSIS
       vgcfgrestore option_args position_args
	   [ option_args ]
	   [ position_args ]

	   --commandprofile String
	   --config String
	-d|--debug
	   --devices PV
	   --devicesfile String
	   --driverloaded y|n
	-f|--file String
	   --force
	-h|--help
	   --journal String
	-l|--list
	   --lockopt String
	   --longhelp
	-M|--metadatatype lvm2
	   --nohints
	   --nolocking
	   --profile String
	-q|--quiet
	-t|--test
	-v|--verbose
	   --version
	-y|--yes

DESCRIPTION
       vgcfgrestore  restores the metadata of a VG from a text back up file produced by vgcfgbackup. This writes VG metadata onto the devices specifed in back
       up file.

       A back up file can be specified with --file.  If no backup file is specified, the most recent one is used. Use --list for a list of the available  back
       up and archive files of a VG.

       WARNING:	 When  a  VG contains thin pools, changes to thin metadata cannot be reverted, and data loss may occur if thin metadata has changed. The force
       option is required to restore in this case.

USAGE
       Restore VG metadata from last backup.

       vgcfgrestore VG
	   [ COMMON_OPTIONS ]

       —

       Restore VG metadata from specified file.

       vgcfgrestore -f|--file String VG
	   [ COMMON_OPTIONS ]

       —

       List all VG metadata backups.

       vgcfgrestore -l|--list VG
	   [ COMMON_OPTIONS ]

       —

       List one VG metadata backup file.

       vgcfgrestore -l|--list -f|--file String
	   [ COMMON_OPTIONS ]
	   [ VG ]

       —

       Common options for command:
	   [ -M|--metadatatype lvm2 ]
	   [	--force ]

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

       -f|--file String
	      Read metadata backup from the named file.	 Usually this file was created by vgcfgbackup.

       --force ...
	      Force metadata restore even with thin pool LVs.  Use with extreme caution. Most changes to thin metadata cannot be reverted.  You may lose  data
	      if you restore metadata that does not match the thin pool kernel metadata precisely.

       -h|--help
	      Display help text.

       --journal String
	      Record  information  in  the systemd journal.  This information is in addition to information enabled by the lvm.conf log/journal setting.  com‐
	      mand: record information about the command.  output: record the default command output.  debug: record full command debugging.

       -l|--list
	      List metadata backup and archive files pertaining to the VG.  May be used with --file. Does not restore the VG.

       --lockopt String
	      Used to pass options for special cases to lvmlockd.  See lvmlockd(8) for more information.

       --longhelp
	      Display long help text.

       -M|--metadatatype lvm2
	      Specifies the type of on-disk metadata to use.  lvm2 (or just 2) is the current, standard format.	 lvm1 (or just 1) is no longer used.

       --nohints
	      Do not use the hints file to locate devices for PVs. A command may read more devices to find PVs when hints are not used. The command will still
	      perform standard hint file invalidation where appropriate.

       --nolocking
	      Disable locking. Use with caution, concurrent commands may produce incorrect results.

       --profile String
	      An alias for --commandprofile or --metadataprofile, depending on the command.

       -q|--quiet ...
	      Suppress output and log messages. Overrides --debug and --verbose.  Repeat once to also suppress any prompts with answer 'no'.

       -t|--test
	      Run in test mode. Commands will not update metadata.  This is implemented by disabling all metadata writing but nevertheless  returning  success
	      to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes
	      has changed but hasn't.

       -v|--verbose ...
	      Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.

       --version
	      Display version information.

       -y|--yes
	      Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution.	(For automatic no, see -qq.)

VARIABLES
       VG     Volume Group name.  See lvm(8) for valid names.

       String See the option description for information about the string content.

       Size[UNIT]
	      Size  is	an  input number that accepts an optional unit.	 Input units are always treated as base two values, regardless of capitalization, e.g.
	      'k' and 'K' both refer to 1024.  The default input unit is specified by letter, followed by |UNIT.  UNIT represents other possible input	units:
	      b|B is bytes, s|S is sectors of 512 bytes, k|K is KiB, m|M is MiB, g|G is GiB, t|T is TiB, p|P is PiB, e|E is EiB.  (This should not be confused
	      with the output control --units, where capital letters mean multiple of 1000.)

ENVIRONMENT VARIABLES
       See lvm(8) for information about environment variables used by lvm.  For example, LVM_VG_NAME can generally be substituted for a required VG parameter.

NOTES
       To  replace  PVs,  vgdisplay --partial --verbose will show the UUIDs and sizes of any PVs that are no longer present. If a PV in the VG is lost and you
       wish to substitute another of the same size, use pvcreate --restorefile filename --uuid uuid (plus additional arguments as appropriate)	to  initialise
       it  with	 the same UUID as the missing PV. Repeat for all other missing PVs in the VG.  Then use vgcfgrestore --file filename to restore the VG's meta‐
       data.

SEE ALSO
       lvm(8), lvm.conf(5), lvmconfig(8), lvmdevices(8),

       pvchange(8), pvck(8), pvcreate(8), pvdisplay(8), pvmove(8), pvremove(8), pvresize(8), pvs(8), pvscan(8),

       vgcfgbackup(8), vgcfgrestore(8), vgchange(8), vgck(8), vgcreate(8), vgconvert(8), vgdisplay(8), vgexport(8), vgextend(8), vgimport(8),
       vgimportclone(8), vgimportdevices(8), vgmerge(8), vgmknodes(8), vgreduce(8), vgremove(8), vgrename(8), vgs(8), vgscan(8), vgsplit(8),

       lvcreate(8), lvchange(8), lvconvert(8), lvdisplay(8), lvextend(8), lvreduce(8), lvremove(8), lvrename(8), lvresize(8), lvs(8), lvscan(8),

       lvm-fullreport(8), lvm-lvpoll(8), blkdeactivate(8), lvmdump(8),

       dmeventd(8), lvmpolld(8), lvmlockd(8), lvmlockctl(8), cmirrord(8), lvmdbusd(8), fsadm(8),

       lvmsystemid(7), lvmreport(7), lvmraid(7), lvmthin(7), lvmcache(7)

Red Hat, Inc.						       LVM TOOLS 2.03.16(2) (2022-05-18)					       VGCFGRESTORE(8)
