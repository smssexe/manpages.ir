RDMA-RESOURCE(8)							     Linux							      RDMA-RESOURCE(8)

NAME
       rdma-resource - rdma resource configuration

SYNOPSIS
       rdma [ OPTIONS ] RESOURCE { COMMAND | help }

       RESOURCE := { cm_id | cq | mr | pd | qp | ctx | srq }

       OPTIONS := { -j[son] | -d[etails] }

       rdma resource show [ DEV/PORT_INDEX ]

       rdma resource help

DESCRIPTION
   rdma resource show - display rdma resource tracking information
       DEV/PORT_INDEX - specifies the RDMA link to show.  If this argument is omitted all links are listed.

EXAMPLES
       rdma resource show
	   Shows summary for all devices on the system.

       rdma resource show mlx5_2
	   Shows the state of specified rdma device.

       rdma res show qp link mlx5_4
	   Get all QPs for the specific device.

       rdma res show qp link mlx5_4/1
	   Get QPs of specific port.

       rdma res show qp link mlx5_4/0
	   Provide illegal port number (0 is illegal).

       rdma res show qp link mlx5_4/-
	   Get QPs which have not assigned port yet.

       rdma res show qp link mlx5_4/- -d
	   Detailed view.

       rdma res show qp link mlx5_4/- -dd
	   Detailed view including driver-specific details.

       rdma res show qp link mlx5_4/1 lqpn 0-6
	   Limit to specific Local QPNs.

       rdma res show qp link mlx5_4/1 lqpn 6 -r
	   Driver specific details in raw format.

       rdma resource show cm_id dst-port 7174
	   Show CM_IDs with destination ip port of 7174.

       rdma resource show cm_id src-addr 172.16.0.100
	   Show CM_IDs bound to local ip address 172.16.0.100

       rdma resource show cq pid 30489
	   Show CQs belonging to pid 30489

       rdma resource show ctx ctxn 1
	   Show contexts that have index equal to 1.

       rdma resource show srq lqpn 5-7
	   Show SRQs that the QPs with lqpn 5-7 are associated with.

SEE ALSO
       rdma(8), rdma-dev(8), rdma-link(8), rdma-statistic(8),

AUTHOR
       Leon Romanovsky <leonro@mellanox.com>

iproute2								  26 Dec 2017							      RDMA-RESOURCE(8)
