POWEROFF(8)								   poweroff								   POWEROFF(8)

NAME
       poweroff, reboot, halt - Power off, reboot, or halt the machine

SYNOPSIS

       poweroff [OPTIONS...]

       reboot [OPTIONS...]

       halt [OPTIONS...]

DESCRIPTION
       poweroff, reboot, and halt may be used to power off, reboot, or halt the machine. All three commands take the same options.

OPTIONS
       The following options are understood:

       --help
	   Print a short help text and exit.

	   Added in version 253.

       --halt
	   Halt the machine, regardless of which one of the three commands is invoked.

	   Added in version 253.

       -p, --poweroff
	   Power off the machine, when either halt or poweroff is invoked. This option is ignored when reboot is invoked.

	   Added in version 253.

       --reboot
	   Reboot the machine, regardless of which one of the three commands is invoked.

	   Added in version 253.

       -f, --force
	   Force immediate power-off, halt, or reboot. If specified, the command does not contact the init system. In most cases, filesystems are not properly
	   unmounted before shutdown. For example, the command reboot -f is mostly equivalent to systemctl reboot -ff, instead of systemctl reboot -f.

	   Added in version 253.

       -w, --wtmp-only
	   Only write wtmp shutdown entry, do not actually power off, reboot, or halt.

	   Added in version 253.

       -d, --no-wtmp
	   Do not write wtmp shutdown entry.

	   Added in version 253.

       -n, --no-sync
	   Don't sync hard disks/storage media before power-off, reboot, or halt.

	   Added in version 253.

       --no-wall
	   Do not send wall message before power-off, reboot, or halt.

	   Added in version 253.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise.

NOTES
       These commands are implemented in a way that preserves basic compatibility with the original SysV commands.  systemctl(1) verbs poweroff, reboot, halt
       provide the same functionality with some additional features.

       Note that on many SysV systems halt used to be synonymous to poweroff, i.e. both commands would equally result in powering the machine off. systemd is
       more accurate here, and halt results in halting the machine only (leaving power on), and poweroff is required to actually power it off.

SEE ALSO
       systemd(1), systemctl(1), shutdown(8), wall(1)

systemd 255																	   POWEROFF(8)
