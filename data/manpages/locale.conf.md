LOCALE.CONF(5)								  locale.conf								LOCALE.CONF(5)

NAME
       locale.conf - Configuration file for locale settings

SYNOPSIS
       /etc/locale.conf

DESCRIPTION
       The /etc/locale.conf file configures system-wide locale settings. It is read at early boot by systemd(1).

       The format of locale.conf is a newline-separated list of environment-like shell-compatible variable assignments, ignoring comments and empty lines. It
       is possible to source the configuration from shell scripts, however, beyond mere variable assignments, no shell features are supported, allowing
       applications to read the file without implementing a shell compatible execution engine. See os-release(5) for a detailed description of the format.

       Note that the kernel command line options locale.LANG=, locale.LANGUAGE=, locale.LC_CTYPE=, locale.LC_NUMERIC=, locale.LC_TIME=, locale.LC_COLLATE=,
       locale.LC_MONETARY=, locale.LC_MESSAGES=, locale.LC_PAPER=, locale.LC_NAME=, locale.LC_ADDRESS=, locale.LC_TELEPHONE=, locale.LC_MEASUREMENT=,
       locale.LC_IDENTIFICATION= may be used to override the locale settings at boot.

       The locale settings configured in /etc/locale.conf are system-wide and are inherited by every service or user, unless overridden or unset by individual
       programs or users.

       Depending on the operating system, other configuration files might be checked for locale configuration as well, however only as fallback.

       /etc/locale.conf can be updated using systemd-localed.service(8).  localectl(1) may be used to alter the settings in this file during runtime from the
       command line. Use systemd-firstboot(1) to customize them on mounted (but not booted) system images.

OPTIONS
       The following locale settings may be set using /etc/locale.conf: LANG=, LANGUAGE=, LC_CTYPE=, LC_NUMERIC=, LC_TIME=, LC_COLLATE=, LC_MONETARY=,
       LC_MESSAGES=, LC_PAPER=, LC_NAME=, LC_ADDRESS=, LC_TELEPHONE=, LC_MEASUREMENT=, LC_IDENTIFICATION=. Note that LC_ALL may not be configured in this
       file. For details about the meaning and semantics of these settings, refer to locale(7).

EXAMPLE
       Example 1. German locale with English messages

       /etc/locale.conf:

	   # Custom settings

	   LANG=de_DE.UTF-8
	   LC_MESSAGES=en_US.UTF-8

SEE ALSO
       systemd(1), locale(7), localectl(1), systemd-localed.service(8), systemd-firstboot(1)

systemd 255																	LOCALE.CONF(5)
