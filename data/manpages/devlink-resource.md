DEVLINK-RESOURCE(8)							     Linux							   DEVLINK-RESOURCE(8)

NAME
       devlink-resource - devlink device resource configuration

SYNOPSIS
       devlink [ OPTIONS ] resource  { COMMAND | help }

       OPTIONS := { -v[erbose] }

       devlink resource show DEV

       devlink resource help

       devlink resource set DEV path RESOURCE_PATH size RESOURCE_SIZE

DESCRIPTION
   devlink resource show - display devlink device's resosources
       DEV - specifies the devlink device to show.

	   Format is:
	     BUS_NAME/BUS_ADDRESS

   devlink resource set - sets resource size of specific resource
       DEV - specifies the devlink device.

       path RESOURCE_PATH
	      Resource's path.

       size RESOURCE_SIZE
	      The new resource's size.

EXAMPLES
       devlink resource show pci/0000:01:00.0
	   Shows the resources of the specified devlink device.

       devlink resource set pci/0000:01:00.0 /kvd/linear 98304
	   Sets the size of the specified resource for the specified devlink device.

SEE ALSO
       devlink(8), devlink-port(8), devlink-sb(8), devlink-monitor(8),

AUTHOR
       Arkadi Sharshevsky <arkadis@mellanox.com>

iproute2								  11 Feb 2018							   DEVLINK-RESOURCE(8)
