proc_ide(5)							      File Formats Manual							   proc_ide(5)

NAME
       /proc/ide/ - IDE channels and attached devices

DESCRIPTION
       /proc/ide
	      This directory exists on systems with the IDE bus.  There are directories for each IDE channel and attached device.  Files include:

		  cache		     buffer size in KB
		  capacity	     number of sectors
		  driver	     driver version
		  geometry	     physical and logical geometry
		  identify	     in hexadecimal
		  media		     media type
		  model		     manufacturer's model number
		  settings	     drive settings
		  smart_thresholds   IDE disk management thresholds (in hex)
		  smart_values	     IDE disk management values (in hex)

	      The hdparm(8) utility provides access to this information in a friendly format.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								   proc_ide(5)
