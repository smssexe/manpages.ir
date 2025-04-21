Connmark retriever action in tc(8)					     Linux					    Connmark retriever action in tc(8)

NAME
       connmark - netfilter connmark retriever action

SYNOPSIS
       tc ... action connmark [ zone u16_zone_index ] [ CONTROL ] [ index u32_index ]

       CONTROL := { reclassify | pipe | drop | continue | ok }

DESCRIPTION
       The connmark action is used to restore the connection's mark value into the packet's fwmark.

OPTIONS
       zone u16_zone_index
	      Specify the conntrack zone when doing conntrack lookups for packets.  u16_zone_index is a 16bit unsigned decimal value.

       CONTROL
	      How to continue after executing this action.

	      reclassify
		     Restarts classification by jumping back to the first filter attached to this action's parent.

	      pipe   Continue with the next action, this is the default.

	      drop
	      shot   Packet will be dropped without running further actions.

	      continue
		     Continue classification with next filter in line.

	      pass   Return to calling qdisc for packet processing. This ends the classification process.

       index u32_index
	      Specify an index for this action in order to being able to identify it in later commands.	 u32_index is a 32bit unsigned decimal value.

SEE ALSO
       tc(8)

iproute2								  11 Jan 2016					    Connmark retriever action in tc(8)
