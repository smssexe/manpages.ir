SKB editing action in tc(8)						     Linux						   SKB editing action in tc(8)

NAME
       skbedit - SKB editing action

SYNOPSIS
       tc ... action skbedit [ queue_mapping QUEUE_MAPPING ] [ priority PRIORITY ] [ mark MARK[/MASK] ] [ ptype PTYPE ] [ inheritdsfield ]

DESCRIPTION
       The  skbedit  action allows one to change a packet's associated meta data. It complements the pedit action, which in turn allows one to change parts of
       the packet data itself.

       The most unique feature of skbedit is its ability to decide over which queue of an interface with multiple transmit queues the packet  is  to  be  sent
       out.  The number of available transmit queues is reflected by sysfs entries within /sys/class/net/<interface>/queues with name tx-N (where N is the ac‐
       tual queue number).

OPTIONS
       queue_mapping QUEUE_MAPPING
	      Override the packet's transmit queue. Useful when applied to packets transmitted over MQ-capable network interfaces.  QUEUE_MAPPING  is  an  un‐
	      signed 16bit value in decimal format.

       priority PRIORITY
	      Override	the  packet classification decision.  PRIORITY is either root, none or a hexadecimal major class ID optionally followed by a colon (:)
	      and a hexadecimal minor class ID.

       mark MARK[/MASK]
	      Change the packet's firewall mark value.	MARK is an unsigned 32bit value in automatically detected format (i.e., prefix with '0x' for hexadeci‐
	      mal interpretation, etc.).  MASK defines the 32-bit mask selecting bits of mark value. Default is 0xffffffff.

       ptype PTYPE
	      Override the packet's type. Useful for setting packet type to host when needing to allow ingressing packets with the wrong MAC address but  cor‐
	      rect IP address.	PTYPE is one of: host, otherhost, broadcast, multicast

       inheritdsfield
	      Override	the packet classification decision, and any value specified with priority, using the information stored in the Differentiated Services
	      Field of the IPv6/IPv4 header (RFC2474).

SEE ALSO
       tc(8), tc-pedit(8)

iproute2								  12 Jan 2015						   SKB editing action in tc(8)
