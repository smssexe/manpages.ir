VDPA(8)									     Linux								       VDPA(8)

NAME
       vdpa - vdpa management tool

SYNOPSIS
       vdpa [ OPTIONS ] { dev|mgmtdev } { COMMAND | help }

OPTIONS
       -V, --Version
	      Print the version of the vdpa utility and exit.

       -j, --json
	      Generate JSON output.

       -p, --pretty
	      When combined with -j generate a pretty JSON output.

   OBJECT
       dev    - vdpa device.

       mgmtdev
	      - vdpa management device.

   COMMAND
       Specifies the action to perform on the object.  The set of possible actions depends on the object type.	It is possible to show (or list ) objects. The
       help command is available for all objects. It prints out a list of available commands and argument syntax conventions.

       If no command is given, some default command is assumed.	 Usually it is show or, if the objects of this class cannot be listed, help.

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       vdpa-dev(8), vdpa-mgmtdev(8),

REPORTING BUGS
       Report  any  bugs  to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.  You do not
       have to be subscribed to the list to send a message there.

AUTHOR
       Parav Pandit <parav@nvidia.com>

iproute2								  5 Jan 2021								       VDPA(8)
