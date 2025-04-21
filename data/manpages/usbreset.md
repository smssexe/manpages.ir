usbreset(1)							      Linux USB Utilities							   usbreset(1)

NAME
       usbreset - send a USB port reset to a USB device

SYNOPSIS
       usbreset [ device ]

DESCRIPTION
       usbreset	 is a utility that performs resets on USB devices. It is particularly useful situations where a USB device is unresponsive or exhibits erratic
       behavior.  The USB device to be reset can be specified in one of three formats:

       PPPP:VVVV
	      Reset by product and vendor IDs

       BBB/DDD
	      Reset by bus and device number

       Product
	      Reset by product name

       When run without any arguments, usbreset provides usage information and a list of connected USB devices, including their product and  vendor  IDs,  bus
       and device numbers, and product names.

RETURN VALUE
       If the specified device is not found, a non-zero exit code is returned.

EXAMPLES
       Reset device with vendor ID 1234 and product ID 5678:
	      usbreset 1234:5678

       Reset device 002 on bus 001:
	      usbreset 001:002

       Reset device named USB2.0 Hub:
	      usbreset "USB2.0 Hub"

SEE ALSO
       lsusb(8).

AUTHOR
       Alan Stern <stern@rowland.harvard.edu>

usbutils-017								04 January 2024								   usbreset(1)
