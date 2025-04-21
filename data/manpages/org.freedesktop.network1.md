ORG.FREEDESKTOP.NETWORK1(5)					   org.freedesktop.network1					   ORG.FREEDESKTOP.NETWORK1(5)

NAME
       org.freedesktop.network1 - The D-Bus interface of systemd-networkd

INTRODUCTION
       systemd-networkd.service(8) is a system service that manages and configures network interfaces. This page describes the D-Bus interface.

THE MANAGER OBJECT
       The service exposes the following interfaces on the Manager object on the bus:

	   node /org/freedesktop/network1 {
	     interface org.freedesktop.network1.Manager {
	       methods:
		 ListLinks(out a(iso) links);
		 GetLinkByName(in  s name,
			       out i ifindex,
			       out o path);
		 GetLinkByIndex(in  i ifindex,
				out s name,
				out o path);
		 SetLinkNTP(in	i ifindex,
			    in	as servers);
		 SetLinkDNS(in	i ifindex,
			    in	a(iay) addresses);
		 SetLinkDNSEx(in  i ifindex,
			      in  a(iayqs) addresses);
		 SetLinkDomains(in  i ifindex,
				in  a(sb) domains);
		 SetLinkDefaultRoute(in	 i ifindex,
				     in	 b enable);
		 SetLinkLLMNR(in  i ifindex,
			      in  s mode);
		 SetLinkMulticastDNS(in	 i ifindex,
				     in	 s mode);
		 SetLinkDNSOverTLS(in  i ifindex,
				   in  s mode);
		 SetLinkDNSSEC(in  i ifindex,
			       in  s mode);
		 SetLinkDNSSECNegativeTrustAnchors(in  i ifindex,
						   in  as names);
		 RevertLinkNTP(in  i ifindex);
		 RevertLinkDNS(in  i ifindex);
		 RenewLink(in  i ifindex);
		 ForceRenewLink(in  i ifindex);
		 ReconfigureLink(in  i ifindex);
		 Reload();
		 DescribeLink(in  i ifindex,
			      out s json);
		 Describe(out s json);
	       properties:
		 readonly s OperationalState = '...';
		 readonly s CarrierState = '...';
		 readonly s AddressState = '...';
		 readonly s IPv4AddressState = '...';
		 readonly s IPv6AddressState = '...';
		 readonly s OnlineState = '...';
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly t NamespaceId = ...;
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	   };

       Provides information about the manager.

LINK OBJECT
	   node /org/freedesktop/network1/link/_1 {
	     interface org.freedesktop.network1.Link {
	       methods:
		 SetNTP(in  as servers);
		 SetDNS(in  a(iay) addresses);
		 SetDNSEx(in  a(iayqs) addresses);
		 SetDomains(in	a(sb) domains);
		 SetDefaultRoute(in  b enable);
		 SetLLMNR(in  s mode);
		 SetMulticastDNS(in  s mode);
		 SetDNSOverTLS(in  s mode);
		 SetDNSSEC(in  s mode);
		 SetDNSSECNegativeTrustAnchors(in  as names);
		 RevertNTP();
		 RevertDNS();
		 Renew();
		 ForceRenew();
		 Reconfigure();
		 Describe(out s json);
	       properties:
		 readonly s OperationalState = '...';
		 readonly s CarrierState = '...';
		 readonly s AddressState = '...';
		 readonly s IPv4AddressState = '...';
		 readonly s IPv6AddressState = '...';
		 readonly s OnlineState = '...';
		 readonly s AdministrativeState = '...';
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("false")
		 readonly (tt) BitRates = ...;
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	   };

       Provides information about interfaces.

NETWORK OBJECT
	   node /org/freedesktop/network1/network/_1 {
	     interface org.freedesktop.network1.Network {
	       properties:
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly s Description = '...';
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly s SourcePath = '...';
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly as MatchMAC = ['...', ...];
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly as MatchPath = ['...', ...];
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly as MatchDriver = ['...', ...];
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly as MatchType = ['...', ...];
		 @org.freedesktop.DBus.Property.EmitsChangedSignal("const")
		 readonly as MatchName = ['...', ...];
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	   };

       Provides information about .network files.

DHCP SERVER OBJECT
	   node /org/freedesktop/network1/link/_1 {
	     interface org.freedesktop.network1.DHCPServer {
	       properties:
		 readonly a(uayayayayt) Leases = [...];
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	     interface org.freedesktop.network1.Link { ... };
	   };

       Provides information about leases.

DHCPV4 CLIENT OBJECT
	   node /org/freedesktop/network1/link/_1 {
	     interface org.freedesktop.network1.DHCPv4Client {
	       properties:
		 readonly s State = '...';
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	     interface org.freedesktop.network1.Link { ... };
	   };

       Provides information about DHCPv4 client status.

DHCPV6 CLIENT OBJECT
	   node /org/freedesktop/network1/link/_1 {
	     interface org.freedesktop.network1.DHCPv6Client {
	       properties:
		 readonly s State = '...';
	     };
	     interface org.freedesktop.DBus.Peer { ... };
	     interface org.freedesktop.DBus.Introspectable { ... };
	     interface org.freedesktop.DBus.Properties { ... };
	     interface org.freedesktop.network1.Link { ... };
	   };

       Provides information about DHCPv6 client status.

EXAMPLES
       Example 1. Introspect org.freedesktop.network1.Manager on the bus

	   $ gdbus introspect --system \
	     --dest org.freedesktop.network1 \
	     --object-path /org/freedesktop/network1

       Example 2. Introspect org.freedesktop.network1.Link on the bus

	   $ gdbus introspect --system \
	     --dest org.freedesktop.network1 \
	     --object-path /org/freedesktop/network1/link/_11

VERSIONING
       These D-Bus interfaces follow the usual interface versioning guidelines[1].

HISTORY
   DHCPv4 Client Object
       State was added in version 255.

   DHCPv6 Client Object
       State was added in version 255.

NOTES
	1. the usual interface versioning guidelines
	   https://0pointer.de/blog/projects/versioning-dbus.html

systemd 255															   ORG.FREEDESKTOP.NETWORK1(5)
