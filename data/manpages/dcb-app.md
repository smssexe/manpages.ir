DCB-ETS(8)								     Linux								    DCB-ETS(8)

NAME
       dcb-app - show / manipulate application priority table of the DCB (Data Center Bridging) subsystem

SYNOPSIS
       dcb [ OPTIONS ] app { COMMAND | help }

       dcb app	{  show	 |  flush  }  dev DEV [ default-prio ] [ ethtype-prio ] [ stream-port-prio ] [ dgram-port-prio ] [ port-prio ] [ dscp-prio ]

       dcb ets	{  add	|  del	|  replace  }  dev DEV [ default-prio PRIO-LIST ] [ ethtype-prio ET-MAP ] [ stream-port-prio PORT-MAP ] [ dgram-port-prio
	       PORT-MAP ] [ port-prio PORT-MAP ] [ dscp-prio DSCP-MAP ]

       PRIO-LIST := [ PRIO-LIST ] PRIO

       ET-MAP := [ ET-MAP ] ET-MAPPING

       ET-MAPPING := ET:PRIO

       PORT-MAP := [ PORT-MAP ] PORT-MAPPING

       PORT-MAPPING := PORT:PRIO

       DSCP-MAP := [ DSCP-MAP ] DSCP-MAPPING

       DSCP-MAPPING := { DSCP | all }:PRIO

       ET := { 0x600 .. 0xffff }

       PORT := { 1 .. 65535 }

       DSCP := { 0 .. 63 }

       PRIO := { 0 .. 7 }

DESCRIPTION
       dcb app is used to configure APP table, or application priority table in the DCB (Data Center Bridging) subsystem. The APP table is used to assign pri‐
       ority to traffic based on value in one of several headers: EtherType, L4 destination port, or DSCP. It also allows configuration of port-default prior‐
       ity that is chosen if no other prioritization rule applies.

       DCB APP entries are 3-tuples of selector, protocol ID, and priority. Selector is an enumeration that picks one of the prioritization namespaces. Cur‐
       rently it mostly corresponds to configurable parameters described below. Protocol ID is a value in the selector namespace. E.g. for EtherType selector,
       protocol IDs are the individual EtherTypes, for DSCP they are individual code points. The priority is the priority that should be assigned to traffic
       that matches the selector and protocol ID.

       The APP table is a set of DCB APP entries. The only requirement is that duplicate entries are not added. Notably, it is valid to have conflicting pri‐
       ority assignment for the same selector and protocol ID. For example, the set of two APP entries (DSCP, 10, 1) and (DSCP, 10, 2), where packets with
       DSCP of 10 should get priority of both 1 and 2, form a well-defined APP table. The dcb app tool allows low-level management of the app table by adding
       and deleting individual APP 3-tuples through add and del commands. On the other other hand, the command replace does what one would typically want in
       this situation--first adds the new configuration, and then removes the obsolete one, so that only one prioritization is in effect for a given selector
       and protocol ID.

COMMANDS
       show   Display all entries with a given selector. When no selector is given, shows all APP table entries categorized per selector.

       flush  Remove all entries with a given selector. When no selector is given, removes all APP table entries.

       add
       del    Add and, respectively, remove individual APP 3-tuples to and from the DCB APP table.

       replace
	      Take  the	 list of entries mentioned as parameter, and add those that are not present in the APP table yet. Then remove those entries, whose se‐
	      lector and protocol ID have been mentioned as parameter, but not with the exact same priority. This has the effect of, for  the  given  selector
	      and protocol ID, causing that the table only contains the priority (or priorities) given as parameter.

PARAMETERS
       The  following table shows parameters in a way that they would be used with add, del and replace commands. For show and flush, the parameter name is to
       be used as a simple keyword without further arguments.

       default-prio PRIO-LIST
	      The priority to be used for traffic the priority of which is otherwise unspecified. The argument is a list of individual priorities.  Note  that
	      default-prio rules are configured as triplets (EtherType, 0, PRIO).  dcb app translates these rules to the symbolic name default-prio and back.

       ethtype-prio ET-MAP
	      ET-MAP  uses the array parameter syntax, see dcb(8) for details. Keys are EtherType values. Values are priorities to be assigned to traffic with
	      the matching EtherType.

       stream-port-prio PORT-MAP
       dgram-port-prio PORT-MAP
       port-prio PORT-MAP
	      PORT-MAP uses the array parameter syntax, see dcb(8) for details. Keys are L4 destination port numbers that match on, respectively, TCP and SCTP
	      traffic, UDP and DCCP traffic, and either of those. Values are priorities that should be assigned to matching traffic.

       dscp-prio DSCP-MAP
	      DSCP-MAP uses the array parameter syntax, see dcb(8) for details. Keys are DSCP points, values are priorities assigned to traffic with  matching
	      DSCP.  DSCP points can be written either directly as numeric values, or using symbolic names specified in /etc/iproute2/rt_dsfield (however note
	      that that file specifies full 8-bit dsfield values, whereas dcb app will only use the higher six bits).  dcb app show will similarly format DSCP
	      values as symbolic names if possible. The command line option -N turns the show translation off.

EXAMPLE & USAGE
       Prioritize traffic with DSCP 0 to priority 0, 24 to 3 and 48 to 6:

       # dcb app add dev eth0 dscp-prio 0:0 24:3 48:6

       Add another rule to configure DSCP 24 to priority 2 and show the result:

       # dcb app add dev eth0 dscp-prio 24:2
       # dcb app show dev eth0 dscp-prio
       dscp-prio 0:0 CS3:2 CS3:3 CS6:6
       # dcb -N app show dev eth0 dscp-prio
       dscp-prio 0:0 24:2 24:3 48:6

       Reconfigure the table so that the only rule for DSCP 24 is for assignment of priority 4:

       # dcb app replace dev eth0 dscp-prio 24:4
       # dcb app show dev eth0 dscp-prio
       dscp-prio 0:0 24:4 48:6

       Flush all DSCP rules:

       # dcb app flush dev eth0 dscp-prio
       # dcb app show dev eth0 dscp-prio
       (nothing)

EXIT STATUS
       Exit status is 0 if command was successful or a positive integer upon failure.

SEE ALSO
       dcb(8)

REPORTING BUGS
       Report any bugs to the Network Developers mailing list <netdev@vger.kernel.org> where the development and maintenance is primarily done.	  You  do  not
       have to be subscribed to the list to send a message there.

AUTHOR
       Petr Machata <me@pmachata.org>

iproute2								6 December 2020								    DCB-ETS(8)
