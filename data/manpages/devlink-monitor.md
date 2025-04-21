DEVLINK-MONITOR(8)							     Linux							    DEVLINK-MONITOR(8)

NAME
       devlink-monitor - state monitoring

SYNOPSIS
       devlink monitor [ all | OBJECT-LIST ]

DESCRIPTION
       The devlink utility can monitor the state of devlink devices and ports continuously. This option has a slightly different format. Namely, the monitor
       command is the first in the command line and then the object list.

       OBJECT-LIST is the list of object types that we want to monitor.	 It may contain dev, port, health, trap, trap-group, trap-policer.

       devlink opens Devlink Netlink socket, listens on it and dumps state changes.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-sb(8), devlink-port(8), devlink-health(8), devlink-trap(8),

AUTHOR
       Jiri Pirko <jiri@mellanox.com>

iproute2								  14 Mar 2016							    DEVLINK-MONITOR(8)
