VGDISPLAY(8)							    System Manager's Manual							  VGDISPLAY(8)

NAME
       vgdisplay — Display volume group information

SYNOPSIS
       vgdisplay
	   [ option_args ]
	   [ position_args ]

DESCRIPTION
       vgdisplay shows the attributes of VGs, and the associated PVs and LVs.

       vgs(8) is a preferred alternative that shows the same information and more, using a more compact and configurable output format.

USAGE
       vgdisplay
	   [ -A|--activevolumegroups ]
	   [ -c|--colon ]
	   [ -C|--columns ]
	   [ -o|--options String ]
	   [ -S|--select String ]
	   [ -s|--short ]
	   [ -O|--sort String ]
	   [	--aligned ]
	   [	--binary ]
	   [	--configreport log|vg|lv|pv|pvseg|seg ]
	   [	--foreign ]
	   [	--ignorelockingfailure ]
	   [	--logonly ]
	   [	--noheadings ]
	   [	--nosuffix ]
	   [	--readonly ]
	   [	--shared ]
	   [	--separator String ]
	   [	--unbuffered ]
	   [	--units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E ]
	   [ COMMON_OPTIONS ]
	   [ VG|Tag ... ]

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

       -A|--activevolumegroups
	      Only select active VGs. The VG is considered active if at least one of its LVs is active.

       --aligned
	      Use with --separator to align the output columns

       --binary
	      Use  binary  values  "0" or "1" instead of descriptive literal values for columns that have exactly two valid values to report (not counting the
	      "unknown" value which denotes that the value could not be determined).

       -c|--colon
	      Generate colon separated output for easier parsing in scripts or programs.  Also see vgs(8) which provides considerably more  control  over  the
	      output.

       -C|--columns
	      Display output in columns, the equivalent of vgs(8).  Options listed are the same as options given in vgs(8).

       --commandprofile String
	      The command profile to use for command configuration.  See lvm.conf(5) for more information about profiles.

       --config String
	      Config  settings	for  the  command.  These  override lvm.conf(5) settings.  The String arg uses the same format as lvm.conf(5), or may use sec‐
	      tion/field syntax.  See lvm.conf(5) for more information about config.

       --configreport log|vg|lv|pv|pvseg|seg
	      See lvmreport(7).

       -d|--debug ...
	      Set debug level. Repeat from 1 to 6 times to increase the detail of messages sent to the log file and/or syslog (if configured).

       --devices PV
	      Restricts the devices that are visible and accessible to the command.  Devices not listed will appear to be missing. This option can be  repeat‐
	      ed, or accepts a comma separated list of devices. This overrides the devices file.

       --devicesfile String
	      A file listing devices that LVM should use.  The file must exist in /etc/lvm/devices/ and is managed with the lvmdevices(8) command.  This over‐
	      rides the lvm.conf(5) devices/devicesfile and devices/use_devicesfile settings.

       --driverloaded y|n
	      If set to no, the command will not attempt to use device-mapper.	For testing and debugging.

       --foreign
	      Report/display foreign VGs that would otherwise be skipped.  See lvmsystemid(7) for more information about foreign VGs.

       -h|--help
	      Display help text.

       --ignorelockingfailure
	      Allows a command to continue with read-only metadata operations after locking failures.

       --journal String
	      Record  information  in  the systemd journal.  This information is in addition to information enabled by the lvm.conf log/journal setting.  com‐
	      mand: record information about the command.  output: record the default command output.  debug: record full command debugging.

       --lockopt String
	      Used to pass options for special cases to lvmlockd.  See lvmlockd(8) for more information.

       --logonly
	      Suppress command report and display only log report.

       --longhelp
	      Display long help text.

       --noheadings
	      Suppress the headings line that is normally the first line of output.  Useful if grepping the output.

       --nohints
	      Do not use the hints file to locate devices for PVs. A command may read more devices to find PVs when hints are not used. The command will still
	      perform standard hint file invalidation where appropriate.

       --nolocking
	      Disable locking. Use with caution, concurrent commands may produce incorrect results.

       --nosuffix
	      Suppress the suffix on output sizes. Use with --units (except h and H) if processing the output.

       -o|--options String
	      Comma-separated, ordered list of fields to display in columns.  String arg syntax is: [+|-|#]Field1[,Field2 ...]	The prefix + will  append  the
	      specified	 fields to the default fields, - will remove the specified fields from the default fields, and # will compact specified fields (remov‐
	      ing them when empty for all rows.)  Use -o help to view the list of all available fields.	 Use separate lists of fields to add, remove  or  com‐
	      pact  by	repeating  the	-o option: -o+field1,field2 -o-field3,field4 -o#field5.	 These lists are evaluated from left to right.	Use field name
	      lv_all to view all LV fields, vg_all all VG fields, pv_all all PV fields, pvseg_all all PV segment fields, seg_all all LV	 segment  fields,  and
	      pvseg_all	 all PV segment columns.  See the lvm.conf(5) report section for more config options.  See lvmreport(7) for more information about re‐
	      porting.

       --profile String
	      An alias for --commandprofile or --metadataprofile, depending on the command.

       -q|--quiet ...
	      Suppress output and log messages. Overrides --debug and --verbose.  Repeat once to also suppress any prompts with answer 'no'.

       --readonly
	      Run the command in a special read-only mode which will read on-disk metadata without needing to take any locks. This can be used to peek	inside
	      metadata	used  by  a  virtual machine image while the virtual machine is running. No attempt will be made to communicate with the device-mapper
	      kernel driver, so this option is unable to report whether or not LVs are actually in use.

       -S|--select String
	      Select objects for processing and reporting based on specified criteria.	The criteria syntax is described by --select  help  and	 lvmreport(7).
	      For  reporting commands, one row is displayed for each object matching the criteria.  See --options help for selectable object fields.  Rows can
	      be displayed with an additional "selected" field (-o selected) showing 1 if the row matches the selection and 0  otherwise.   For	 non-reporting
	      commands which process LVM entities, the selection is used to choose items to process.

       --separator String
	      String to use to separate each column. Useful if grepping the output.

       --shared
	      Report/display  shared  VGs  that	 would otherwise be skipped when lvmlockd is not being used on the host.  See lvmlockd(8) for more information
	      about shared VGs.

       -s|--short
	      Give a short listing showing the existence of VGs.

       -O|--sort String
	      Comma-separated ordered list of columns to sort by. Replaces the default selection. Precede any column with - for a reverse sort on that column.

       -t|--test
	      Run in test mode. Commands will not update metadata.  This is implemented by disabling all metadata writing but nevertheless  returning  success
	      to the calling function. This may lead to unusual error messages in multi-stage operations if a tool relies on reading back metadata it believes
	      has changed but hasn't.

       --unbuffered
	      Produce output immediately without sorting or aligning the columns properly.

       --units [Number]r|R|h|H|b|B|s|S|k|K|m|M|g|G|t|T|p|P|e|E
	      All  sizes  are  output  in  these  units:  human-(r)eadable  with  '<'  rounding	 indicator, (h)uman-readable, (b)ytes, (s)ectors, (k)ilobytes,
	      (m)egabytes, (g)igabytes, (t)erabytes, (p)etabytes, (e)xabytes.  Capitalise to use multiples of 1000 (S.I.) instead of 1024.  Custom  units  can
	      be specified, e.g. --units 3M.

       -v|--verbose ...
	      Set verbose level. Repeat from 1 to 4 times to increase the detail of messages sent to stdout and stderr.

       --version
	      Display version information.

       -y|--yes
	      Do not prompt for confirmation interactively but always assume the answer yes. Use with extreme caution.	(For automatic no, see -qq.)

VARIABLES
       VG     Volume Group name.  See lvm(8) for valid names.

       Tag    Tag name.	 See lvm(8) for information about tag names and using tags in place of a VG, LV or PV.

       String See the option description for information about the string content.

       Size[UNIT]
	      Size  is	an  input number that accepts an optional unit.	 Input units are always treated as base two values, regardless of capitalization, e.g.
	      'k' and 'K' both refer to 1024.  The default input unit is specified by letter, followed by |UNIT.  UNIT represents other possible input	units:
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

Red Hat, Inc.						       LVM TOOLS 2.03.16(2) (2022-05-18)						  VGDISPLAY(8)
