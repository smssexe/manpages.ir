SYSTEMD-NETWORK-GENERATOR.SERVICE(8)			       systemd-network-generator.service			  SYSTEMD-NETWORK-GENERATOR.SERVICE(8)

NAME
       systemd-network-generator.service, systemd-network-generator - Generate network configuration from the kernel command line

SYNOPSIS
       systemd-network-generator.service

       /usr/lib/systemd/systemd-network-generator

DESCRIPTION
       systemd-network-generator.service is a system service that translates ip= and related settings on the kernel command line (see below) into
       systemd.network(5), systemd.netdev(5), and systemd.link(5) configuration files understood by systemd-networkd.service(8) and systemd-udevd.service(8).

       Files are generated in /run/systemd/network/.

       Note: despite the name, this generator executes as a normal systemd service and is not an implementation of the systemd.generator(7) concept.

KERNEL COMMAND LINE OPTIONS
       This tool understands the following options:

       ip=, nameserver=, rd.route=, rd.peerdns=
	   Translated into systemd.network(5) files.

	   In addition to the parameters dracut.cmdline(7) defines the ip= option accepts the special value "link-local". If selected, the network interfaces
	   will be configured for link-local addressing (IPv4LL, IPv6LL) only, DHCP or IPv6RA will not be enabled.

	   Added in version 245.

       ifname=, net.ifname-policy=
	   Translated into systemd.link(5) files.

	   Added in version 245.

       vlan=, bond=, bridge=, bootdev=
	   Translated into systemd.netdev(5) files.

	   Added in version 245.

       See dracut.cmdline(7) and systemd-udevd.service(8) for option syntax and details.

SEE ALSO
       systemd(1), systemd-networkd.service(8), dracut(8)

systemd 255														  SYSTEMD-NETWORK-GENERATOR.SERVICE(8)
