CLOUD-INIT-PER(1)						    General Commands Manual						     CLOUD-INIT-PER(1)

NAME
       cloud-init-per - Run a command with arguments at a specific frequency

SYNOPSIS
       cloud-init-per <frequency> <name> <cmd> [ arg1 [ arg2 [...]]]

DESCRIPTION
       Run a command with arguments at a specific frequency.

       This utility can make it easier to use boothooks or bootcmd on a per "once" or "always" basis. For example:

	   - [ cloud-init-per, once, mymkfs, mkfs, /dev/vdb ]

       The cloud-init-per command replaced the cloud-init-run-module command.

OPTIONS
       frequency
	      This can be one of the following values:

	      once: run only once and do not re-run for new instance-id

	      instance: run only once for a given instance-id and re-run for new instance-id

	      always: run every boot

       name   A name to give the command to run to show up in logs.

       cmd [ arg1 [ arg2 [...]]]
	      The actual command to run followed by any additional arguments.

COPYRIGHT
       Copyright (C) 2020 Canonical Ltd. License GPL-3 or Apache-2.0

SEE ALSO
       Full documentation at: <https://docs.cloud-init.io>

																	     CLOUD-INIT-PER(1)
