proc_scsi(5)							      File Formats Manual							  proc_scsi(5)

NAME
       /proc/scsi/ - SCSI

DESCRIPTION
       /proc/scsi/
	      A	 directory  with the scsi mid-level pseudo-file and various SCSI low-level driver directories, which contain a file for each SCSI host in this
	      system, all of which give the status of some part of the SCSI IO subsystem.  These files contain ASCII structures and are,  therefore,  readable
	      with cat(1).

	      You can also write to some of the files to reconfigure the subsystem or switch certain features on or off.

       /proc/scsi/scsi
	      This  is a listing of all SCSI devices known to the kernel.  The listing is similar to the one seen during bootup.  scsi currently supports only
	      the add-single-device command which allows root to add a hotplugged device to the list of known devices.

	      The command

		  echo 'scsi add-single-device 1 0 5 0' > /proc/scsi/scsi

	      will cause host scsi1 to scan on SCSI channel 0 for a device on ID 5 LUN 0.  If there is already a device known on this address or  the  address
	      is invalid, an error will be returned.

       /proc/scsi/drivername/
	      drivername  can  currently  be  NCR53c7xx,  aha152x,  aha1542,  aha1740,	aic7xxx, buslogic, eata_dma, eata_pio, fdomain, in2000, pas16, qlogic,
	      scsi_debug, seagate, t128, u15-24f, ultrastore, or wd7000.  These directories show up for all drivers that registered at	least  one  SCSI  HBA.
	      Every directory contains one file per registered host.  Every host-file is named after the number the host was assigned during initialization.

	      Reading these files will usually show driver and host configuration, statistics, and so on.

	      Writing to these files allows different things on different hosts.  For example, with the latency and nolatency commands, root can switch on and
	      off command latency measurement code in the eata_dma driver.  With the lockup and unlock commands, root can control bus lockups simulated by the
	      scsi_debug driver.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								  proc_scsi(5)
