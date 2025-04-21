NEEDRESTART(1)								 User Commands								NEEDRESTART(1)

NAME
       needrestart - needrestart

DESCRIPTION
       needrestart checks which daemons need to be restarted after library upgrades.

USAGE
       Usage:

	      needrestart [-(v|q)] [-n] [-c <cfg>] [-r <mode>] [-f <fe>] [-u <ui>] [-(b|p)] [-kl]

       -v     be more verbose

       -q     be quiet

       -m <mode>
	      set level of technical details

	  e   (e)asy mode

	  a   (a)dvanced mode

	  u   (u)buntu mode, used to customized the behaviour in the APT hook. See /usr/share/doc/README.Ubuntu.

       -n     set default answer to 'no'

       -c <cfg>
	      config filename

       -r <mode>
	      set restart mode

	  l   (l)ist only

	  i   (i)nteractive restart

	  a   (a)utomatically restart

	      ATTENTION:  If  needrestart  is  configured to run in interactive mode but is run non-interactive (i.e. unattended-upgrades) it will fallback to
	      list only mode.

       -b     enable batch mode

       -p     nagios plugin mode: makes output and exit codes nagios compatible

       -f <fe>
	      override debconf(7) frontend, sets the DEBIAN_FRONTEND environment variable to <fe>

       -t <seconds>
	      When checking running interpreter processes, allow process start times that are close to timestamps of files the interpreter uses,  within  this
	      tolerance	 (default 2). The default value of 2 seconds is best for checks of Linux hosts, on which system limitations prevent more accurate mea‐
	      surements of process start times. Values higher than 0 should prevent false positives yet may in extreme cases  cause  false  negatives;	values
	      higher than 2 should not be necessary.

       -u <ui>
	      use preferred UI package (-u ? shows available packages)

       By using one of the following options only the specified checks are performed:

       -k     check for obsolete kernel

       -l     check for obsolete libraries

ENVIRONMENT
       The following environment variables can be used to override the config file options. Command line parameters do always supersede them.

       NEEDRESTART_MODE
	      Change the configured restart mode (see also the -r parameter): (l)ist only, (i)nteractive or (a)utomatically

       When used with apt-get(8) needrestart supports the following additional environment variables:

       DEBIAN_FRONTEND
	      The debconf(7) frontend to use, can also set using the -f parameter.

       NEEDRESTART_SUSPEND
	      If set to a non-empty value the apt-get(8) hook will not run needrestart after installing or updating packages.

AUTHOR
       Thomas Liske <thomas@fiasko-nw.net>

COPYRIGHT
       2013 - 2022 (C) Thomas Liske [http://fiasko-nw.net/~thomas/]

       This  program  is  free	software;  you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free
       Software Foundation; either version 2 of the License, or (at your option) any later version.

UPSTREAM
       https://github.com/liske/needrestart

needrestart								 January 2015								NEEDRESTART(1)
