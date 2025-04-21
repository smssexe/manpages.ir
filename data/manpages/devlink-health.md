DEVLINK-HEALTH(8)							     Linux							     DEVLINK-HEALTH(8)

NAME
       devlink-health - devlink health reporting and recovery

SYNOPSIS
       devlink [ OPTIONS ] health  { COMMAND | help }

       OPTIONS := { -V[ersion] }

       devlink health show [ { DEV | DEV/PORT_INDEX } reporter REPORTER ]

       devlink health recover { DEV | DEV/PORT_INDEX } reporter REPORTER

       devlink health diagnose { DEV | DEV/PORT_INDEX } reporter REPORTER

       devlink health dump show { DEV | DEV/PORT_INDEX } reporter REPORTER

       devlink health test { DEV | DEV/PORT_INDEX } reporter REPORTER

       devlink health dump clear { DEV | DEV/PORT_INDEX } reporter REPORTER

       devlink health set { DEV | DEV/PORT_INDEX } reporter REPORTER [ grace_period MSEC ] [ auto_recover { true | false } ] [ auto_dump { true | false } ]

       devlink health help

DESCRIPTION
   devlink health show - Show status and configuration on all supported reporters.
       Displays info about reporters registered on devlink devices and ports.

       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

   devlink health recover - Initiate a recovery operation on a reporter.
       This action performs a recovery and increases the recoveries counter on success.

       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

   devlink health diagnose - Retrieve diagnostics data on a reporter.
       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

   devlink health test - Trigger a test event on a reporter.
       DEV - specifies the devlink device.

       REPORTER - specifies the reporter's name registered on the devlink device.

   devlink health dump show - Display the last saved dump.
       devlink health saves a single dump per reporter. If an dump is
       not already stored by the Devlink, this command will generate a new
       dump. The dump can be generated either automatically when a
       reporter reports on an error or manually at the user's request.

       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

   devlink health dump clear - Delete the saved dump.
       Deleting the saved dump enables a generation of a new dump on
       the next "devlink health dump show" command.

       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

   devlink health set - Configure health reporter.
       Please note that some params are not supported on a reporter which doesn't support a recovery or dump method.

       DEV - specifies the devlink device.
       DEV/PORT_INDEX - specifies the devlink port.

       REPORTER - specifies the reporter's name registered on specified devlink device or port.

       grace_period MSEC
	      Time interval between consecutive auto recoveries.

       auto_recover { true | false }
	      Indicates whether the devlink should execute automatic recover on error.

       auto_dump { true | false }
	      Indicates whether the devlink should execute automatic dump on error.

EXAMPLES
       devlink health show
	   List status and configuration of available reporters on devices and ports.

       devlink health show pci/0000:00:09.0/1 reporter tx
	   List status and configuration of tx reporter registered on port on pci/0000:00:09.0/1

       devlink health recover pci/0000:00:09.0 reporter fw_fatal
	   Initiate recovery on fw_fatal reporter registered on device on pci/0000:00:09.0.

       devlink health recover pci/0000:00:09.0/1 reporter tx
	   Initiate recovery on tx reporter registered on port on pci/0000:00:09.0/1.

       devlink health diagnose pci/0000:00:09.0 reporter fw
	   List diagnostics data on the specified device and reporter.

       devlink health dump show pci/0000:00:09.0/1 reporter tx
	   Display the last saved dump on the specified port and reporter.

       devlink health dump clear pci/0000:00:09.0/1 reporter tx
	   Delete saved dump on the specified port and reporter.

       devlink health set pci/0000:00:09.0 reporter fw_fatal grace_period 3500
	   Set time interval between auto recoveries to minimum of 3500 msec on the specified device and reporter.

       devlink health set pci/0000:00:09.0/1 reporter tx grace_period 3500
	   Set time interval between auto recoveries to minimum of 3500 msec on the specified port and reporter.

       devlink health set pci/0000:00:09.0 reporter fw_fatal auto_recover false
	   Turn off auto recovery on the specified device and reporter.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-port(8), devlink-param(8), devlink-region(8),

AUTHOR
       Aya Levin <ayal@mellanox.com>

iproute2								  20 Feb 2019							     DEVLINK-HEALTH(8)
