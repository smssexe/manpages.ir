SG_SAT_IDENTIFY(8)							   SG3_UTILS							    SG_SAT_IDENTIFY(8)

NAME
       sg_sat_identify - send ATA IDENTIFY DEVICE command via SCSI to ATA Translation (SAT) layer

SYNOPSIS
       sg_sat_identify [--ck_cond] [--extend] [--help] [--hex] [--ident] [--len=CLEN] [--packet] [--raw] [--readonly] [--verbose] [--version] DEVICE

DESCRIPTION
       This  utility sends either an ATA IDENTIFY DEVICE command or an ATA IDENTIFY PACKET DEVICE command to DEVICE and outputs the response. The devices that
       respond to these commands are ATA disks and ATAPI devices respectively.	Rather than send these commands directly to the device they  are  sent	via  a
       SCSI  transport	which  is  assumed to contain a SCSI to ATA Translation (SAT) Layer (SATL). The SATL may be in an operating system driver, in host bus
       adapter firmware or in some external enclosure.

       The SAT standard (SAT ANSI INCITS 431-2007, prior draft: sat-r09.pdf at www.t10.org) defines two SCSI "ATA PASS-THROUGH" commands: one using a 16  byte
       "cdb"  and  the	other with a 12 byte cdb. This utility defaults to using the 16 byte cdb variant. SAT-4 revision 5 added a SCSI "ATA PASS-THROUGH(32)"
       command. SAT-2 and SAT-3 are now also standards: SAT-2 ANSI INCITS 465-2010 and SAT-3 ANSI INCITS 517-2015 . The SAT-4 project is near  standardization
       and the most recent draft is sat4r06.pdf .

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -c, --ck_cond
	      sets the CK_COND bit in the ATA PASS-THROUGH SCSI cdb. The default setting is clear (i.e. 0). When set the SATL should yield a sense buffer con‐
	      taining  a  ATA  Result descriptor irrespective of whether the command succeeded or failed. When clear the SATL should only yield a sense buffer
	      containing a ATA Result descriptor if the command failed.

       -e, --extend
	      sets the EXTEND bit in the ATA PASS-THROUGH SCSI cdb. The default setting is clear (i.e. 0). When set a 48 bit LBA command is sent  to  the  de‐
	      vice. This option has no effect when --len=12.

       -h, --help
	      outputs the usage message summarizing command line options then exits. Ignores DEVICE if given.

       -H, --hex
	      outputs  the  ATA IDENTIFY (PACKET) DEVICE response in hex. The default action (i.e. without any '-H' options) is to output the response in hex,
	      grouped in 16 bit words (i.e. the ATA standard's preference).  When given once, the response is output in ASCII hex bytes (i.e. the  SCSI	 stan‐
	      dard's  preference).  When given twice (i.e. '-HH') the output is in hex, grouped in 16 bit words, the same as the default but without a header.
	      When given thrice (i.e. '-HHH') the output is in hex, grouped in 16 bit words, in a format that is acceptable for 'hdparm --Istdin' to  process.
	      '-HHHH' simply outputs hex data bytes, space separated, 16 per line.

       -i, --ident
	      outputs  the World Wide Name (WWN) of the device. This should be a NAA-5 64 bit number. It is output in hex prefixed with "0x". If not available
	      then "0x0000000000000000" is output. The equivalent for a SCSI disk (i.e. its logical unit name) can be found with "sg_vpd -ii".

       -l, --len=CLEN
	      CLEN this is the length of the SCSI cdb used for the ATA PASS-THROUGH command.  CLEN can either be 12, 16 or 32. The default is 16.  The	larger
	      cdb  sizes are needed for 48 bit LBA addressing of ATA devices. The ATA Auxiliary and ICC registers are only conveyed with the 32 byte cdb vari‐
	      ant.

       -p, --packet
	      send an ATA IDENTIFY PACKET DEVICE command (via the SATL). The default action is to send an ATA IDENTIFY DEVICE command.	Note  that  the	 ATAPI
	      specification by T13 (i.e. the PACKET interface) is now obsolete.

       -r, --raw
	      output  the  ATA	IDENTIFY (PACKET) DEVICE response in binary. The output should be piped to a file or another utility when this option is used.
	      The binary is sent to stdout, and errors are sent to stderr.

       -R, --readonly
	      open the DEVICE read-only (e.g. in Unix with the O_RDONLY flag).	The default is to open it read-write.

       -v, --verbose
	      increases the level or verbosity.

       -V, --version
	      print out version string

NOTES
       Since the response to the IDENTIFY (PACKET) DEVICE command is very important for the correct use of an ATA(PI) device (and is typically the first  com‐
       mand sent), a SATL should provide an ATA Information VPD page which contains the similar information.

       The  SCSI  ATA PASS-THROUGH (12) command's opcode is 0xa1 and it clashes with the MMC set's BLANK command used by cd/dvd writers. So a SATL in front of
       an ATAPI device that uses MMC (i.e. has peripheral device type 5) probably should treat opcode 0xa1 as a BLANK command  and  send  it  through  to  the
       cd/dvd drive. The ATA PASS-THROUGH (16) command's opcode (0x85) does not clash with anything so it is a better choice.

       Prior to Linux kernel 2.6.29 USB mass storage limited sense data to 18 bytes which made the --ck_cond option yield strange (truncated) results.

EXAMPLES
       These  examples	use  Linux  device  names  and	a  Linux utility called hdparm. For suitable device names in other supported Operating Systems see the
       sg3_utils(8) man page.

       In this example /dev/sdb is a SATA 2.5" disk connected via a USB (type C connector) dongle that implements the UAS (USB attached SCSI)  protocol	 (also
       known as UASP). UAS is a vast improvement over the USB mass storage class.

	   # sg_sat_identify /dev/sdb
       Response for IDENTIFY DEVICE ATA command:
	00   0c5a 3fff c837 0010 0000 0000 003f 0000  .Z ?. .7 .. .. .. .? ..
	....

       The hexadecimal ASCII (with plain ASCII to the right) output is abridged to a single line (i.e. the first 16 bytes (or 8 words)). Now to decode some of
       that ATA Identify response. First sg_inq can decode a few strings:

	   # sg_sat_identify -HHHH /dev/sdb | sg_inq --ata -I -
       ATA device: model, serial number and firmware revision:
	 ST9500420AS	 5VJCE6R7 0002SDM1

       For a lot more details, the hdparm utility is a good choice:

	   # sg_sat_identify -HHH /dev/sdb | hdparm --Istdin
       ATA device, with non-removable media
	       Model Number:	   ST9500420AS
	       Serial Number:	   5VJCE6R7
	       Firmware Revision:  0002SDM1
	       Transport:	   Serial
       Standards:
	....

       There  are  about 80 more lines of details decoded by hdparm in this case.  Notice the difference in the number of "H" options: three give an unadorned
       hex output arranged in (little endian) words (i.e. 16 bits each) while four "H" options give an unadorned hex output in bytes (i.e. 8 bits each).

EXIT STATUS
       The exit status of sg_sat_identify is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHOR
       Written by Douglas Gilbert

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2006-2020 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_vpd(sg3_utils), sg_inq(sg3_utils), sdparm(sdparm), hdparm(hdparm)

sg3_utils-1.45								 January 2020							    SG_SAT_IDENTIFY(8)
