RDMA-LINK(8)								     Linux								  RDMA-LINK(8)

NAME
       rdma-link - rdma link configuration

SYNOPSIS
       devlink [ OPTIONS ] link	 { COMMAND | help }

       OPTIONS := { -V[ersion] | -d[etails] }

       rdma link show [ DEV/PORT_INDEX ]

       rdma link add NAME type TYPE netdev NETDEV

       rdma link delete NAME

       rdma link help

DESCRIPTION
   rdma link show - display rdma link attributes
       DEV/PORT_INDEX - specifies the RDMA link to show.  If this argument is omitted all links are listed.

   rdma link add NAME type TYPE netdev NETDEV - add an rdma link for the specified type to the network device
       NAME - specifies the new name of the rdma link to add

       TYPE - specifies which rdma type to use.	 Link types:

	       rxe - Soft RoCE driver

	       siw - Soft iWARP driver

       NETDEV - specifies the network device to which the link is bound

   rdma link delete NAME - delete an rdma link
       NAME - specifies the name of the rdma link to delete

EXAMPLES
       rdma link show
	   Shows the state of all rdma links on the system.

       rdma link show mlx5_2/1
	   Shows the state of specified rdma link.

       rdma link add rxe_eth0 type rxe netdev eth0
	   Adds a RXE link named rxe_eth0 to network device eth0

       rdma link del rxe_eth0
	   Removes RXE link rxe_eth0

SEE ALSO
       rdma(8), rdma-dev(8), rdma-resource(8), rdma-statistic(8),

AUTHOR
       Leon Romanovsky <leonro@mellanox.com>

iproute2								  06 Jul 2017								  RDMA-LINK(8)
