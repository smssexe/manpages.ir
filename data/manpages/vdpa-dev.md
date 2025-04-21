DEVLINK-DEV(8)								     Linux								DEVLINK-DEV(8)

NAME
       vdpa-dev - vdpa device configuration

SYNOPSIS
       vdpa dev [ OPTIONS ]  { COMMAND| help }

       OPTIONS := { -V[ersion] }

       vdpa dev show [ DEV ]

       vdpa dev help

       vdpa dev add name NAME mgmtdev MGMTDEV [ mac MACADDR ] [ mtu MTU ] [ max_vqp MAX_VQ_PAIRS ]

       vdpa dev del DEV

       vdpa dev config show [ DEV ]

       vdpa dev vstats show DEV qidx QUEUE_INDEX

DESCRIPTION
   vdpa dev show - display vdpa device attributes
       DEV - specifies the vdpa device to show.	 If this argument is omitted all devices are listed.

	   Format is:
	     VDPA_DEVICE_NAME

   vdpa dev add - add a new vdpa device.
       name NAME
	      Name of the new vdpa device to add.

       mgmtdev MGMTDEV
	      Name of the management device to use for device addition.

       mac MACADDR - specifies the mac address for the new vdpa device.	 This is applicable only for the network type of vdpa device. This is optional.

       mtu MTU - specifies the mtu for the new vdpa device.  This is applicable only for the network type of vdpa device. This is optional.

   vdpa dev del - Delete the vdpa device.
       DEV - specifies the vdpa device to delete.

   vdpa dev config show - Show configuration of specific device or all devices.
       DEV - specifies the vdpa device to show its configuration.  If this argument is omitted all devices configuration is listed.

	   Format is:
	     VDPA_DEVICE_NAME

   vdpa	 dev  vstats  show - shows vendor specific statistics for the given device and virtqueue index. The information is presented as name-value pairs where
       name is the name of the field and value is a numeric value for it.
       DEV    - specifies the vdpa device to query

       qidx QUEUE_INDEX
	      - specifies the virtqueue index to query

EXAMPLES
       vdpa dev show
	   Shows the all vdpa devices on the system.

       vdpa dev show foo
	   Shows the specified vdpa device.

       vdpa dev add name foo mgmtdev vdpa_sim_net
	   Add the vdpa device named foo on the management device vdpa_sim_net.

       vdpa dev add name foo mgmtdev vdpa_sim_net mac 00:11:22:33:44:55
	   Add the vdpa device named foo on the management device vdpa_sim_net with mac address of 00:11:22:33:44:55.

       vdpa dev add name foo mgmtdev vdpa_sim_net mac 00:11:22:33:44:55 mtu 9000
	   Add the vdpa device named foo on the management device vdpa_sim_net with mac address of 00:11:22:33:44:55 and mtu of 9000 bytes.

       vdpa dev add name foo mgmtdev auxiliary/mlx5_core.sf.1 mac 00:11:22:33:44:55 max_vqp 8
	   Add the vdpa device named foo on the management device auxiliary/mlx5_core.sf.1 with mac address of 00:11:22:33:44:55 and max 8 virtqueue pairs

       vdpa dev del foo
	   Delete the vdpa device named foo which was previously created.

       vdpa dev config show foo
	   Shows the vdpa device configuration of device named foo.

       vdpa dev vstats show vdpa0 qidx 1
	   Shows vendor specific statistics information for vdpa device vdpa0 and virtqueue index 1

SEE ALSO
       vdpa(8), vdpa-mgmtdev(8),

AUTHOR
       Parav Pandit <parav@nvidia.com>

iproute2								  5 Jan 2021								DEVLINK-DEV(8)
