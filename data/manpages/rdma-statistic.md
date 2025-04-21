RDMA-STATISTIC(8)							     Linux							     RDMA-STATISTIC(8)

NAME
       rdma-statistic - RDMA statistic counter configuration

SYNOPSIS
       rdma [ OPTIONS ] statistic { COMMAND | help }

       rdma statistic { OBJECT } show

       rdma statistic [ OBJECT ] show link [ DEV/PORT_INDX ] [ FILTER_NAME FILTER_VALUE ]

       rdma statistic OBJECT mode

       rdma statistic OBJECT set COUNTER_SCOPE [ DEV/PORT_INDEX ] auto { CRITERIA | off }

       rdma statistic OBJECT bind COUNTER_SCOPE [ DEV/PORT_INDEX ] [ OBJECT-ID ] [ COUNTER-ID ]

       rdma statistic OBJECT unbind COUNTER_SCOPE [ DEV/PORT_INDEX ] [ COUNTER-ID ] [ OBJECT-ID ]

       rdma statistic mode [ supported ] link [ DEV/PORT_INDEX ]

       rdma statistic set link [ DEV/PORT_INDEX ] optional-counters [ OPTIONAL-COUNTERS ]

       rdma statistic unset link [ DEV/PORT_INDEX ] optional-counters

       COUNTER_SCOPE := { link | dev }

       OBJECT := { qp | mr }

       CRITERIA := { type | pid }

       FILTER_NAME := { cntn | lqpn | pid | qp-type }

DESCRIPTION
   rdma statistic [object] show - Queries the specified RDMA device for RDMA and driver-specific statistics. Show the default hw counters if object is not
       specified
       DEV - specifies counters on this RDMA device to show.

       PORT_INDEX - specifies counters on this RDMA port to show.

       FILTER_NAME - specifies a filter to show only the results matching it.

   rdma statistic <object> set - configure counter statistic auto-mode for a specific device/port
       In auto mode all objects belong to one category are bind automatically to a single counter set. The "off" is global for all auto modes together. Not
       applicable for MR's.

   rdma statistic <object> bind - manually bind an object (e.g., a qp) with a counter
       When bound the statistics of this object are available in this counter. Not applicable for MR's.

   rdma statistic <object> unbind - manually unbind an object (e.g., a qp) from the counter previously bound
       When unbound the statistics of this object are no longer available in this counter; And if object id is not specified then all objects on this counter
       will be unbound. Not applicable for MR's.

       COUNTER-ID - specifies the id of the counter to be bound.  If this argument is omitted then a new counter will be allocated.

   rdma statistic mode - Display the enabled optional counters for each link.
   rdma statistic mode supported - Display the supported optional counters for each link.
   rdma statistic set - Enable a set of optional counters for a specific device/port.
       OPTIONAL-COUNTERS - specifies the name of the optional counters to enable. Optional counters that are not specified will be disabled. Note that op‐
       tional counters are driver-specific.

   rdma statistic unset - Disable all optional counters for a specific device/port.
EXAMPLES
       rdma statistic show
	   Shows the state of the default counter of all RDMA devices on the system.

       rdma statistic show link mlx5_2/1
	   Shows the state of the default counter of specified RDMA port

       rdma statistic qp show
	   Shows the state of all qp counters of all RDMA devices on the system.

       rdma statistic qp show link mlx5_2/1
	   Shows the state of all qp counters of specified RDMA port.

       rdma statistic qp show link mlx5_2 pid 30489
	   Shows the state of all qp counters of specified RDMA port and belonging to pid 30489

       rdma statistic qp show link mlx5_2 qp-type UD
	   Shows the state of all qp counters of specified RDMA port and with QP type UD

       rdma statistic qp mode
	   List current counter mode on all devices

       rdma statistic qp mode link mlx5_2/1
	   List current counter mode of device mlx5_2 port 1

       rdma statistic qp set link mlx5_2/1 auto type on
	   On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same qp type.

       rdma statistic qp set link mlx5_2/1 auto pid on
	   On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same pid.

       rdma statistic qp set link mlx5_2/1 auto pid,type on
	   On device mlx5_2 port 1, for each new user QP bind it with a counter automatically. Per counter for QPs with same pid and same type.

       rdma statistic qp set link mlx5_2/1 auto off
	   Turn-off auto mode on device mlx5_2 port 1. The allocated counters can be manually accessed.

       rdma statistic qp bind link mlx5_2/1 lqpn 178
	   On device mlx5_2 port 1, allocate a counter and bind the specified qp on it

       rdma statistic qp unbind link mlx5_2/1 cntn 4 lqpn 178
	   On device mlx5_2 port 1, bind the specified qp on the specified counter

       rdma statistic qp unbind link mlx5_2/1 cntn 4
	   On device mlx5_2 port 1, unbind all QPs on the specified counter. After that this counter will be released automatically by the kernel.

       rdma statistic show mr
	   List all currently allocated MR's and their counters.

       rdma statistic show mr mrn 6
	   Dump a specific MR statistics with mrn 6. Dumps nothing if does not exists.

       rdma statistic mode link mlx5_2/1
	   Display the optional counters that was enabled on mlx5_2/1.

       rdma statistic mode supported link mlx5_2/1
	   Display the optional counters that mlx5_2/1 supports.

       rdma statistic set link mlx5_2/1 optional-counters cc_rx_ce_pkts,cc_rx_cnp_pkts
	   Enable the cc_rx_ce_pkts,cc_rx_cnp_pkts counters on device mlx5_2 port 1.

       rdma statistic unset link mlx5_2/1 optional-counters
	   Disable all the optional counters on device mlx5_2 port 1.

SEE ALSO
       rdma(8), rdma-dev(8), rdma-link(8), rdma-resource(8),

AUTHORS
       Mark Zhang <markz@mellanox.com>
       Erez Alfasi <ereza@mellanox.com>
       Neta Ostrovsky <netao@nvidia.com>

iproute2								 27 June 2019							     RDMA-STATISTIC(8)
