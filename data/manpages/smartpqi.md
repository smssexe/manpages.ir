smartpqi(4)							   Kernel Interfaces Manual							   smartpqi(4)

NAME
       smartpqi - Microchip Smart Storage SCSI driver

SYNOPSIS
       modprobe smartpqi [disable_device_id_wildcards={0|1}] [disable_heartbeat={0|1}] [disable_ctrl_shutdown={0|1}] [lockup_action={none|reboot|panic}]
			 [expose_ld_first={0|1}] [hide_vsep={0|1}] [disable_managed_interrupts={0|1}] [ctrl_ready_timeout={0|[30,1800]}]

DESCRIPTION
       smartpqi is a SCSI driver for Microchip Smart Storage controllers.

   Supported ioctl() operations
       For  compatibility  with	 applications written for the cciss(4) and hpsa(4) drivers, many, but not all of the ioctl(2) operations supported by the hpsa
       driver are also supported by the smartpqi driver.  The data structures used by these operations are described in	 the  Linux  kernel  source  file  in‐
       clude/linux/cciss_ioctl.h.

       CCISS_DEREGDISK
       CCISS_REGNEWDISK
       CCISS_REGNEWD
	      These  operations	 all  do exactly the same thing, which is to cause the driver to re-scan for new devices.  This does exactly the same thing as
	      writing to the smartpqi-specific host rescan attribute.

       CCISS_GETPCIINFO
	      This operation returns the PCI domain, bus, device, and function and "board ID" (PCI subsystem ID).

       CCISS_GETDRIVVER
	      This operation returns the driver version in four bytes, encoded as:

		  (major_version << 28) | (minor_version << 24) |
			  (release << 16) | revision

       CCISS_PASSTHRU
	      Allows BMIC and CISS commands to be passed through to the controller.

   Boot options
       disable_device_id_wildcards={0|1}
	      Disables support for device ID wildcards.	 The default value is 0 (wildcards are enabled).

       disable_heartbeat={0|1}
	      Disables support for the controller's heartbeat check.  This parameter is used for debugging purposes.  The default value is 0 (the controller's
	      heartbeat check is enabled).

       disable_ctrl_shutdown={0|1}
	      Disables support for shutting down the controller in the event of a controller lockup.  The default value is 0 (controller will be shut down).

       lockup_action={none|reboot|panic}
	      Specifies the action the driver takes when a controller lockup is detected.  The default action is none.
	      parameter	  action
	      ─────────────────────────────────────────────
	      none	  take controller offline only
	      reboot	  reboot the system
	      panic	  panic the system

       expose_ld_first={0|1}
	      This option exposes logical devices to the OS before physical devices.  The default value is 0 (physical devices exposed first).

       hide_vsep={0|1}
	      This option disables exposure of the virtual SEP to the OS.  The default value is 0 (virtual SEP is exposed).

       disable_managed_interrupts={0|1}
	      Disables driver utilization of Linux kernel managed interrupts for controllers.  The managed interrupts feature automatically distributes inter‐
	      rupts to all available CPUs and assigns SMP affinity.  The default value is 0 (managed interrupts enabled).

       ctrl_ready_timeout={0|[30,1800]}
	      This option specifies the timeout in seconds for the driver to wait for the controller to be ready.  The valid range is 0 or  [30,  1800].   The
	      default value is 0, which causes the driver to use a timeout of 180 seconds.

FILES
   Device nodes
       Disk  drives are accessed via the SCSI disk driver (sd), tape drives via the SCSI tape driver (st), and the RAID controller via the SCSI generic driver
       (sg), with device nodes named /dev/sd*, /dev/st*, and /dev/sg*, respectively.

   SmartPQI-specific host attribute files in /sys
       /sys/class/scsi_host/host*/rescan
	      The host rescan attribute is a write-only attribute.  Writing to this attribute will cause the driver to scan for new, changed, or  removed  de‐
	      vices  (e.g.,  hot-plugged  tape	drives, or newly configured or deleted logical volumes) and notify the SCSI mid-layer of any changes detected.
	      Usually this action is triggered automatically by configuration changes, so the user should not normally have to write to this file.   Doing  so
	      may be useful when hot-plugging devices such as tape drives or entire storage boxes containing pre-configured logical volumes.

       /sys/class/scsi_host/host*/lockup_action
	      The  host	 lockup_action attribute is a read/write attribute.  This attribute will cause the driver to perform a specific action in the unlikely
	      event that a controller lockup has been detected.	 See OPTIONS above for an explanation of the lockup_action values.

       /sys/class/scsi_host/host*/driver_version
	      The driver_version attribute is read-only.  This attribute contains the smartpqi driver version.

	      For example:

		  $ cat /sys/class/scsi_host/host1/driver_version
		  1.1.2-126

       /sys/class/scsi_host/host*/firmware_version
	      The firmware_version attribute is read-only.  This attribute contains the controller firmware version.

	      For example:

		  $ cat /sys/class/scsi_host/host1/firmware_version
		  1.29-112

       /sys/class/scsi_host/host*/model
	      The model attribute is read-only.	 This attribute contains the product identification string of the controller.

	      For example:

		  $ cat /sys/class/scsi_host/host1/model
		  1100-16i

       /sys/class/scsi_host/host*/serial_number
	      The serial_number attribute is read-only.	 This attribute contains the unique identification number of the controller.

	      For example:

		  $ cat /sys/class/scsi_host/host1/serial_number
		  6A316373777

       /sys/class/scsi_host/host*/vendor
	      The vendor attribute is read-only.  This attribute contains the vendor identification string of the controller.

	      For example:

		  $ cat /sys/class/scsi_host/host1/vendor
		  Adaptec

       /sys/class/scsi_host/host*/enable_stream_detection
	      The enable_stream_detection attribute is read-write.  This attribute enables/disables stream detection in the driver.  Enabling stream detection
	      can improve sequential write performance for ioaccel-enabled volumes.  See the ssd_smart_path_enabled disk  attribute  section  for  details  on
	      ioaccel-enabled volumes.	The default value is 1 (stream detection enabled).

	      Enable example:

		  $ echo 1 > /sys/class/scsi_host/host1/enable_stream_detection

       /sys/class/scsi_host/host*/enable_r5_writes
	      The  enable_r5_writes  attribute	is read-write.	This attribute enables/disables RAID 5 write operations for ioaccel-enabled volumes.  Enabling
	      can improve sequential write performance.	 See the ssd_smart_path_enabled disk attribute section for details on  ioaccel-enabled	volumes.   The
	      default value is 1 (RAID 5 writes enabled).

	      Enable example:

		  $ echo 1 > /sys/class/scsi_host/host1/enable_r5_writes

       /sys/class/scsi_host/host*/enable_r6_writes
	      The  enable_r6_writes  attribute	is read-write.	This attribute enables/disables RAID 6 write operations for ioaccel-enabled volumes.  Enabling
	      can improve sequential write performance.	 See the ssd_smart_path_enabled disk attribute section for details on  ioaccel-enabled	volumes.   The
	      default value is 1 (RAID 6 writes enabled).

	      Enable example:

		  $ echo 1 > /sys/class/scsi_host/host1/enable_r6_writes

   SmartPQI-specific disk attribute files in /sys
       In  the	file  specifications below, c stands for the number of the appropriate SCSI controller, b is the bus number, t the target number, and l is the
       logical unit number (LUN).

       /sys/class/scsi_disk/c:b:t:l/device/raid_level
	      The raid_level attribute is read-only.  This attribute contains the RAID level of the logical volume.

	      For example:

		  $ cat /sys/class/scsi_disk/4:0:0:0/device/raid_level
		  RAID 0

       /sys/class/scsi_disk/c:b:t:l/device/sas_address
	      The sas_address attribute is read-only.  This attribute contains the SAS address of the device.

	      For example:

		  $ cat /sys/class/scsi_disk/1:0:3:0/device/sas_address
		  0x5001173d028543a2

       /sys/class/scsi_disk/c:b:t:l/device/ssd_smart_path_enabled
	      The ssd_smart_path_enabled attribute is read-only.  This attribute is for ioaccel-enabled volumes.  (Ioaccel is an alternative driver submission
	      path that allows the driver to send I/O requests directly to backend SCSI devices, bypassing the controller firmware.  This results  in  an  in‐
	      crease  in performance.  This method is used for HBA disks and for logical volumes comprised of SSDs.)  Contains 1 if ioaccel is enabled for the
	      volume and 0 otherwise.

	      For example:

		  $ cat /sys/class/scsi_disk/1:0:3:0/device/ssd_smart_path_enabled
		  0

       /sys/class/scsi_disk/c:b:t:l/device/lunid
	      The lunid attribute is read-only.	 This attribute contains the SCSI LUN ID for the device.

	      For example:

		  $ cat /sys/class/scsi_disk/13:1:0:3/device/lunid
		  0x0300004000000000

       /sys/class/scsi_disk/c:b:t:l/device/unique_id
	      The unique_id attribute is read-only.  This attribute contains a 16-byte ID that uniquely identifies the device within the controller.

	      For example:

		  $ cat /sys/class/scsi_disk/13:1:0:3/device/unique_id
		  600508B1001C6D4723A8E98D704FDB94

       /sys/class/scsi_disk/c:b:t:l/device/path_info
	      The path_info attribute is read-only.  This attribute contains the c:b:t:l of the device along with the device type and whether  the  device  is
	      Active or Inactive.  If the device is an HBA device, path_info will also display the PORT, BOX, and BAY the device is plugged into.

	      For example:

		  $ cat /sys/class/scsi_disk/13:1:0:3/device/path_info
		  [13:1:0:3]	Direct-Access	  Active

		  $ cat /sys/class/scsi_disk/12:0:9:0/device/path_info
		  [12:0:9:0]  Direct-Access   PORT: C1 BOX: 1 BAY: 14 Inactive
		  [12:0:9:0]  Direct-Access   PORT: C0 BOX: 1 BAY: 14 Active

       /sys/class/scsi_disk/c:b:t:l/device/raid_bypass_cnt
	      The  raid_bypass_cnt  attribute  is  read-only.	This attribute contains the number of I/O requests that have gone through the ioaccel path for
	      ioaccel-enabled volumes.	See the ssd_smart_path_enabled disk attribute section for details on ioaccel-enabled volumes.

	      For example:

		  $ cat /sys/class/scsi_disk/13:1:0:3/device/raid_bypass_cnt
		  0x300

       /sys/class/scsi_disk/c:b:t:l/device/sas_ncq_prio_enable
	      The sas_ncq_prio_enable attribute is read/write.	This attribute enables SATA NCQ priority support.  This attribute works only when  device  has
	      NCQ support and controller firmware can handle IO with NCQ priority attribute.

	      For example:

		  $ echo 1 > /sys/class/scsi_disk/13:1:0:3/device/sas_ncq_prio_enable

VERSIONS
       The smartpqi driver was added in Linux 4.9.

NOTES
   Configuration
       To  configure  a	 Microchip Smart Storage controller, refer to the User Guide for the controller, which can be found by searching for the specific con‐
       troller at https://www.microchip.com/design-centers/storage.

HISTORY
       /sys/class/scsi_host/host*/version was replaced by two sysfs entries:

	      /sys/class/scsi_host/host*/driver_version

	      /sys/class/scsi_host/host*/firmware_version

SEE ALSO
       cciss(4), hpsa(4), sd(4), st(4), sg(4)

       Documentation/ABI/testing/sysfs-bus-pci-devices-cciss in the Linux kernel source tree.

Linux man-pages 6.7							  2023-10-31								   smartpqi(4)
