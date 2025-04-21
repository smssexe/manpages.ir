DEVLINK-REGION(8)							     Linux							     DEVLINK-REGION(8)

NAME
       devlink-region - devlink address region access

SYNOPSIS
       devlink [ OPTIONS ] region  { COMMAND | help }

       OPTIONS := { -V[ersion] | -n[no-nice-names] }

       devlink region show [ DEV/REGION ]

       devlink region new DEV/REGION [ snapshot SNAPSHOT_ID ]

       devlink region del DEV/REGION snapshot SNAPSHOT_ID

       devlink region dump DEV/REGION snapshot SNAPSHOT_ID

       devlink region read DEV/REGION [ snapshot SNAPSHOT_ID ] address ADDRESS length LENGTH

       devlink region help

DESCRIPTION
   devlink region show - Show all supported address regions names, snapshots and sizes
       DEV/REGION - specifies the devlink device and address-region to query.

   devlink region new - Create a snapshot specified by address-region name and snapshot ID
       DEV/REGION - specifies the devlink device and address-region to snapshot

       snapshot SNAPSHOT_ID - optionally specifies the snapshot ID to assign. If not specified, devlink will assign a unique ID to the snapshot.

   devlink region del - Delete a snapshot specified by address-region name and snapshot ID
       DEV/REGION - specifies the devlink device and address-region to delete the snapshot from

       snapshot SNAPSHOT_ID - specifies the snapshot ID to delete

   devlink region dump - Dump all the available data from a region or from snapshot of a region
       DEV/REGION - specifies the device and address-region to dump from.

       snapshot SNAPSHOT_ID - specifies the snapshot-id of the region to dump.

   devlink region read - Read from a specific region address for a given length
       DEV/REGION - specifies the device and address-region to read from.

       snapshot SNAPSHOT_ID - specifies the snapshot-id of the region to read.

       address ADDRESS - specifies the address to read from.

       length LENGTH - specifies the length of data to read.

EXAMPLES
       devlink region show
	   List available address regions and snapshot.

       devlink region new pci/0000:00:05.0/cr-space
	   Create a new snapshot from cr-space address region from device pci/0000:00:05.0.

       devlink region del pci/0000:00:05.0/cr-space snapshot 1
	   Delete snapshot id 1 from cr-space address region from device pci/0000:00:05.0.

       devlink region dump pci/0000:00:05.0/cr-space snapshot 1
	   Dump the snapshot taken from cr-space address region with ID 1

       devlink region read pci/0000:00:05.0/cr-space snapshot 1 address 0x10 length 16
	   Read from address 0x10, 16 Bytes of snapshot ID 1 taken from cr-space address region

SEE ALSO
       devlink(8), devlink-dev(8), devlink-port(8), devlink-monitor(8),

AUTHOR
       Alex Vesker <valex@mellanox.com>

iproute2								  10 Jan 2018							     DEVLINK-REGION(8)
