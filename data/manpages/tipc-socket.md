TIPC-SOCKET(8)								     Linux								TIPC-SOCKET(8)

NAME
       tipc-socket - show TIPC socket (port) information

SYNOPSIS
       tipc socket list

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show help about last valid command. For example tipc socket --help will show socket help and tipc --help will show general help. The position of
	      the option in the string is irrelevant.

DESCRIPTION
       A TIPC socket is represented by an unsigned integer.

	  Bound state
	      A bound socket has a logical TIPC port name associated with it.

	  Connected state
	      A connected socket is directly connected to another socket creating a point to point connection between TIPC sockets. If the connection to X was
	      made using a logical port name Y that name will show up as connected to X via Y

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-bearer(8) tipc-link(8), tipc-media(8), tipc-nametable(8), tipc-node(8),

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  02 Jun 2015								TIPC-SOCKET(8)
