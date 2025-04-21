TIPC-NODE(8)								     Linux								  TIPC-NODE(8)

NAME
       tipc-node - modify and show local node parameters or list peer nodes

SYNOPSIS
       tipc node set { address ADDRESS | netid NETID }

       tipc node get { address | netid }

       tipc node list

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show help about last valid command. For example tipc node --help will show node help and tipc --help will show general help. The position of the
	      option in the string is irrelevant.

DESCRIPTION
   Node parameters
       address
	      The TIPC logical address. On the form x.y.z where x, y and z are unsigned integers.

       netid
	      Network identity. Can by used to create individual TIPC clusters on the same media.

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-bearer(8), tipc-link(8), tipc-media(8), tipc-nametable(8), tipc-peer(8), tipc-socket(8)

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  02 Jun 2015								  TIPC-NODE(8)
