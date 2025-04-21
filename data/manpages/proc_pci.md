proc_pci(5)							      File Formats Manual							   proc_pci(5)

NAME
       /proc/pci - PCI devices

DESCRIPTION
       /proc/pci
	      This is a listing of all PCI devices found during kernel initialization and their configuration.

	      This  file  has been deprecated in favor of a new /proc interface for PCI (/proc/bus/pci).  It became optional in Linux 2.2 (available with CON‐
	      FIG_PCI_OLD_PROC set at kernel compilation).  It became once more nonoptionally enabled in Linux 2.4.  Next, it  was  deprecated	in  Linux  2.6
	      (still available with CONFIG_PCI_LEGACY_PROC set), and finally removed altogether since Linux 2.6.17.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								   proc_pci(5)
