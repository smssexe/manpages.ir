SWITCH_ROOT(8)							     System Administration							SWITCH_ROOT(8)

NAME
       switch_root - switch to another filesystem as the root of the mount tree

SYNOPSIS
       switch_root [-hV]

       switch_root newroot init [arg...]

DESCRIPTION
       switch_root moves already mounted /proc, /dev, /sys and /run to newroot and makes newroot the new root filesystem and starts init process.

       WARNING: switch_root removes recursively all files and directories on the current root filesystem.

OPTIONS
       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       switch_root returns 1 on failure, it never returns on success.

NOTES
       switch_root will fail to function if newroot is not the root of a mount. If you want to switch root into a directory that does not meet this
       requirement then you can first use a bind-mounting trick to turn any directory into a mount point:

	   mount --bind $DIR $DIR

AUTHORS
       Peter Jones <pjones@redhat.com>, Jeremy Katz <katzj@redhat.com>, Karel Zak <kzak@redhat.com>

SEE ALSO
       chroot(2), init(8), mkinitrd(8), mount(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The switch_root command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								SWITCH_ROOT(8)
