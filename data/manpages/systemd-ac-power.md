SYSTEMD-AC-POWER(1)						       systemd-ac-power							   SYSTEMD-AC-POWER(1)

NAME
       systemd-ac-power - Report whether we are connected to an external power source

SYNOPSIS

       systemd-ac-power [OPTIONS...]

DESCRIPTION
       systemd-ac-power may be used to check whether the system is running on AC power or not. By default it will simply return success (if we can detect that
       we are running on AC power) or failure, with no output. This can be useful for example to debug ConditionACPower= (see systemd.unit(5)).

OPTIONS
       The following options are understood:

       -v, --verbose
	   Show result as text instead of just returning success or failure.

	   Added in version 253.

       --low
	   Instead of showing AC power state, show low battery state. In this case will return zero if all batteries are currently discharging and below 5% of
	   maximum charge. Returns non-zero otherwise.

	   Added in version 254.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXIT STATUS
       On success (running on AC power), 0 is returned, a non-zero failure code otherwise.

SEE ALSO
       systemd(1)

systemd 255																   SYSTEMD-AC-POWER(1)
