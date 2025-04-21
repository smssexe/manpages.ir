SYSTEMD-BINFMT.SERVICE(8)					    systemd-binfmt.service					     SYSTEMD-BINFMT.SERVICE(8)

NAME
       systemd-binfmt.service, systemd-binfmt - Configure additional binary formats for executables at boot

SYNOPSIS
       systemd-binfmt.service

       /usr/lib/systemd/systemd-binfmt

DESCRIPTION
       systemd-binfmt.service is an early boot service that registers additional binary formats for executables in the kernel.

       See binfmt.d(5) for information about the configuration of this service.

OPTIONS
       --unregister
	   If passed, instead of registering configured binary formats in the kernel, the reverse operation is executed: all currently registered binary
	   formats are unregistered from the kernel.

	   Added in version 246.

       --cat-config
	   Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.

       --tldr
	   Copy the contents of config files to standard output. Only the "interesting" parts of the configuration files are printed, comments and empty lines
	   are skipped. Before each file, the filename is printed as a comment.

       --no-pager
	   Do not pipe output into a pager.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

SEE ALSO
       systemd(1), binfmt.d(5), wine(8)

systemd 255															     SYSTEMD-BINFMT.SERVICE(8)
