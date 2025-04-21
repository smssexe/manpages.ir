SG_INQ(8)								   SG3_UTILS								     SG_INQ(8)

NAME
       sg_inq - issue SCSI INQUIRY command and/or decode its response

SYNOPSIS
       sg_inq  [--ata]	[--block=0|1]  [--cmddt]  [--descriptors] [--export] [--extended] [--force] [--help] [--hex] [--id] [--inhex=FN] [--len=LEN]  [--long]
       [--maxlen=LEN] [--only] [--page=PG] [--raw] [--vendor] [--verbose] [--version] [--vpd] DEVICE

       sg_inq [-36] [-a] [-A] [-b] [--B=0|1] [-c] [-cl] [-d] [-e] [-f] [-h] [-H] [-i] [-I=FN] [-l=LEN] [-L] [-m] [-M] [-o] [-p=VPD_PG]	[-P]  [-r]  [-s]  [-u]
       [-v] [-V] [-x] [-36] [-?] DEVICE

DESCRIPTION
       This utility, when DEVICE is given, sends a SCSI INQUIRY command to it then outputs the response. All SCSI devices are meant to respond to a "standard"
       INQUIRY command with at least a 36 byte response (in SCSI 2 and higher). An INQUIRY is termed as "standard" when both the EVPD and CmdDt (now obsolete)
       bits are clear.

       Alternatively  the --inhex=FN option can be given. In this case FN is assumed to be a file name ('-' for stdin) containing ASCII hexadecimal represent‐
       ing an INQUIRY response.

       This utility supports two command line syntaxes. The preferred one is shown first in the synopsis and is described in the main OPTIONS section. A later
       section titled OLDER COMMAND LINE OPTIONS describes the second group of options.

       An important "non-standard" INQUIRY page is the Device Identification Vital Product Data (VPD) page [0x83]. Since  SPC-3,  support  for	this  page  is
       mandatory.  The	--id  option decodes this page. New VPD page information is no longer being added to this utility. To get information on new VPD pages
       see the sg_vpd(8) or sdparm(8) utilities.

       In Linux, if the DEVICE exists and the SCSI INQUIRY fails (e.g. because the SG_IO ioctl is not supported) then  an  ATA	IDENTIFY  (PACKET)  DEVICE  is
       tried.  If  it  succeeds then device identification strings are output. The --raw and --hex options can be used to manipulate the output.  If the --ata
       option is given then the SCSI INQUIRY is not performed and the DEVICE is assumed to be ATA (or ATAPI). For more information see the ATA DEVICES section
       below.

       In some operating systems a NVMe device (e.g. SSD) may be given as the DEVICE. For more information see the NVME DEVICES section below.

       The reference document used for interpreting an INQUIRY is T10/BSR INCITS 502 Revision 19 which is draft SPC-5 revision 19, 14 February 2018).  It  can
       be found at http://www.t10.org . Obsolete and reserved items in the standard INQUIRY response output are displayed in square brackets.

OPTIONS
       Arguments to long options are mandatory for short options as well.  The options are arranged in alphabetical order based on the long option name.

       -a, --ata
	      Assume  given  DEVICE is an ATA or ATAPI device which can receive ATA commands from the host operating system. Skip the SCSI INQUIRY command and
	      use either the ATA IDENTIFY DEVICE command (for non-packet devices) or the ATA IDENTIFY PACKET DEVICE command. To show the response in hex,  add
	      a '--verbose' option. This option is only available in Linux.

       -B, --block=0|1
	      this option controls how the file handle to the DEVICE is opened. If this argument is 0 then the open is non-blocking. If the argument is 1 then
	      the  open	 is  blocking. In Unix a non-blocking open is indicated by a O_NONBLOCK flag while a blocking open is indicated by the absence of that
	      flag. The default value depends on the operating system and the type of DEVICE node. For Linux pass-throughs (i.e. the sg and bsg	 drivers)  the
	      default is 0.

       -c, --cmddt
	      set  the Command Support Data (CmdDt) bit (defaults to clear(0)). Used in conjunction with the --page=PG option where PG specifies the SCSI com‐
	      mand opcode to query. When used twice (e.g. '-cc') this utility forms a list by looping over all 256 opcodes (0  to  255	inclusive)  only  out‐
	      putting a line for commands that are found. The CmdDt bit is now obsolete; it has been replaced by the REPORT SUPPORTED OPERATION CODES command,
	      see the sg_opcodes(8) utility.

       -d, --descriptors
	      decodes  and  prints the version descriptors found in a standard INQUIRY response. There are up to 8 of them. Version descriptors indicate which
	      versions of standards and/or drafts the DEVICE complies with. The normal components of a standard INQUIRY are output (typically from  the	 first
	      36 bytes of the response) followed by the version descriptors if any.

       -e     see entry below for --vpd.

       -f, --force
	      As  a  sanity  check, the normal action when fetching VPD pages other than page 0x0 (the "Supported VPD pages" VPD page), is to first fetch page
	      0x0 and only if the requested page is one of the supported pages, to go ahead and fetch the requested page.
	      When this option is given, skip checking of VPD page 0x0 before accessing the requested VPD page. The prior check of VPD page 0x0	 is  known  to
	      crash certain USB devices, so use with care.

       -u, --export
	      prints  out  information	obtained  from	the device. The output can be modified by selecting a VPD page with PG (from --page=PG). If the device
	      identification VPD page 0x83 is given it prints out information in the form: "SCSI_IDENT_<assoc>_<type>=<ident>" to stdout. If the device serial
	      number VPD page 0x80 is given it prints out information in the form: "SCSI_SERIAL=<ident>". Other VPD pages are not supported. If no VPD page is
	      given it prints out information in the form: "SCSI_VENDOR=<vendor>", "SCSI_MODEL=<model>", and "SCSI_REVISION=<rev>", taken  from	 the  standard
	      inquiry. This may be useful for tools like udev(7) in Linux.

       -E, -x, --extended
	      prints the extended INQUIRY VPD page [0x86].

       -h, --help
	      print out the usage message then exit. When used twice, after the usage message, there is a list of available abbreviations than can be given to
	      the --page=PG option.

       -H, --hex
	      rather than decode a standard INQUIRY response, a VPD page or command support data; print out the response in hex and send the output to stdout.
	      Error  messages  and  warnings are typically output to stderr. When used twice with the ATA Information VPD page [0x89] decodes the start of the
	      response then outputs the ATA IDENTIFY (PACKET) DEVICE response in hexadecimal bytes (not 16 bit words). When used three times with the ATA  In‐
	      formation	 VPD page [0x89] or the --ata option, this utility outputs the ATA IDENTIFY (PACKET) DEVICE response in hexadecimal words suitable for
	      input to 'hdparm --Istdin'.  See note below.
	      To generate output suitable for placing in a file that can be used by a later invocation with the --inhex=FN  option,  use  the  '-HHHH'	option
	      (e.g. 'sg_inq -p di -HHHH /dev/sg3 > dev_id.hex').

       -i, --id
	      prints the device identification VPD page [0x83].

       -I, --inhex=FN
	      FN  is expected to be a file name (or '-' for stdin) which contains ASCII hexadecimal or binary representing an INQUIRY (including VPD page) re‐
	      sponse. This utility will then decode that response. It is preferable to also supply the --page=PG option, if not this utility will  attempt  to
	      guess  which VPD page (or standard INQUIRY) that the response is associated with. The hexadecimal should be arranged as 1 or 2 digits represent‐
	      ing a byte each of which is whitespace or comma separated. Anything from and including a hash mark to the end of a line is ignored. If the --raw
	      option is also given then FN is treated as binary.

       -l, --len=LEN
	      the number LEN is the "allocation length" field in the INQUIRY cdb.  This is the (maximum) length of the response returned by  the  device.  The
	      default  value  of  LEN  is 0 which is interpreted as: first request is for 36 bytes and if necessary execute another INQUIRY if the "additional
	      length" field in the response indicates that more than 36 bytes is available.
	      If LEN is greater than 0 then only one INQUIRY command is performed.  This means that the Serial Number (obtained from  the  Serial  Number  VPD
	      pgae (0x80)) is not fetched and therefore not printed.  See the NOTES section below about "36 byte INQUIRYs".

       -L, --long
	      this option causes more information to be decoded from the Identify command sent to a NVMe DEVICE.

       -m, --maxlen=LEN
	      this  option has the same action as the --len=LEN option above. It has been added for compatibility with the sg_vpd, sg_modes and sg_logs utili‐
	      ties.

       -O, --old
	      Switch to older style options. Please use as first option on the command line.

       -o, --only
	      Do not attempt to additionally retrieve the serial number VPD page (0x80) to enhance the output of a standard INQUIRY. So with this option given
	      and no others, this utility will send a standard INQUIRY SCSI command and decode its response. No other SCSI commands will be sent  to  the  DE‐
	      VICE.   Without  this  option an additional SCSI command is sent: a (non-standard) SCSI INQUIRY to fetch the Serial Number VPD page. However the
	      Serial Number VPD page is not mandatory (while the Device Identification page is mandatory but a billion USB keys ignore	that)  and  may	 cause
	      nuisance error reports.
	      For  NVMe	 devices only the Identify controller is performed, even if the DEVICE includes a namespace identifier. For example in FreeBSD given a
	      DEVICE named /dev/nvme0ns1 then an Identify controller is sent to /dev/nvme0 and nothing is sent to its "ns1" (first namespace).

       -p, --page=PG
	      the PG argument can be either a number of an abbreviation for a VPD page. To enumerate the available abbreviations for VPD pages use '-hh' or  a
	      bad  abbreviation (e.g, '--page=xxx'). When the --cmddt option is given (once) then PG is interpreted as an opcode number (so VPD page abbrevia‐
	      tions make little sense).
	      If PG is a negative number, then a standard INQUIRY is performed. This can be used to override some guessing logic  associated  with  the	 --in‐
	      hex=FN option.
	      If PG is not found in the 'Supported VPD pages' VPD page (0x0) then EDOM is returned. To bypass this check use the --force option.

       -r, --raw
	      in the absence of --inhex=FN then the output response is in binary.  The output should be piped to a file or another utility when this option is
	      used. The binary is sent to stdout, and errors are sent to stderr.
	      If used with --inhex=FN then the contents of FN is treated as binary.

       -s, --vendor
	      output  a	 standard INQUIRY response's vendor specific fields from offset 36 to 55 in ASCII. When used twice (i.e. '-ss') also output the vendor
	      specific field from offset 96 in ASCII. This is only done if the data passes some simple sanity checks.

       -v, --verbose
	      increase level of verbosity. Can be used multiple times.

       -V, --version
	      print out version string then exit.

       -e, --vpd
	      set the Enable Vital Product Data (EVPD) bit (defaults to clear(0)). Used in conjunction with the --page=PG option where PG  specifies  the  VPD
	      page  number to query. If the --page=PG is not given then PG defaults to zero which is the "Supported VPD pages" VPD page. A more up to date de‐
	      coding of VPD pages can be found in the sg_vpd(8) utility.

NOTES
       Some devices with weak SCSI command set implementations lock up when they receive commands they don't understand (and some lock up if they receive  re‐
       sponse lengths that they don't expect). Such devices need to be treated carefully, use the '--len=36' option. Without this option this utility will is‐
       sue an initial standard INQUIRY requesting 36 bytes of response data. If the device indicates it could have supplied more data then a second INQUIRY is
       issued to fetch the longer response. That second command may lock up faulty devices.

       ATA  or ATAPI devices that use a SCSI to ATA Translation layer (see SAT at www.t10.org) may support the SCSI ATA INFORMATION VPD page. This returns the
       IDENTIFY (PACKET) DEVICE response amongst other things.	The ATA Information VPD page can be fetched with '--page=ai'.

       In the INQUIRY standard response there is a 'MultiP' flag which is set when the device has 2 or more ports. Some vendors use the preceding vendor  spe‐
       cific  ('VS')  bit  to indicate which port is being accessed by the INQUIRY command (0 -> relative port 1 (port "a"), 1 -> relative port 2 (port "b")).
       When the 'MultiP' flag is set, the preceding vendor specific bit is shown in parentheses. SPC-3 compliant devices should use the device	identification
       VPD page (0x83) to show which port is being used for access and the SCSI ports VPD page (0x88) to show all available ports on the device.

       In  the	2.4  series  of	 Linux kernels the DEVICE must be a SCSI generic (sg) device. In the 2.6 series and later block devices (e.g.  disks and ATAPI
       DVDs) can also be specified. For example "sg_inq /dev/sda" will work in the 2.6 series kernels. From lk 2.6.6 other SCSI "char"	device	names  may  be
       used as well (e.g. "/dev/st0m").

       The number of bytes output by --hex and --raw is 36 bytes or the number given to --len=LEN (or --maxlen=LEN). That number is reduced if the "resid" re‐
       turned by the HBA indicates less bytes were sent back from DEVICE.

       The DEVICE is opened with a read-only flag (e.g. in Unix with the O_RDONLY flag).

ATA DEVICES
       There  are  two major types of ATA devices: non-packet devices (e.g. ATA disks) and packet devices (ATAPI). The majority of ATAPI devices are CD/DVD/BD
       drives in which the ATAPI transport carries the MMC set (i.e.  a SCSI command set). Further, both types of ATA devices can be connected to a host  com‐
       puter  via  a "SCSI" (or some other) transport. When an ATA disk is controlled via a SCSI (or non-ATA) transport then two approaches are commonly used:
       tunnelling (e.g. STP in Serial Attached SCSI (SAS)) or by emulating a SCSI device (e.g. with a SCSI to ATA translation layer, see SAT at www.t10.org ).
       Even when the physical transport to the host computer is ATA (especially in the case of SATA) the operating system may choose to put a SAT layer in the
       driver "stack" (e.g. libata in Linux).

       The main identifying command for any SCSI device is an INQUIRY. The corresponding command for an ATA non-packet device is IDENTIFY DEVICE while for  an
       ATA packet device it is IDENTIFY PACKET DEVICE.

       When  this  utility  is invoked for an ATAPI device (e.g. a CD/DVD/BD drive with "sg_inq /dev/hdc") then a SCSI INQUIRY is sent to the device and if it
       responds then the response to decoded and output and this utility exits. To see the response for an ATA IDENTIFY PACKET DEVICE command  add  the	 --ata
       option (e.g. "sg_inq --ata /dev/hdc).

       This  utility  doesn't decode the response to an ATA IDENTIFY (PACKET) DEVICE command, hdparm does a good job at that. The '-HHH' option has been added
       for use with either the '--ata' or '--page=ai' option to produce a format acceptable to "hdparm --Istdin".  An example: 'sg_inq --ata -HHH  /dev/hdc  |
       hdparm --Istdin'. See hdparm.

NVME DEVICES
       Currently  these	 device are typically SSDs (Solid State Disks) directly connected to a PCIe connector or via a specialized connector such as a M2 con‐
       nector. Linux and FreeBSD treat NVMe storage devices as separate from SCSI storage with device names like /dev/nvme0n1 (in Linux) and /dev/nvme0ns1 (in
       FreeBSD). The NVM Express group has a document titled "NVM Express: SCSI Translation Reference" which defines  a	 partial  "SCSI	 to  NVMe  Translation
       Layer" often known by its acronym: SNTL.

       On  operating systems where it is supported by this package, this utility will detect NVMe storage devices directly connected and send an Identify con‐
       troller NVMe Admin command and decode its response. A NVMe controller is architecturally similar to a SCSI target device. If the NVMe DEVICE  indicates
       a  namespace  then an Identify namespace NVMe Admin command is sent to that namespace and its response is decoded. Namespaces are numbered sequentially
       starting from 1. Namespaces are similar to SCSI Logical Units and their identifiers (nsid_s) can be thought of as SCSI LUNs. In the Linux  and  FreeBSD
       example	device names above the "n1" and the "ns1" parts indicate nsid 1 . If no namespace is given in the DEVICE then all namespaces found in the con‐
       troller are sent Identify namespace commands and the responses are decoded.

       To get more details in the response use the --long option. To only get the controller's Identify decoded use the --only option.

       It is possible that even though the DEVICE presents as a NVMe device, it has a SNTL and accepts SCSI commands. In this case to send a SCSI INQUIRY com‐
       mand (and fetch its VPD pages) use 'sg_vpd -p sinq <dev>' (or to get VPD pages: 'sg_vpd -p <vpd_page> <dev>').

EXIT STATUS
       The exit status of sg_inq is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

OLDER COMMAND LINE OPTIONS
       The options in this section were the only ones available prior to sg3_utils version 1.23 . Since then this utility defaults to the newer	 command  line
       options	which  can be overridden by using --old (or -O) as the first option. See the ENVIRONMENT VARIABLES section for another way to force the use of
       these older command line options.

       -36    only requests 36 bytes of response data for an INQUIRY. Furthermore even if the device indicates in its response it can supply more data, a sec‐
	      ond (longer) INQUIRY is not performed. This is a paranoid setting.  Equivalent to '--len=36' in the OPTIONS section.

       -a     fetch the ATA Information VPD page [0x89]. Equivalent to '--page=ai' in the OPTIONS section. This page is defined in SAT (see at www.t10.org).

       -A     Assume given DEVICE is an ATA or ATAPI device.  Equivalent to --ata in the OPTIONS section.

       -b     decodes the Block Limits VPD page [0xb0].	 Equivalent to '--page=bl' in the OPTIONS section. This page is defined in SBC-2 (see www.t10.org) and
	      later.

       -B=0|1 equivalent to --block=0|1 in OPTIONS section.

       -c     set the Command Support Data (CmdDt) bit (defaults to clear(0)). Used in conjunction with the -p=VPD_PG option to specify the SCSI  command  op‐
	      code to query. Equivalent to --cmddt in the OPTIONS section.

       -cl    lists  the command data for all supported commands (followed by the command name) by looping through all 256 opcodes. This option uses the CmdDt
	      bit which is now obsolete. See the sg_opcodes(8) utility.	 Equivalent to '--cmddt --cmddt' in the OPTIONS section.

       -d     decodes depending on context. If -e option is given, or any option that implies -e (e.g. '-i' or '-p=80'), then this utility attempts to	decode
	      the indicated VPD page.  Otherwise the version descriptors (if any) are listed following a standard INQUIRY response. In the version descriptors
	      sense, equivalent to --descriptors in the OPTIONS section.

       -e     enable  (i.e.  sets) the Vital Product Data (EVPD) bit (defaults to clear(0)).  Used in conjunction with the -p=VPD_PG option to specify the VPD
	      page to fetch. If -p=VPD_PG is not given then VPD page 0 (list supported VPD pages) is assumed.

       -f     Equivalent to --force in the OPTIONS section.

       -h     outputs INQUIRY response in hex rather than trying to decode it.	Equivalent to --hex in the OPTIONS section.

       -H     same action as -h.  Equivalent to --hex in the OPTIONS section.

       -i     decodes the Device Identification VPD page [0x83]. Equivalent to --id in the OPTIONS section. This page is made up of several  "designation  de‐
	      scriptors". If -h is given then each descriptor header is decoded and the identifier itself is output in hex. To see the whole VPD 0x83 page re‐
	      sponse in hex use '-p=83 -h'.

       -I=FN  equivalent to --inhex=FN in the OPTIONS section.

       -l=LEN equivalent to --len=LEN in the OPTIONS section.

       -L     equivalent to --long in the OPTIONS section.

       -m     decodes the Management network addresses VPD page [0x85]. Equivalent to '--page=mna' in the OPTIONS section.

       -M     decodes the Mode page policy VPD page [0x87].  Equivalent to '--page=mpp' in the OPTIONS section.

       -N, --new
	      Switch to the newer style options.

       -o     equivalent to --only in the OPTIONS section.

       -p=VPD_PG
	      used  in	conjunction  with the -e or -c option. If neither given then the -e option assumed. When the -e option is also given (or assumed) then
	      the argument to this option is the VPD page number.  The argument is interpreted as hexadecimal and is expected to be in the range 0 to  ff  in‐
	      clusive.	Only  VPD page 0 is decoded and it lists supported VPD pages and their names (if known). To decode the mandatory device identification
	      page (0x83) use the -i option. A now obsolete usage is when the -c option is given in which case the argument to this option is assumed to be  a
	      command opcode number. Recent SCSI draft standards have moved this facility to a separate command (see sg_opcodes(8)). Defaults to 0 so if -e is
	      given without this option then VPD page 0 is output.

       -P     decodes the Unit Path Report VPD page [0xc0] which is EMC specific.  Equivalent to '--page=upr' in the OPTIONS section.

       -r     outputs  the  response in binary to stdout.  Equivalent to --raw in the OPTIONS section.	Can be used twice (i.e. '-rr' (and '-HHH' has same ef‐
	      fect)) and if used with the -A or -a option yields output with the same format as "cat /proc/ide/hd<x>/identify" so that it can then be piped to
	      "hdparm --Istdin".

       -s     decodes the SCSI Ports VPD page [0x88].  Equivalent to '--page=sp' in the OPTIONS section.

       -u     equivalent to '--export' in the OPTIONS section.

       -v     increase level of verbosity. Can be used multiple times.

       -V     print out version string then exit.

       -x     decodes the Extended INQUIRY data VPD [0x86] page.  Equivalent to '--page=ei' in the OPTIONS section.

       -?     output usage message and exit. Ignore all other parameters.

EXAMPLES
       The examples in this page use Linux device names. For suitable device names in other supported Operating Systems see the sg3_utils(8) man page.

       To view the standard inquiry response use without options:

	  sg_inq /dev/sda

       Some SCSI devices include version descriptors indicating the various SCSI standards and drafts they support. They can be viewed with:

	  sg_inq -d /dev/sda

       Modern SCSI devices include Vital Product Data (VPD)pages which can be viewed with the SCSI INQUIRY command. To list the supported VPD pages  (but  not
       their contents) try:

	  sg_inq -e /dev/sda

       Some VPD pages can be read with the sg_inq utility but a newer utility called sg_vpd specializes in showing their contents. The sdparm utility can also
       be used to show the contents of VPD pages.

       Further examples of sg_inq together with some typical output can be found on http://sg.danny.cz/sg/sg3_utils.html web page.

ENVIRONMENT VARIABLES
       Since  sg3_utils	 version  1.23 the environment variable SG3_UTILS_OLD_OPTS can be given. When it is present this utility will expect the older command
       line options. So the presence of this environment variable is equivalent to using --old (or -O) as the first command line option.

AUTHOR
       Written by Douglas Gilbert

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2001-2021 Douglas Gilbert
       This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_opcodes(8), sg_vpd(8), sg_logs(8), sg_modes(8), sdparm(8), hdparm(8), sgdiag(scsirastools)

sg3_utils-1.46								  March 2021								     SG_INQ(8)
