RDMA-SYSTEM(8)								     Linux								RDMA-SYSTEM(8)

NAME
       rdma-system - RDMA subsystem configuration

SYNOPSIS
       rdma [ OPTIONS ] sys  { COMMAND | help }

       OPTIONS := { -V[ersion] | -d[etails] }

       rdma system show

       rdma system set netns NEWMODE

       rdma system help

DESCRIPTION
   rdma system set - set RDMA subsystem network namespace mode
   rdma system show - display RDMA subsystem network namespace mode
       NEWMODE - specifies the RDMA subsystem mode. Either exclusive or shared.	 When user wants to assign dedicated RDMA device to a particular network name‐
       space, exclusive mode should be set before creating any network namespace. If there are active network namespaces and if one or more RDMA devices ex‐
       ist, changing mode from shared to exclusive returns error code EBUSY.

       When RDMA subsystem is in shared mode, RDMA device is accessible in all network namespace. When RDMA device isolation among multiple network namespaces
       is not needed, shared mode can be used.

       It is preferred to not change the subsystem mode when there is active RDMA traffic running, even though it is supported.

EXAMPLES
       rdma system show
	   Shows the state of RDMA subsystem network namespace mode on the system.

       rdma system set netns exclusive
	   Sets the RDMA subsystem in network namespace exclusive mode. In this mode RDMA devices are visible only in single network namespace.

       rdma system set netns shared
	   Sets the RDMA subsystem in network namespace shared mode. In this mode RDMA devices are shared among network namespaces.

SEE ALSO
       rdma(8), rdma-link(8), rdma-resource(8), network_namespaces(7), namespaces(7),

AUTHOR
       Parav Pandit <parav@mellanox.com>

iproute2								  06 Jul 2017								RDMA-SYSTEM(8)
