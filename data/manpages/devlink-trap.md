DEVLINK-TRAP(8)								     Linux							       DEVLINK-TRAP(8)

NAME
       devlink-trap - devlink trap configuration

SYNOPSIS
       devlink [ OPTIONS ] trap { COMMAND | help }

       OPTIONS := { -v[erbose] | -s[tatistics] }

       devlink trap show [ DEV trap TRAP ]

       devlink trap set DEV trap TRAP [ action { trap | drop | mirror } ]

       devlink trap group show [ DEV group GROUP ]

       devlink trap group set DEV group GROUP [ action { trap | drop | mirror } ]
	       [ policer POLICER ] [ nopolicer ]

       devlink trap policer set DEV policer POLICER [ rate RATE ] [ burst BURST ]

       devlink trap help

DESCRIPTION
   devlink trap show - display available packet traps and their attributes
       DEV - specifies the devlink device from which to show packet traps.  If this argument is omitted all packet traps of all devices are listed.

       trap TRAP - specifies the packet trap.  Only applicable if a devlink device is also specified.

   devlink trap set - set attributes of a packet trap
       DEV - specifies the devlink device the packet trap belongs to.

       trap TRAP - specifies the packet trap.

       action { trap | drop | mirror }
	      packet trap action.

	      trap - the sole copy of the packet is sent to the CPU.

	      drop - the packet is dropped by the underlying device and a copy is not sent to the CPU.

	      mirror - the packet is forwarded by the underlying device and a copy is sent to the CPU.

   devlink trap group show - display available packet trap groups and their attributes
       DEV  -  specifies  the  devlink	device	from  which to show packet trap groups.	 If this argument is omitted all packet trap groups of all devices are
       listed.

       group GROUP - specifies the packet trap group.  Only applicable if a devlink device is also specified.

   devlink trap group set - set attributes of a packet trap group
       DEV - specifies the devlink device the packet trap group belongs to.

       group GROUP - specifies the packet trap group.

       action { trap | drop | mirror }
	      packet trap action. The action is set for all the packet traps member in the trap group. The actions of non-drop traps cannot be changed and are
	      thus skipped.

       policer POLICER
	      packet trap policer. The policer to bind to the packet trap group. A value of "0" will unbind the currently bound policer.

       nopolicer
	      Unbind packet trap policer from the packet trap group.

   devlink trap policer set - set attributes of packet trap policer
       DEV - specifies the devlink device the packet trap policer belongs to.

       policer POLICER - specifies the packet trap policer.

       rate RATE - packet trap policer rate in packets per second.

       burst BURST - packet trap policer burst size in packets.

EXAMPLES
       devlink trap show
	   List available packet traps.

       devlink trap group show
	   List available packet trap groups.

       devlink -vs trap show pci/0000:01:00.0 trap source_mac_is_multicast
	   Show attributes and statistics of a specific packet trap.

       devlink -s trap group show pci/0000:01:00.0 group l2_drops
	   Show attributes and statistics of a specific packet trap group.

       devlink trap set pci/0000:01:00.0 trap source_mac_is_multicast action trap
	   Set the action of a specific packet trap to 'trap'.

       devlink trap policer show
	   List available packet trap policers.

       devlink -s trap policer show pci/0000:01:00.0 policer 1
	   Show attributes and statistics of a specific packet trap policer.

       devlink trap policer set pci/0000:01:00.0 policer 1 rate 1000 burst 128
	   Set the rate and burst size of a specific packet trap policer.

SEE ALSO
       devlink(8), devlink-dev(8), devlink-monitor(8),

AUTHOR
       Ido Schimmel <idosch@mellanox.com>

iproute2								 2 August 2019							       DEVLINK-TRAP(8)
