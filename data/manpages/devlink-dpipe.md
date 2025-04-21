DEVLINK-DPIPE(8)							     Linux							      DEVLINK-DPIPE(8)

NAME
       devlink-dpipe - devlink dataplane pipeline visualization

SYNOPSIS
       devlink [ OPTIONS ] dpipe { table | header } { COMMAND | help }

       OPTIONS := { -V[ersion] }

       devlink dpipe table show DEV [ name TABLE_NAME ]

       devlink dpipe table set DEV name TABLE_NAME

       devlink dpipe table dump DEV name TABLE_NAME

       devlink dpipe header show DEV

       devlink dpipe help

DESCRIPTION
   devlink dpipe table show - display devlink dpipe table attributes
       name TABLE_NAME
	      Specifies the table to operate on.

   devlink dpipe table set - set devlink dpipe table attributes
       name TABLE_NAME
	      Specifies the table to operate on.

   devlink dpipe table dump - dump devlink dpipe table entries
       name TABLE_NAME
	      Specifies the table to operate on.

   devlink dpipe header show - display devlink dpipe header attributes
       name TABLE_NAME
	      Specifies the table to operate on.

EXAMPLES
       devlink dpipe table show pci/0000:01:00.0
	   Shows all dpipe tables on specified devlink device.

       devlink dpipe table show pci/0000:01:00.0 name mlxsw_erif
	   Shows mlxsw_erif dpipe table on specified devlink device.

       devlink dpipe table set pci/0000:01:00.0 name mlxsw_erif counters_enabled true
	   Turns on the counters on mlxsw_erif table.

       devlink dpipe table dump pci/0000:01:00.0 name mlxsw_erif
	   Dumps content of mlxsw_erif table.

       devlink dpipe header show pci/0000:01:00.0
	   Shows all dpipe headers on specified devlink device.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-monitor(8),

AUTHOR
       Jiri Pirko <jiri@mellanox.com>

iproute2								  4 Apr 2020							      DEVLINK-DPIPE(8)
