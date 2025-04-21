SG_BG_CTL(8)								   SG3_UTILS								  SG_BG_CTL(8)

NAME
       sg_bg_ctl - send SCSI BACKGROUND CONTROL command

SYNOPSIS
       sg_bg_ctl [--ctl=CTL] [--help] [--time=TN] [--verbose] [--version] DEVICE

DESCRIPTION
       Sends  a	 SCSI  BACKGROUND  CONTROL command to the DEVICE. This command was first found in the SBC-4 draft standard revision 8 (sbc4r08.pdf). It can be
       used to start and stop 'advanced background operations' on the DEVICE. Only resource or thin provisioned devices (logical  units	 which	are  typically
       (solid  state) disks) support this command. Those advanced background operations often include garbage collection type operations which may degrade the
       disk's performance while they are being performed.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -c, --ctl=CTL
	      CTL is the value placed in the BO_CTL field of the BACKGROUND CONTROL command (cdb). It is a two bit field so has 4 variants: 0 does not	change
	      the  host	 initiated advanced background operations; 1 starts these operations; 2 stops these operations and 3 is reserved. The default value is
	      0.

       -h, --help
	      output the usage message then exit.

       -t, --time=TN
	      TN is a maximum time (with a unit of 100 ms or 1/10 second) that advanced background operations can occur. This value is ignored if the CTL  ar‐
	      gument  is  other than 1. The default value is 0 which means there is no maximum time limit. Only values 0 to 255 (which is 25.5 seconds) can be
	      given. This value is place in the BO_TIME field of the BACKGROUND CONTROL command.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

NOTES
       According to T10, support for 'background control operations' is indicated by the BOCS bit being set in	the  Block  device  characteristics  VPD  page
       [0xb1].	 The  setting of the BOCS bit can be checked with the sg_vpd and sdparm utilities (and it is read only). There is a Background operations con‐
       trol mode page [0xa, 0x6] with a BO_MODE field for modifying the action of this operation. The BO_MODE field can be accessed and possibly modified with
       the sdparm utility. The BO_STATUS field can be found in the Background operation log page [0x15, 0x2] and that can be viewed with the sg_logs utility.

       The current draft describing this area is SBC-4 revision 10 (sbc4r10.pdf) in clause 4.33 . That contains the following example of a  background	opera‐
       tion:  "Advanced background operation may include NAND block erase operations, media read operations, and media write operations (e.g., garbage collec‐
       tion), which may impact response time for normal read requests or write requests from the application client."

EXIT STATUS
       The exit status of sg_bg_ctl is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2016 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_vpd,sg_logs(sg3_utils); sdparm(sdparm)

sg3_utils-1.43								   May 2016								  SG_BG_CTL(8)
