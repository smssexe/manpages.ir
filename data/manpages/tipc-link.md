TIPC-LINK(8)								     Linux								  TIPC-LINK(8)

NAME
       tipc-link - show links or modify link properties

SYNOPSIS
       tipc link set
	       [ { priority PRIORITY | tolerance TOLERANCE | window WINDOW } link LINK ] |
	       [ { broadcast [ BROADCAST  | REPLICAST  | AUTOSELECT [ ratio SIZE ] ] } ]

       tipc link get
	       [ { priority | tolerance | window } link LINK ] |
	       [ { broadcast } ]

       tipc link statistics { show [ link LINK ] | reset link LINK }

       tipc link list

       tipc link monitor set { threshold }

       tipc link monitor get { threshold }

       tipc link monitor summary

       tipc link monitor list
	       [ media	{ eth | ib } device DEVICE ] |
	       [ media udp name NAME ]

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show help about last valid command. For example tipc link --help will show link help and tipc --help will show general help. The position of the
	      option in the string is irrelevant.

       -j, -json
	      Output results in JavaScript Object Notation (JSON).

       -p, -pretty
	      The default JSON format is compact and more efficient to parse but hard for most users to read.  This flag adds indentation for readability.

DESCRIPTION
   Link statistics
       ACTIVE link state
	      An  ACTIVE link is serving traffic. Two links to the same node can become ACTIVE if they have the same link priority.  If there is more than two
	      links with the same priority the additional links will be put in STANDBY state.

       STANDBY link state
	      A STANDBY link has lower link priority than an ACTIVE link. A STANDBY link has control traffic flowing and is ready to take over should the  AC‐
	      TIVE link(s) go down.

       MTU
	      The Maximum Transmission Unit. The two endpoints advertise their default or configured MTU at initial link setup and will agree to use the lower
	      of the two values should they differ.

       Packets
	      The total amount of transmitted or received TIPC packets on a link. Including fragmented and bundled packets.

       Fragments
	      Represented  in  the  form fragments/fragmented.	Where fragmented is the amount of data messages which have been broken into fragments.	Subse‐
	      quently the fragments are the total amount of packets that the fragmented messages has been broken into.

       Bundles
	      Represented in the form bundles/bundled.	If a link becomes congested the link will attempt to bundle data from small bundled packets into  bun‐
	      dles of full MTU size packets before they are transmitted.

       Profile
	      Shows  the average packet size in octets/bytes for a sample of packets. It also shows the packet size distribution of the sampled packets in the
	      intervals

	      0-64 bytes
	      64-256 bytes
	      256-1024 bytes
	      1024-4096 bytes
	      4096-16384 bytes
	      16384-32768 bytes
	      32768-66000 bytes

       Message counters

	      states - Number of link state messages

	      probes - Link state messages with probe flag set. Typically sent when a link is idle

	      nacks - Number of negative acknowledgement (NACK) packets sent and received by the link

	      defs - Number of packets received out of order

	      dups - Number of duplicate packets received

       Congestion link
	      The number of times an application has tried to send data when the TIPC link was congested

       Send queue
	      Max is the maximum amount of messages that has resided in the out queue during the statistics collection period of a link.

	      Avg is the average outqueue size during the lifetime of a link.

   Link properties
       priority
	      The priority between logical TIPC links to a particular node. Link priority can range from 0 (lowest) to 31 (highest).

       tolerance
	      Link tolerance specifies the maximum time in milliseconds that TIPC will allow a communication problem to exist before taking the link down. The
	      default value is 1500 milliseconds.

       window
	      The link window controls how many unacknowledged messages a link endpoint can have in its transmit queue before TIPC's congestion control mecha‐
	      nism is activated.

   Monitor properties
       threshold
	      The threshold specifies the cluster size exceeding which the link monitoring algorithm will switch from "full-mesh" to  "overlapping-ring".   If
	      set  of  0  the overlapping-ring monitoring is always on and if set to a value larger than anticipated cluster size the overlapping-ring is dis‐
	      abled.  The default value is 32.

   Monitor information
       table_generation
	      Represents the event count in a node's local monitoring list. It steps every time something changes in the local monitor list, including changes
	      in the local domain.

       cluster_size
	      Represents the current count of cluster members.

       algorithm
	      The current supervision algorithm used for neighbour monitoring for the bearer.  Possible values are full-mesh or overlapping-ring.

       status
	      The node status derived by the local node.  Possible status are up or down.

       monitored
	      Represent the type of monitoring chosen by the local node.  Possible values are direct or indirect.

       generation
	      Represents the domain generation which is the event count in a node's local domain. Every time something changes (peer  add/remove/up/down)  the
	      domain generation is stepped and a new version of node record is sent to inform the neighbors about this change. The domain generation helps the
	      receiver of a domain record to know if it should ignore or process the record.

       applied_node_status
	      The  node	 status	 reported  by the peer node for the succeeding peers in the node list. The Node list is a circular list of ascending addresses
	      starting with the local node.  Possible status are: U or D. The status U implies up and D down.

       [non_applied_node:status]
	      Represents the nodes and their status as reported by the peer node.  These nodes were not applied to the monitoring list	for  this  peer	 node.
	      They are usually transient and occur during the cluster startup phase or network reconfiguration.	 Possible status are: U or D. The status U im‐
	      plies up and D down.

   Broadcast properties
       BROADCAST
	      Forces all multicast traffic to be transmitted via broadcast only, irrespective of cluster size and number of destinations.

       REPLICAST
	      Forces all multicast traffic to be transmitted via replicast only, irrespective of cluster size and number of destinations.

       AUTOSELECT
	      Auto switching to broadcast or replicast depending on cluster size and destination node number.

       ratio SIZE
	      Set the AUTOSELECT criteria, percentage of destination nodes vs cluster size.

EXAMPLES
       tipc link monitor list
	   Shows the link monitoring information for cluster members on device data0.

       tipc link monitor summary
	   The monitor summary command prints the basic attributes.

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-media(8), tipc-bearer(8), tipc-nametable(8), tipc-node(8), tipc-peer(8), tipc-socket(8)

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  22 Mar 2019								  TIPC-LINK(8)
