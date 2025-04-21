RDMA-DEV(8)								     Linux								   RDMA-DEV(8)

NAME
       rdma-dev - RDMA device configuration

SYNOPSIS
       rdma [ OPTIONS ] dev  { COMMAND | help }

       OPTIONS := { -V[ersion] | -d[etails] }

       rdma dev show [ DEV ]

       rdma dev set [ DEV ] name NEWNAME

       rdma dev set [ DEV ] netns NSNAME

       rdma dev set [ DEV ] adaptive-moderation [on/off]

       rdma dev help

DESCRIPTION
   rdma dev set - rename RDMA device or set network namespace or set RDMA device adaptive-moderation
   rdma dev show - display RDMA device attributes
       DEV - specifies the RDMA device to show.	 If this argument is omitted all devices are listed.

EXAMPLES
       rdma dev
	   Shows the state of all RDMA devices on the system.

       rdma dev show mlx5_3
	   Shows the state of specified RDMA device.

       rdma dev set mlx5_3 name rdma_0
	   Renames the mlx5_3 device to rdma_0.

       rdma dev set mlx5_3 netns foo
	   Changes the network namespace of RDMA device to foo where foo is previously created using iproute2 ip command.

       rdma dev set mlx5_3 adaptive-moderation [on/off]
	   Sets the state of adaptive interrupt moderation for the RDMA device.
	   This is a global setting for the RDMA device but the value is printed for each CQ individually because the state is constant from CQ allocation.

SEE ALSO
       ip(8), rdma(8), rdma-link(8), rdma-resource(8), rdma-system(8), rdma-statistic(8),

AUTHOR
       Leon Romanovsky <leonro@mellanox.com>

iproute2								  06 Jul 2017								   RDMA-DEV(8)
