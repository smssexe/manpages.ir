SYSTEMD-BATTERY-CHECK.SERVICE(8)				     systemd-battery-check				      SYSTEMD-BATTERY-CHECK.SERVICE(8)

NAME
       systemd-battery-check.service, systemd-battery-check - Check battery level whether there's enough charge, and power off if not

SYNOPSIS
       systemd-battery-check.service

       /usr/lib/systemd/systemd-battery-check [OPTIONS...]

DESCRIPTION
       This service checks the presence of an external power supply and the battery level during the early boot stage to determine whether there is sufficient
       power to carry on with the booting process.

       systemd-battery-check returns success if the device is connected to an AC power source or if the battery charge is greater than 5%. It returns failure
       otherwise.

OPTIONS
       The following options are understood by systemd-battery-check:

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXIT STATUS
       On success (running on AC power or battery capacity greater than 5%), 0 is returned, a non-zero failure code otherwise.

KERNEL COMMAND LINE
       The following variables are understood:

       systemd.battery-check=BOOL
	   Takes a boolean. If specified with false, systemd-battery-check command will return immediately with exit status 0 without checking battery
	   capacity and AC power existence, and the service systemd-battery-check.service will succeed. This may be useful when the command wrongly detects
	   and reports battery capacity percentage or AC power existence, or when you want to boot the system forcibly.

	   Added in version 254.

SEE ALSO
       systemd(1)

systemd 255														      SYSTEMD-BATTERY-CHECK.SERVICE(8)
