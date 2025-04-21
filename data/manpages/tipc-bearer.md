TIPC-BEARER(8)								     Linux								TIPC-BEARER(8)

NAME
       tipc-bearer - show or modify TIPC bearers

SYNOPSIS
       tipc bearer add media udp name NAME remoteip REMOTEIP

       tipc bearer enable [ domain DOMAIN ] [ priority PRIORITY ] media
	       { { eth | ib } device DEVICE } |
	       { udp name NAME localip LOCALIP [ localport LOCALPORT ] [ remoteip REMOTEIP ] [ remoteport REMOTEPORT ] }

       tipc bearer disable media
	       { { eth | ib } device DEVICE } |
	       { udp name NAME }

       tipc bearer set { priority PRIORITY | tolerance TOLERANCE | window WINDOW } media
	       { { eth | ib } device DEVICE } |
	       { udp name NAME }

       tipc bearer get [ priority | tolerance | window ] media
	       { { eth | ib } device DEVICE } |
	       { udp name NAME [ localip | localport | remoteip | remoteport ] }

       tipc bearer list

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show help about last valid command. For example tipc bearer --help will show bearer help and tipc --help will show general help. The position of
	      the option in the string is irrelevant.

DESCRIPTION
   Bearer identification
       media MEDIA
	      Specifies	 the TIPC media type for a particular bearer to operate on.  Different media types have different ways of identifying a unique bearer.
	      For example, ib and eth identify a bearer with a DEVICE while udp identify a bearer with a LOCALIP and a NAME

	      ib - Infiniband

	      eth - Ethernet

	      udp - User Datagram Protocol (UDP)

       name NAME
	      Logical bearer identifier valid for bearers on udp media.

       device DEVICE
	      Physical bearer device valid for bearers on eth and ib media.

   Bearer properties
       domain
	      The addressing domain (region) in which a bearer will establish links and accept link establish requests.

       priority
	      Default link priority inherited by all links subsequently established over a bearer. A single bearer can only host  one  link  to	 a  particular
	      node.  This  means  the default link priority for a bearer typically affects which bearer to use when communicating with a particular node in an
	      multi bearer setup. For more info about link priority see tipc-link(8)

       tolerance
	      Default link tolerance inherited by all links subsequently established over a bearer. For more info about link tolerance see tipc-link(8)

       window
	      Default link window inherited by all links subsequently established over a bearer. For more info about the link window size see tipc-link(8)

   UDP bearer options
       localip LOCALIP
	      Specify a local IP v4/v6 address for a udp bearer.

       localport LOCALPORT
	      Specify the local port for a udp bearer. The default port 6118 is used if no port is specified.

       remoteip REMOTEIP
	      Specify a remote IP for a udp bearer. If no remote IP is specified a udp bearer runs in multicast mode and tries	to  auto-discover  its	neigh‐
	      bours.   The  multicast  IP address is generated based on the TIPC network ID. If a remote IP is specified the udp bearer runs in point-to-point
	      mode.

	      Multiple remoteip addresses can be added via the bearer add command. Adding one or more unicast remoteip addresses to  an	 existing  udp	bearer
	      puts  the bearer in replicast mode where IP multicast is emulated by sending multiple unicast messages to each configured remoteip.  When a peer
	      sees a TIPC discovery message from an unknown peer the peer address is automatically added to the remoteip (replicast) list, thus only one  side
	      of a link needs to be manually configured. A remoteip address cannot be added to a multicast bearer.

       remoteport REMOTEPORT
	      Specify the remote port for a udp bearer. The default port 6118 is used if no port is specified.

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-link(8), tipc-media(8), tipc-nametable(8), tipc-node(8), tipc-peer(8), tipc-socket(8)

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  02 Jun 2015								TIPC-BEARER(8)
