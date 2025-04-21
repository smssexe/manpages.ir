CLOUD-ID(1)							    General Commands Manual							   CLOUD-ID(1)

NAME
       cloud-id - Report the canonical cloud-id for this instance

SYNOPSIS
       cloud-id [-h] [-j] [-l] [-i <INSTANCE_DATA>]

DESCRIPTION
       cloud-id is the lowercase name of the cloud datasource discovered.

       The cloud-id will be 'not run' when systemd generator has not run yet.  The cloud-id will be 'disabled' when cloud-init is disabled or when ds-identify
       did not find a valid datasource.

       See cloud-init status --long for more information.

OPTIONS
       -h, --help
	      Show help message and exit

       -j, --json
	      Report all standardized cloud-id information as json

       -l, --long
	      Report extended cloud-id information as tab-delimited string

       -i <data>, --instance-data <data>
	      Path to instance-data.json file. Default is /run/cloud-init/instance-data.json

EXIT STATUS
       0      On success

       1      Due to an error

       2      Due to cloud-init in a disabled state. See: cloud-init status --long

       3      The cloud-init generator and discovery has not yet run.

COPYRIGHT
       Copyright (C) 2021 Canonical Ltd. License GPL-3 or Apache-2.0

SEE ALSO
       Full documentation at: <https://docs.cloud-init.io>

																		   CLOUD-ID(1)
