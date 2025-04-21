NETWORKCTL(1)								  networkctl								 NETWORKCTL(1)

NAME
       networkctl - Query or modify the status of network links

SYNOPSIS

       networkctl [OPTIONS...] COMMAND [LINK...]

DESCRIPTION
       networkctl may be used to query or modify the state of the network links as seen by systemd-networkd. Please refer to systemd-networkd.service(8) for
       an introduction to the basic concepts, functionality, and configuration syntax.

COMMANDS
       The following commands are understood:

       list [PATTERN...]
	   Show a list of existing links and their status. If one or more PATTERNs are specified, only links matching one of them are shown. If no further
	   arguments are specified shows all links, otherwise just the specified links. Produces output similar to:

	       IDX LINK		TYPE	 OPERATIONAL SETUP
		 1 lo		loopback carrier     unmanaged
		 2 eth0		ether	 routable    configured
		 3 virbr0	ether	 no-carrier  unmanaged
		 4 virbr0-nic	ether	 off	     unmanaged

	       4 links listed.

	   The operational status is one of the following:

	   missing
	       The device is missing.

	       Added in version 245.

	   off
	       The device is powered down.

	       Added in version 240.

	   no-carrier
	       The device is powered up, but does not yet have a carrier.

	       Added in version 240.

	   dormant
	       The device has a carrier, but is not yet ready for normal traffic.

	       Added in version 240.

	   degraded-carrier
	       One of the bonding or bridge slave network interfaces is in off, no-carrier, or dormant state, and the master interface has no address.

	       Added in version 242.

	   carrier
	       The link has carrier, or for bond or bridge master, all bonding or bridge slave network interfaces are enslaved to the master.

	       Added in version 240.

	   degraded
	       The link has carrier and addresses valid on the local link configured. For bond or bridge master this means that not all slave network
	       interfaces have carrier but at least one does.

	       Added in version 240.

	   enslaved
	       The link has carrier and is enslaved to bond or bridge master network interface.

	       Added in version 242.

	   routable
	       The link has carrier and routable address configured. For bond or bridge master it is not necessary for all slave network interfaces to have
	       carrier, but at least one must.

	       Added in version 240.

	   The setup status is one of the following:

	   pending
	       systemd-udevd(8) is still processing the link, we don't yet know if we will manage it.

	       Added in version 240.

	   initialized
	       systemd-udevd(8) has processed the link, but we don't yet know if we will manage it.

	       Added in version 251.

	   configuring
	       Configuration for the link is being retrieved or the link is being configured.

	       Added in version 240.

	   configured
	       Link has been configured successfully.

	       Added in version 240.

	   unmanaged
	       systemd-networkd is not handling the link.

	       Added in version 240.

	   failed
	       systemd-networkd failed to configure the link.

	       Added in version 240.

	   linger
	       The link is gone, but has not yet been dropped by systemd-networkd.

	       Added in version 240.

	   Added in version 219.

       status [PATTERN...]
	   Show information about the specified links: type, state, kernel module driver, hardware and IP address, configured DNS servers, etc. If one or more
	   PATTERNs are specified, only links matching one of them are shown.

	   When no links are specified, an overall network status is shown. Also see the option --all.

	   Produces output similar to:

	       ●	State: routable
		 Online state: online
		      Address: 10.193.76.5 on eth0
			       192.168.122.1 on virbr0
			       169.254.190.105 on eth0
			       fe80::5054:aa:bbbb:cccc on eth0
		      Gateway: 10.193.11.1 (CISCO SYSTEMS, INC.) on eth0
			  DNS: 8.8.8.8
			       8.8.4.4

	   In the overall network status, the online state depends on the individual online state of all required links. Managed links are required for online
	   by default. In this case, the online state is one of the following:

	   unknown
	       All links have unknown online status (i.e. there are no required links).

	       Added in version 249.

	   offline
	       All required links are offline.

	       Added in version 249.

	   partial
	       Some, but not all, required links are online.

	       Added in version 249.

	   online
	       All required links are online.

	       Added in version 249.

	   Added in version 219.

       lldp [PATTERN...]
	   Show discovered LLDP (Link Layer Discovery Protocol) neighbors. If one or more PATTERNs are specified only neighbors on those interfaces are shown.
	   Otherwise shows discovered neighbors on all interfaces. Note that for this feature to work, LLDP= must be turned on for the specific interface, see
	   systemd.network(5) for details.

	   Produces output similar to:

	       LINK		CHASSIS ID	  SYSTEM NAME	   CAPS	       PORT ID		 PORT DESCRIPTION
	       enp0s25		00:e0:4c:00:00:00 GS1900	   ..b........ 2		 Port #2

	       Capability Flags:
	       o - Other; p - Repeater;	 b - Bridge; w - WLAN Access Point; r - Router;
	       t - Telephone; d - DOCSIS cable device; a - Station; c - Customer VLAN;
	       s - Service VLAN, m - Two-port MAC Relay (TPMR)

	       1 neighbors listed.

	   Added in version 219.

       label
	   Show numerical address labels that can be used for address selection. This is the same information that ip-addrlabel(8) shows. See RFC 3484[1] for
	   a discussion of address labels.

	   Produces output similar to:

	       Prefix/Prefixlen				 Label
		       ::/0				     1
		   fc00::/7				     5
		   fec0::/10				    11
		   2002::/16				     2
		   3ffe::/16				    12
		2001:10::/28				     7
		   2001::/32				     6
	       ::ffff:0.0.0.0/96			     4
		       ::/96				     3
		      ::1/128				     0

	   Added in version 234.

       delete DEVICE...
	   Deletes virtual netdevs. Takes interface name or index number.

	   Added in version 243.

       up DEVICE...
	   Bring devices up. Takes interface name or index number.

	   Added in version 246.

       down DEVICE...
	   Bring devices down. Takes interface name or index number.

	   Added in version 246.

       renew DEVICE...
	   Renew dynamic configurations e.g. addresses received from DHCP server. Takes interface name or index number.

	   Added in version 244.

       forcerenew DEVICE...
	   Send a FORCERENEW message to all connected clients, triggering DHCP reconfiguration. Takes interface name or index number.

	   Added in version 246.

       reconfigure DEVICE...
	   Reconfigure network interfaces. Takes interface name or index number. Note that this does not reload .netdev or .network corresponding to the
	   specified interface. So, if you edit config files, it is necessary to call networkctl reload first to apply new settings.

	   Added in version 244.

       reload
	   Reload .netdev and .network files. If a new .netdev file is found, then the corresponding netdev is created. Note that even if an existing .netdev
	   is modified or removed, systemd-networkd does not update or remove the netdev. If a new, modified or removed .network file is found, then all
	   interfaces which match the file are reconfigured.

	   Added in version 244.

       edit FILE|@DEVICE...
	   Edit network configuration files, which include .network, .netdev, and .link files. If no network config file matching the given name is found, a
	   new one will be created under /etc/. Specially, if the name is prefixed by "@", it will be treated as a network interface, and editing will be
	   performed on the network config files associated with it. Additionally, the interface name can be suffixed with ":network" (default) or ":link", in
	   order to choose the type of network config to operate on.

	   If --drop-in= is specified, edit the drop-in file instead of the main configuration file. Unless --no-reload is specified, systemd-networkd will be
	   reloaded after the edit of the .network or .netdev files finishes. The same applies for .link files and systemd-udevd(8). Note that the changed
	   link settings are not automatically applied after reloading. To achieve that, trigger uevents for the corresponding interface. Refer to
	   systemd.link(5) for more information.

	   Added in version 254.

       cat FILE|@DEVICE...
	   Show network configuration files. This command honors the "@" prefix in the same way as edit.

	   Added in version 254.

OPTIONS
       The following options are understood:

       -a --all
	   Show all links with status.

	   Added in version 219.

       -s --stats
	   Show link statistics with status.

	   Added in version 243.

       -l, --full
	   Do not ellipsize the output.

	   Added in version 245.

       -n, --lines=
	   When used with status, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument.
	   Defaults to 10.

	   Added in version 245.

       --drop-in=NAME
	   When used with edit, edit the drop-in file NAME instead of the main configuration file.

	   Added in version 254.

       --no-reload
	   When used with edit, systemd-networkd.service(8) or systemd-udevd.service(8) will not be reloaded after the editing finishes.

	   Added in version 254.

       --json=MODE
	   Shows output formatted as JSON. Expects one of "short" (for the shortest possible output without any redundant whitespace or line breaks), "pretty"
	   (for a pretty version of the same, with indentation and line breaks) or "off" (to turn off JSON output, the default).

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

       --no-legend
	   Do not print the legend, i.e. column headers and the footer with hints.

       --no-pager
	   Do not pipe output into a pager.

EXIT STATUS
       On success, 0 is returned, a non-zero failure code otherwise.

SEE ALSO
       systemd-networkd.service(8), systemd.network(5), systemd.netdev(5), ip(8)

NOTES
	1. RFC 3484
	   https://tools.ietf.org/html/rfc3484

systemd 255																	 NETWORKCTL(1)
