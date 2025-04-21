proc_bus(5)							      File Formats Manual							   proc_bus(5)

NAME
       /proc/bus/ - installed buses

DESCRIPTION
       /proc/bus/
	      Contains subdirectories for installed buses.

       /proc/bus/pccard/
	      Subdirectory for PCMCIA devices when CONFIG_PCMCIA is set at kernel compilation time.

       /proc/bus/pccard/drivers

       /proc/bus/pci/
	      Contains	various	 bus  subdirectories  and pseudo-files containing information about PCI buses, installed devices, and device drivers.  Some of
	      these files are not ASCII.

       /proc/bus/pci/devices
	      Information about PCI devices.  They may be accessed through lspci(8) and setpci(8).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								   proc_bus(5)
