TIPC-NAMETABLE(8)							     Linux							     TIPC-NAMETABLE(8)

NAME
       tipc-nametable - show TIPC nametable

SYNOPSIS
       tipc nametable show

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help

       -j, -json
	      Output results in JavaScript Object Notation (JSON).

       -p, -pretty
	      The default JSON format is compact and more efficient to parse but hard for most users to read.  This flag adds indentation for readability.

	      Show help about last valid command. For example tipc nametable --help will show nametable help and tipc --help will show general help. The posi‐
	      tion of the option in the string is irrelevant.

DESCRIPTION
       The nametable shows TIPC publication information.

   Nametable format
       Type
	      The 32-bit type field of the port name. The type field often indicates the class of service provided by a port.

       Lower
	      The lower bound of the 32-bit instance field of the port name.  The instance field is often used as as a sub-class indicator.

       Upper
	      The  upper  bound of the 32-bit instance field of the port name.	The instance field is often used as as a sub-class indicator.  A difference in
	      lower and upper means the socket is bound to the port name range [lower,upper]

       Port Identity
	      The unique socket (port) identifier within the TIPC cluster. The port identity consists of a node identity followed by a socket  reference  num‐
	      ber.

       Publication
	      The publication ID is a random number used internally to represent a publication.

       Scope
	      The  publication	scope  specifies  the  visibility of a bound port name.	 The scope can be specified to comprise three different domains: node,
	      cluster and zone.	 Applications residing within the specified scope can see and access the port using the displayed port name.

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-bearer(8), tipc-link(8), tipc-media(8), tipc-node(8), tipc-peer(8), tipc-socket(8)

REPORTING BUGS
       Report any bugs to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.	  You  do  not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  02 Jun 2015							     TIPC-NAMETABLE(8)
