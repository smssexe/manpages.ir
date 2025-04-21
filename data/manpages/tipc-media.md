TIPC-MEDIA(8)								     Linux								 TIPC-MEDIA(8)

NAME
       tipc-media - list or modify media properties

SYNOPSIS
       tipc media set { priority PRIORITY | tolerance TOLERANCE | window WINDOW } media MEDIA

       tipc media get { priority | tolerance | window } media MEDIA

       tipc media list

OPTIONS
       Options (flags) that can be passed anywhere in the command chain.

       -h, --help
	      Show  help  about last valid command. For example tipc media --help will show media help and tipc --help will show general help. The position of
	      the option in the string is irrelevant.

DESCRIPTION
   Media properties
       priority
	      Default link priority inherited by all bearers subsequently enabled on a media. For more info about link priority see tipc-link(8)

       tolerance
	      Default link tolerance inherited by all bearers subsequently enabled on a media. For more info about link tolerance see tipc-link(8)

       window
	      Default link window inherited by all bearers subsequently enabled on a media. For more info about link window see tipc-link(8)

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       tipc(8), tipc-bearer(8), tipc-link(8), tipc-nametable(8), tipc-node(8), tipc-peer(8), tipc-socket(8)

REPORTING BUGS
       Report any bugs to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.	  You  do  not
       have to be subscribed to the list to send a message there.

AUTHOR
       Richard Alpe <richard.alpe@ericsson.com>

iproute2								  02 Jun 2015								 TIPC-MEDIA(8)
