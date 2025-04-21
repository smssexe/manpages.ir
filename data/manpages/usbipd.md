USBIP(8)							System Administration Utilities							      USBIP(8)

NAME
       usbipd - USB/IP server daemon

SYNOPSIS
       usbipd [options]

DESCRIPTION
       usbipd provides USB/IP clients access to exported USB devices.

       Devices have to explicitly be exported using usbip bind before usbipd makes them available to other hosts.

       The daemon accepts connections from USB/IP clients on TCP port 3240 by default.

OPTIONS

       -4, --ipv4

	      Bind to IPv4. Default is both.

       -6, --ipv6

	      Bind to IPv6. Default is both.

       -e, --device

	      Run in device mode. Rather than drive an attached device, create a virtual UDC to bind gadgets to.

       -D, --daemon

	      Run as a daemon process.

       -d, --debug

	      Print debugging information.

       -PFILE, --pid FILE

	      Write process id to FILE.
	      If no FILE specified, use /var/run/usbipd.pid

       -tPORT, --tcp-port PORT

	      Listen on TCP/IP port PORT.

       -h, --help

	      Print the program help message and exit.

       -v, --version

	      Show version.

LIMITATIONS
       usbipd offers no authentication or authorization for USB/IP. Any USB/IP client can connect and use exported devices.

EXAMPLES
	   server:# modprobe usbip-host

	   server:# usbipd -D
	       - Start usbip daemon.

	   server:# usbip list --local
	       - List driver assignments for usb devices.

	   server:# usbip bind --busid=1-2
	       - Bind usbip-host.ko to the device of busid 1-2.
	       - A usb device 1-2 is now exportable to other hosts!
	       - Use 'usbip unbind --busid=1-2' when you want to shutdown exporting and use the device locally.

       The following example shows the usage of device mode

	   server:# modprobe usbip-vudc
	       - Use /sys/class/udc/ interface.
	       - usbip-host is independent of this module.

	   server:# usbipd -e -D
	       - Start usbip daemon in device mode.

	   server:# modprobe g_mass_storage file=/tmp/tmp.img
	       - Bind a gadget to usbip-vudc.
	       - in this example, a mass storage gadget is bound.

	   server:# usbip list --device
	       - List gadgets exported by local usbipd server.

	   server:# modprobe -r g_mass_storage
	       - Unbind a gadget from usbip-vudc.
	       - in this example, the previous mass storage gadget is unbound.

SEE ALSO
       usbip(8)

usbip									 February 2009								      USBIP(8)
