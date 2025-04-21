NETCONFIG(5)							      File Formats Manual							  NETCONFIG(5)

NAME
       netconfig — network configuration data base

SYNOPSIS
       /etc/netconfig

DESCRIPTION
       The netconfig file defines a list of “transport names”, describing their semantics and protocol.	 In FreeBSD, this file is only used by the RPC library
       code.

       Entries have the following format:

       network_id semantics flags family protoname device libraries

       Entries consist of the following fields:

       network_id  The name of the transport described.

       semantics   Describes the semantics of the transport.  This can be one of:

			 tpi_clts      Connectionless transport.

			 tpi_cots      Connection-oriented transport

			 tpi_cots_ord  Connection-oriented, ordered transport.

			 tpi_raw       A raw connection.

       flags	   This field is either blank (specified by “-”), or contains a “v”, meaning visible to the getnetconfig(3) function.

       family	   The protocol family of the transport.  This is currently one of:

			 inet6	   The IPv6 (PF_INET6) family of protocols.

			 inet	   The IPv4 (PF_INET) family of protocols.

			 loopback  The PF_LOCAL protocol family.

       protoname   The name of the protocol used for this transport.  Can currently be either udp, tcp or empty.

       device	   This field is always empty in FreeBSD.

       libraries   This field is always empty in FreeBSD.

       The  order of entries in this file will determine which transport will be preferred by the RPC library code, given a match on a specified network type.
       For example, if a sample network config file would look like this:

	     udp6	tpi_clts      v	    inet6    udp     -	     -
	     tcp6	tpi_cots_ord  v	    inet6    tcp     -	     -
	     udp	tpi_clts      v	    inet     udp     -	     -
	     tcp	tpi_cots_ord  v	    inet     tcp     -	     -
	     rawip	tpi_raw	      -	    inet      -	     -	     -
	     local	tpi_cots_ord  -	    loopback  -	     -	     -

       then using the network type udp in calls to the RPC library function (see rpc(3)) will make the code first try udp6, and then udp.

       getnetconfig(3) and associated functions will parse this file and return structures of the following format:

       struct netconfig {
	   char *nc_netid;		/* Network ID */
	   unsigned long nc_semantics;	/* Semantics (see below) */
	   unsigned long nc_flag;	/* Flags (see below) */
	   char *nc_protofmly;		/* Protocol family */
	   char *nc_proto;		/* Protocol name */
	   char *nc_device;		/* Network device pathname (unused) */
	   unsigned long nc_nlookups;	/* Number of lookup libs (unused) */
	   char **nc_lookups;		/* Names of the libraries (unused) */
	   unsigned long nc_unused[9];	/* reserved */
       };

FILES
       /etc/netconfig

SEE ALSO
       getnetconfig(3), getnetpath(3)

Debian								       November 17, 2000							  NETCONFIG(5)
