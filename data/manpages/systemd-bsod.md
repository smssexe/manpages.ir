SYSTEMD-BSOD.SERVICE(8)							 systemd-bsod						       SYSTEMD-BSOD.SERVICE(8)

NAME
       systemd-bsod.service, systemd-bsod - Displays boot-time emergency log message in full screen.

SYNOPSIS
       systemd-bsod.service

       systemd-bsod [OPTIONS...]

DESCRIPTION
       systemd-bsod.service is used to display a blue screen which contains a message relating to a boot failure, including a QR code which can be scanned to
       get helpful information about the failure.

OPTIONS
       The following options are understood by systemd-bsod:

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

       -c, --continuous
	   When specified, systemd-bsod waits continuously for changes in the journal if it doesn't find any emergency messages on the initial attempt.

	   Added in version 255.

EXIT STATUS
       On success (displaying the journal message successfully), 0 is returned, a non-zero failure code otherwise.

SEE ALSO
       systemd(1)

systemd 255															       SYSTEMD-BSOD.SERVICE(8)
