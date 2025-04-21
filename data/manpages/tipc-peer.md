TIPC-PEER(8)								     Linux								  TIPC-PEER(8)

NAME
       tipc-peer - modify peer information

SYNOPSIS
       tipc peer remove address ADDRESS

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show help about last valid command. For example tipc peer --help will show peer help and tipc --help will show general help. The position of the
	      option in the string is irrelevant.

DESCRIPTION
   Peer remove
       Remove an offline peer node from the local data structures. The peer is identified by its address

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-bearer(8), tipc-link(8), tipc-media(8), tipc-nametable(8), tipc-node(8), tipc-socket(8)

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  04 Dec 2015								  TIPC-PEER(8)
