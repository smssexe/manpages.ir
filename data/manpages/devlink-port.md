DEVLINK-PORT(8)								     Linux							       DEVLINK-PORT(8)

NAME
       devlink-port - devlink port configuration

SYNOPSIS
       devlink [ OPTIONS ] port	 { COMMAND | help }

       OPTIONS := { -V[ersion] | -n[no-nice-names] }

       devlink port set DEV/PORT_INDEX [ type { eth | ib | auto } ]

       devlink port split DEV/PORT_INDEX count COUNT

       devlink port unsplit DEV/PORT_INDEX

       devlink port show [ DEV/PORT_INDEX ]

       devlink port health { show | recover | diagnose | dump | set }

       devlink port add { DEV | DEV/PORT_INDEX } [ flavour FLAVOUR ] [ pfnum PFNUMBER ] [ sfnum SFNUMBER ] [ controller CNUM ]

       devlink port del DEV/PORT_INDEX

       devlink port function set DEV/PORT_INDEX [ hw_addr ADDR ] [ state { active | inactive } ]

       devlink port function rate { show | set | add | del | help }

       devlink dev param set DEV/PORT_INDEX name PARAMETER value VALUE cmode { runtime | driverinit | permanent }

       devlink dev param show [ DEV/PORT_INDEX name PARAMETER ]

       devlink port help

DESCRIPTION
   devlink port set - change devlink port attributes
       DEV/PORT_INDEX - specifies the devlink port to operate on.

	   Format is:
	     BUS_NAME/BUS_ADDRESS/PORT_INDEX

       type { eth | ib | auto }
	      set port type

	      eth - Ethernet

	      ib - Infiniband

	      auto - autoselect

   devlink port split - split devlink port into more
       DEV/PORT_INDEX - specifies the devlink port to operate on.

       count COUNT
	      number of ports to split to.

   devlink port unsplit - unsplit previously split devlink port
       Could be performed on any split port of the same split group.

       DEV/PORT_INDEX - specifies the devlink port to operate on.

   devlink port show - display devlink port attributes
       DEV/PORT_INDEX - specifies the devlink port to show.  If this argument is omitted all ports are listed.

   devlink port health - devlink health reporting and recovery
       Is an alias for devlink-health(8).

   devlink port add - add a devlink port
       DEV - specifies the devlink device to operate on. or

       DEV/PORT_INDEX  - specifies the devlink port index to use for the requested new port.  This is optional. When omitted, driver allocates unique port in‐
       dex.

       flavour { pcipf | pcisf }
	      set port flavour

	      pcipf - PCI PF port

	      pcisf - PCI SF port

       pfnum PFNUMBER
	      Specifies PCI pfnumber to use on which a SF device to create

       sfnum SFNUMBER
	      Specifies sfnumber to assign to the device of the SF.  This field is optional for those devices which supports auto assignment of the SF number.

       controller CNUM
	      Specifies controller number for which the SF port is created.  This field is optional. It is used only when SF port is created for the  external
	      controller.

   devlink port function set - Set the port function attribute(s).
       DEV/PORT_INDEX - specifies the devlink port to operate on.

       hw_addr ADDR
	      Hardware address of the function to set. This is a Ethernet MAC address when port type is Ethernet.

       state { active | inactive }
	      New state of the function to change to.

	      active - Once configuration of the function is done, activate the function.

	      inactive - To inactivate the function and its device(s), set to inactive.

   devlink port del - delete a devlink port
       DEV/PORT_INDEX - specifies the devlink port to delete.

   devlink port param set - set new value to devlink port configuration parameter
       DEV/PORT_INDEX - specifies the devlink port to operate on.

       name PARAMETER
	      Specify parameter name to set.

       value VALUE
	      New value to set.

       cmode { runtime | driverinit | permanent }
	      Configuration mode in which the new value is set.

	      runtime - Set new value while driver is running. This configuration mode doesn't require any reset to apply the new value.

	      driverinit - Set new value which will be applied during driver initialization. This configuration mode requires restart driver by devlink reload
	      command to apply the new value.

	      permanent - New value is written to device's non-volatile memory. This configuration mode requires hard reset to apply the new value.

   devlink port param show - display devlink port supported configuration parameters attributes
       DEV/PORT_INDEX - specifies the devlink port to operate on.

       name PARAMETER Specify parameter name to show.  If this argument, as well as port index, are omitted - all parameters supported by devlink device ports
       are listed.

   devlink port function rate - manage devlink rate objects
       Is an alias for devlink-rate(8).

EXAMPLES
       devlink port show
	   Shows the state of all devlink ports on the system.

       devlink port show pci/0000:01:00.0/1
	   Shows the state of specified devlink port.

       devlink port set pci/0000:01:00.0/1 type eth
	   Set type of specified devlink port to Ethernet.

       devlink port split pci/0000:01:00.0/1 count 4
	   Split the specified devlink port into four ports.

       devlink port unsplit pci/0000:01:00.0/1
	   Unplit the specified previously split devlink port.

       devlink port health show
	   Shows status and configuration of all supported reporters registered on all devlink ports.

       devlink port health show pci/0000:01:00.0/1 reporter tx
	   Shows status and configuration of tx reporter registered on pci/0000:01:00.0/1 devlink port.

       devlink port add pci/0000:06:00.0 flavour pcisf pfnum 0 sfnum 88
	   Add	a  devlink  port  of  flavour PCI SF on PCI PF having number 0 with SF number 88.  To make use of the function an example sequence is to add a
	   port, configure the function attribute and activate the function. Once function usage is completed, inactivate the function and finally delete  the
	   port.  When	there  is desire to reuse the port without deletion, it can be reconfigured and activated again when function is in inactive state and
	   function's operational state is detached.

       devlink port del pci/0000:06:00.0/1
	   Delete previously created devlink port. It is recommended to first deactivate the function if the function supports state management.

       devlink port function set pci/0000:01:00.0/1 hw_addr 00:00:00:11:22:33
	   Configure hardware address of the PCI function represented by devlink port.	If the port supports change in function state, hardware	 address  must
	   be configured before activating the function.

       devlink port function set pci/0000:01:00.0/1 state active
	   Activate the function. This will initiate the function enumeration and driver loading.

       devlink port function set pci/0000:01:00.0/1 state inactive
	   Deactivate the function. This will initiate the function teardown which results in driver unload and device removal.

       devlink port function set pci/0000:01:00.0/1 hw_addr 00:00:00:11:22:33 state active
	   Configure  hardware	address	 and also active the function. When a function is activated together with other configuration in a single command, all
	   the configuration is applied first before changing the state to active.

       devlink dev param show
	   Shows (dumps) all the port parameters across all the devices registered in the devlink.

       devlink dev param set pci/0000:01:00.0/1 name internal_error_reset value true cmode runtime
	   Sets the parameter internal_error_reset of specified devlink port (#1) to true.

       devlink port add pci/0000:06:00.0 flavour pcisf pfnum 0 sfnum 88 controller 1
	   Add a devlink port of flavour PCI SF on controller 1 which has PCI PF of number 0 with SF number 88. To make use of the  function  an  example  se‐
	   quence  is to add a port, configure the function attribute and activate the function. Once the function usage is completed, deactivate the function
	   and finally delete the port. When there is desire to reuse the port without deletion, it can be reconfigured and activated again when  function  is
	   in inactive state and function's operational state is detached.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-sb(8), devlink-monitor(8), devlink-health(8),

AUTHOR
       Jiri Pirko <jiri@mellanox.com>

iproute2								  14 Mar 2016							       DEVLINK-PORT(8)
