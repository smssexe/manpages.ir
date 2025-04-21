DEVLINK-DEV(8)								     Linux								DEVLINK-DEV(8)

NAME
       vdpa-dev - vdpa management device view

SYNOPSIS
       vdpa mgmtdev  { COMMAND| help }

       OPTIONS := { -V[ersion] }

       vdpa mgmtdev show [ MGMTDEV ]

       vdpa mgmtdev help

DESCRIPTION
   vdpa mgmtdev show - display vdpa management device attributes
       MGMTDEV - specifies the vdpa management device to show.	If this argument is omitted all management devices are listed.

EXAMPLES
       vdpa mgmtdev show
	   Shows all the vdpa management devices on the system.

       vdpa mgmtdev show bar
	   Shows the specified vdpa management device.

SEE ALSO
       vdpa(8), vdpa-dev(8),

AUTHOR
       Parav Pandit <parav@nvidia.com>

iproute2								  5 Jan 2021								DEVLINK-DEV(8)
