CLOUD-INIT(1)							    General Commands Manual							 CLOUD-INIT(1)

NAME
       cloud-init - Cloud instance initialization

SYNOPSIS
       cloud-init [-h] [-d] [--force] [-v] [SUBCOMMAND]

DESCRIPTION
       Cloud-init  provides  a	mechanism  for cloud instance initialization.  This is done by identifying the cloud platform that is in use, reading provided
       cloud metadata and optional vendor and user data, and then initializing the instance as requested.

OPTIONS
       -h, --help
	      Show help message and exit.

       -v, --version
	      Show program's version number and exit.

       --all-stages
	      INTERNAL: Run cloud-init's stages under a single process using a syncronization protocol. This is not intended for CLI usage.

SUBCOMMANDS
       Please see the help output for each subcommand for additional details, flags, and subcommands.

       analyze
	      Analyze cloud-init logs and data.

       collect-logs
	      Collect and tar all cloud-init debug info.

       clean  Remove logs and artifacts so cloud-init can re-run.

       devel  Run development tools. See help output for subcommand details.

       features
	      List defined features.

       query  Query standardized instance metadata from the command line.

       schema Validate cloud-config files using jsonschema.

       single Manually run a single module. Useful for testing during development.

       status Report cloud-init status or wait on completion.

DEPRECATED
       -d, --debug
	      Show additional pre-action logging (default: False).

       --force
	      Force running even if no datasource is found (use at your own risk).

       init   Initialize cloud-init and execute initial modules.

       modules
	      Activate modules using a given configuration key.

EXIT STATUS
	      0 - Success

	      1 - Error - Cloud-init failed.

	      2 - Recoverable error - Cloud-init completed but experienced errors.

COPYRIGHT
       Copyright (C) 2020 Canonical Ltd. License GPL-3 or Apache-2.0

SEE ALSO
       Full documentation at: <https://docs.cloud-init.io>

																		 CLOUD-INIT(1)
