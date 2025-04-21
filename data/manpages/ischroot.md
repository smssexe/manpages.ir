ISCHROOT(1)							    General Commands Manual							   ISCHROOT(1)

NAME
       ischroot - detect if running in a chroot

SYNOPSIS
       ischroot [--default-false] [--default-true] [--help] [--version]

DESCRIPTION
       ischroot detects if it is currently running in a chroot.	 The exit status is:

       0      if currently running in a chroot

       1      if currently not running in a chroot

       2      if the detection is not possible.

OPTIONS
       -f, --default-false
	      Exit with status 1 if the detection is not possible.

       -t, --default-true
	      Exit with status 0 if the detection is not possible.

       --help Print a usage message on standard output and exit successfully.

       --version
	      Print version information on standard output and exit successfully.

Debian									  30 May 2011								   ISCHROOT(1)
