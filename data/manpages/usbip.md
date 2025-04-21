USBIP(8)							System Administration Utilities							      USBIP(8)

NAME
       usbip - manage USB/IP devices

SYNOPSIS
       usbip [options] <command> <args>

DESCRIPTION
       On  a  USB/IP  server,  devices	can  be	 listed, bound, and unbound using this program.	 On a USB/IP client, devices exported by USB/IP servers can be
       listed, attached and detached.

OPTIONS

       --debug

	      Print debugging information.

       --log

	      Log to syslog.

       --tcp-port PORT

	      Connect to PORT on remote host (used for attach and list --remote).

COMMANDS

       version

	      Show version and exit.

       help [command]

	      Print the program help message, or help on a specific command, and then exit.

       attach --remote=<host> --busid=<bus_id>

	      Attach a remote USB device.

       attach --remote=<host> --device=<dev_id>

	      Attach a remote USB gadget.  Only used when the remote usbipd is in device mode.

       detach --port=<port>

	      Detach an imported USB device/gadget.

       bind --busid=<busid>

	      Make a device exportable.

       unbind --busid=<busid>

	      Stop exporting a device so it can be used by a local driver.

       list --remote=<host>

	      List USB devices exported by a remote host.

       list --device

	      List USB gadgets of local usbip-vudc.  Only used when the local usbipd is in device mode.	 Note that this can not list usbip-vudc USB gadgets of
	      the remote device mode usbipd.

       list --local

	      List local USB devices.

       port

	      List imported devices/gadgets.

EXAMPLES
	   client:# usbip list --remote=server
	       - List devices exported by remote server.

	   client:# modprobe vhci-hcd

	   client:# usbip attach --remote=server --busid=1-2
	       - Connect the remote USB device.

	   client:# usbip port
	       - List imported devices/gadgets.

	   client:# usbip detach --port=0
	       - Detach the usb device.

       The following example shows the usage of device mode

	   server:# usbip list --device
	       - List gadgets exported by local usbipd server.

	   client:# modprobe vhci-hcd

	   client:# usbip attach --remote=server --device=usbip-vudc.0
	       - Connect the remote USB gadget.

	   client:# usbip port
	       - List imported devices/gadgets.

	   client:# usbip detach --port=0
	       - Detach the usb gadget.

SEE ALSO
       usbipd(8)

usbip									 February 2009								      USBIP(8)
