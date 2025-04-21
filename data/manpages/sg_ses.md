SG_SES(8)								   SG3_UTILS								     SG_SES(8)

NAME
       sg_ses - access a SCSI Enclosure Services (SES) device

SYNOPSIS
       sg_ses  [--all]	[--descriptor=DES]  [--dev-slot-num=SN]	 [--eiioe=A_F]	[--filter]  [--get=STR]	 [--hex]  [--index=IIA | --index=TIA,II] [--inner-hex]
       [--join] [--maxlen=LEN] [--page=PG] [--quiet] [--raw] [--readonly] [--sas-addr=SA] [--status] [--verbose] [--warn] DEVICE

       sg_ses --control [--byte1=B1] [--clear=STR] [--data=H,H...] [--data=@FN] [--descriptor=DES] [--dev-slot-num=SN] [--index=IIA | --index=TIA,II] [--mask]
       [--maxlen=LEN] [--nickname=SEN] [--nickid=SEID]	[--page=PG] [--readonly] [--sas-addr=SA] [--set=STR] [--verbose] DEVICE

       sg_ses --data=@FN --status [--raw --raw] [<all options from first form>]
       sg_ses --inhex=FN --status [--raw --raw] [<all options from first form>]

       sg_ses [--enumerate] [--index=IIA] [--list] [--help] [--version]

DESCRIPTION
       Fetches management information from a SCSI Enclosure Service (SES) device.  This utility can also modify the state of a SES device. The	DEVICE	should
       be  a SES device which may be a dedicated enclosure services processor in which case an INQUIRY response's Peripheral Device Type is 13 [0xd]. Alterna‐
       tively it may be attached to another type of SCSI device (e.g. a disk) in which case the EncServ bit is set in its INQUIRY response.

       If the DEVICE argument is given with no options then the names of all diagnostic pages (dpages) supported are listed. Most, but not necessarily all, of
       the named dpages are defined in the SES standards and drafts. The most recent reference for this utility is the draft SCSI Enclosure Services  4	 docu‐
       ment  T10/BSR  INCITS  555  Revision  5	at  http://www.t10.org	. Existing standards for SES, SES-2 and SES-3 are ANSI INCITS 305-1998 and ANSI INCITS
       448-2008 and ANSI INCITS 518-2017 respectively.

       The first form shown in the synopsis is for fetching and decoding dpages or fields from the SES DEVICE. A SCSI RECEIVE DIAGNOSTIC  RESULTS  command  is
       sent  to	 the  DEVICE  to  obtain each dpage response.  Rather than decoding a fetched dpage, it may be output in hex or binary with the --hex or --raw
       --raw options.

       The second form in the synopsis is for modifying dpages or fields held in the SES DEVICE. A SCSI SEND DIAGNOSTIC command containing a  "control"	 dpage
       is  sent	 to the DEVICE to cause changes. Changing the state of an enclosure (e.g. requesting the "ident" (locate) LED to flash on a disk carrier in an
       array) is typically done using a read-modify-write cycle.  See the section on CHANGING STATE below.

       The third form in the synopsis has two equivalent invocations shown. They decode the contents of a file (named FN) that holds a hexadecimal  or	binary
       representation  of  one,	 or many, SES dpage responses. Typically an earlier invocation of the first form of this utility with the '-HHHH' option would
       have generated that file. Since no SCSI commands are sent, the DEVICE argument if given will be ignored.

       The last form in the synopsis shows the options for providing command line help (i.e. usage information), listing out dpage and field  information  ta‐
       bles held by the utility (--enumerate), or printing the version string of this utility.

       There is a web page discussing this utility at http://sg.danny.cz/sg/sg_ses.html . Support for downloading microcode to a SES device has been placed in
       a separate utility called sg_ses_microcode.

       In the following sections "dpage" refers to a diagnostic page, either fetched with a SCSI RECEIVE DIAGNOSTIC RESULTS command, sent to the DEVICE with a
       SCSI SEND DIAGNOSTIC command, or fetched from data supplied by the --data= option.

OPTIONS
       Arguments to long options are mandatory for short options as well.  The options are arranged in alphabetical order based on the long option name.

       -a, --all
	      shows  (almost)  all  status dpages, following references and presenting the information as a long list whose indentation indicates the level of
	      nesting. This option is actually the same as --join, see its description for more information.

       -b, --byte1=B1
	      some modifiable dpages may need byte 1 (i.e. the second byte) set. In the Enclosure Control dpage, byte 1 contains the INFO, NON-CRIT, CRIT  and
	      UNRECOV  bits.  In  the Subenclosure String Out, Subenclosure Nickname Control and Download Microcode Control dpages, byte 1 is the Subenclosure
	      identifier.  Active when the --control and --data=H,H... options are used and the default value is 0. If the --clear=STR or --set=STR option  is
	      used  then  the value read from byte 1 is written back to byte 1.	 B1 is in decimal unless it is prefixed by '0x' or '0X' (or has a trailing 'h'
	      or 'H').

       -C, --clear=STR
	      Used to clear an element field in the Enclosure Control or Threshold Out dpage. Must be used together with an indexing option to	specify	 which
	      element  is  to  be changed. The Enclosure Control dpage is assumed if the --page=PG option is not given. See the STR FORMAT and the CLEAR, GET,
	      SET sections below.

       -c, --control
	      will send control information to the DEVICE via a SCSI SEND DIAGNOSTIC command. Cannot give both this option and --status.  The  Enclosure  Con‐
	      trol,  String Out, Threshold Out, Array Control (obsolete in SES-2), Subenclosure String Out, Subenclosure Nickname Control and Download Microc‐
	      ode dpages can be set currently. This option is assumed if either the --clear=STR or --set=STR option is given.

       -d, --data=H,H...
	      permits a string of comma separated (ASCII) hex bytes to be specified (limit 1024). A (single) space separated string of hex bytes is  also  al‐
	      lowed  but the list needs to be in quotes. This option allows the parameters to a control dpage to be specified. The string given should not in‐
	      clude the first 4 bytes (i.e. page code and length). See the DATA SUPPLIED section below.

       -d, --data=-
	      reads one or more data strings from stdin, limit almost 2**16 bytes. stdin may provide ASCII hex as a comma separated list  (i.e.	 as  with  the
	      --data=H,H...  option). Additionally spaces, tabs and line feeds are permitted as separators from stdin . Stops reading stdin when an EOF is de‐
	      tected. See the DATA SUPPLIED section below.

       -d, --data=@FN
	      reads one or more data strings from the file called FN, limit almost 2**16 bytes. The contents of the file is decoded in	the  same  fashion  as
	      stdin described in the previous option. See the DATA SUPPLIED section below.

       -D, --descriptor=DES
	      where  DES  is a descriptor name (string) as found in the Element Descriptor dpage. This is a medium level indexing alternative to the low level
	      --index= options. If the descriptor name contains a space then DES needs to be surrounded by quotes (single or  double)  or  the	space  escaped
	      (e.g. preceded by a backslash). See the DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS section below.

       -x, --dev-slot-num=SN, --dsn=SN
	      where  SN	 is  a	device slot number found in the Additional Element Status dpage. Only entries for FCP and SAS devices (with EIP=1) have device
	      slot numbers. SN must be a number in the range 0 to 255 (inclusive). 255 is used to indicate there is no corresponding device slot.  This	 is  a
	      medium level indexing alternative to the low level --index= options. See the DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS section below.

       -E, --eiioe=A_F
	      A_F  is  either the string 'auto' or 'force'. There was some fuzziness in the interpretation of the 'element index' field in the Additional Ele‐
	      ment Status (AES) dpage between SES-2 and SES-3. The EIIOE bit was introduced to resolve the problem but not all enclosures have caught  up.  In
	      the  SES-3 revision 12 draft the EIIOE bit was expanded to a 2 bit EIIOE field.  Using '--eiioe=force' will decode the AES dpage as if the EIIOE
	      field is set to 1.  Using '--eiioe=auto' will decode the AES dpage as if the EIIOE field is set to 1 if the first AES descriptor has its EIP bit
	      set and its element index field is 1 (in other words a heuristic to guess whether the EIIOE field should be set to 1 or 0).
	      If the enclosure sets the actual EIIOE field to 1 or more then this option has no effect. It is recommended that HP JBOD users set  --eiioe=auto
	      .

       -e, --enumerate
	      enumerate all known diagnostic page (dpage) names and SES elements that this utility recognizes plus the abbreviations accepted by this utility.
	      Ignores DEVICE if it is given. Essentially it is dumping out tables held internally by this utility.
	      If  --enumerate  is given twice, then the recognised acronyms for the --clear=STR, --get=STR and --set=STR options are listed. The utility exits
	      after listing this information, so most other options and DEVICE are ignored. Since there are many acronyms  for	the  Enclosure	Control/Status
	      dpage  then  the output can be further restricted by giving the --index=IIA option (e.g. "sg_ses -ee -I ts" to only show the acronyms associated
	      with the Enclosure Control/Status dpage's Temperature Sensor Element Type).

       -f, --filter
	      cuts down on the amount of output from the Enclosure Status dpage and the Additional Element Status dpage. When this option is given,  any  line
	      which has all its binary flags cleared (i.e. 0) is filtered out (i.e.  ignored).	If a line has some other value on it (e.g. a temperature) then
	      it  is  output.	When this option is used twice only elements associated with the "status=ok" field (in the Enclosure status dpage) are output.
	      The --filter option is useful for reducing the amount of output generated by the --join option.

       -G, --get=STR
	      Used to read a field in a status element. Must be used together with a an indexing option to specify which element is to be read. By default the
	      Enclosure Status dpage is read, the only other dpages that can be read are the Threshold In and Additional Element Status dpages. If a value  is
	      found  it	 is  output in decimal to stdout (by default) or in hexadecimal preceded by "0x" if the --hex option is also given. See the STR FORMAT
	      and the CLEAR, GET, SET sections below.

       -h, --help
	      output the usage message then exit. Since there is a lot of information, it is split into two pages. The most important is shown	on  the	 first
	      page.   Use  this option twice (e.g. '-hh') to output the second page. Note: the --enumerate option might also be viewed as a help or usage type
	      option. And like this option it has a "given twice" form: '-ee'.

       -H, --hex
	      If the --get=STR option is given then output the value found (if any) in hexadecimal, with a leading "0x".  Otherwise  output  the  response  in
	      hexadecimal;  with  trailing  ASCII if given once, without it if given twice, and simple hex if given three or more times. Ignored when all ele‐
	      ments from several dpages are being accessed (e.g. when the --join option is used). Also see the --raw option which may be used  with  this  op‐
	      tion.
	      To dump one of more dpage responses to stdout in ASCII parsable hexadecimal use -HHH or -HHHH. The triple H form only outputs hexadecimals which
	      is fine for a single dpage response. When all dpages are dumped (e.g.  with --page=all) then the quad H form adds the name of each dpage follow‐
	      ing  a  hash mark ('#'). The --data= option parser ignores everything from and including a hash mark to the end of the line. Hence the output of
	      the quad H form is still parsable plus it is easier for users to view and possibly edit. -HHHHH (that is 5) adds the page code in hex after  the
	      page's name in the comment.

       -I, --index=IIA
	      where  IIA is either an individual index (II) or an Element type abbreviation (A). See the INDEXES section below. If the --page=PG option is not
	      given then the Enclosure Status (or Control) dpage is assumed.  May be used with the --join option or  one  of  the  --clear=STR,	 --get=STR  or
	      --set=STR options. To enumerate the available Element type abbreviations use the --enumerate option.

       -I, --index=TIA,II
	      where  TIA,II is an type header index (TI) or Element type abbreviation (A) followed by an individual index (II). See the INDEXES section below.
	      If the --page=PG option is not given then the Enclosure Status (or Control) dpage is assumed. May be used with the --join option or one  of  the
	      --clear=STR, --get=STR or --set=STR options. To enumerate the available Element type abbreviations use the --enumerate option.

       -X, --inhex=FN
	      where  FN	 is a filename. It has the equivalent action of the --data=@FN option. If FN is '-' then stdin is read. This option has been given for
	      compatibility with other utilities in this package that use --inhex=FN (or --in=FN) is a similar way. See the "FORMAT OF FILES CONTAINING	 ASCII
	      HEX" section in the sg3_utils manpage for more information.

       -i, --inner-hex
	      the  outer  levels  of a status dpage are decoded and printed out but the innermost level (e.g. the Element Status Descriptor) is output in hex.
	      Also active with the Additional Element Status and Threshold In dpages. Can be used with an indexing option and/or --join options.

       -j, --join
	      group elements from the Element Descriptor, Enclosure Status and Additional Element Status dpages. If this option is given twice	then  elements
	      from the Threshold In dpage are also grouped. The order is dictated by the Configuration dpage.
	      There  can be a bewildering amount of information in the "join" output. The default is to output everything. Several additional options are pro‐
	      vided to cut down the amount displayed. If the indexing options is given, only the matching elements and their associated fields are output. The
	      --filter option (see its description) can be added to reduce the amount of output.  Also "--page=aes" (or "-p 0xa") can be added to suppress the
	      output of rows that don't have a "aes" dpage component. See the INDEXES and DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS sections below.

       -l, --list
	      This option is equivalent to --enumerate. See that option.

       -M, --mask
	      When modifying elements, the default action is a read (status element), mask, modify (based on --clear=STR or --set=STR) then write back as  the
	      control  element.	 The mask step is new in sg_ses version 1.98 and is based on what is allowable (and in the same location) in draft SES-3 revi‐
	      sion 6. Those masks may evolve, as they have in the past. This option re-instates the previous logic which was to ignore the mask step. The  de‐
	      fault action (i.e. without this option) is to perform the mask step in the read-mask-modify-write sequence.

       -m, --maxlen=LEN
	      LEN is placed in the ALLOCATION LENGTH field of the SCSI RECEIVE DIAGNOSTIC RESULTS commands sent by the utility. It represents the maximum size
	      of data the SES device can return (in bytes). It cannot exceed 65535 and defaults to 65532 (bytes). Some systems may not permit such large sizes
	      hence  the  need	for this option. If LEN is less than 0 or greater than 65535 then an error is generated. If LEN is 0 then the default value is
	      used, otherwise if it is less than 4 then it is ignored (and a warning is sent to stderr).

       -n, --nickname=SEN
	      where SEN is the new Subenclosure Nickname. Only the first 32 characters (bytes) of SEN are used, if more are given they are  ignored.  See  the
	      SETTING SUBENCLOSURE NICKNAME section below.

       -N, --nickid=SEID
	      where  SEID  is the Subenclosure identifier that the new Nickname (SEN) will be applied to. So SEID must be an existing Subenclosure identifier.
	      The default value is 0 which is the main enclosure.

       -p, --page=PG
	      where PG is a dpage abbreviation or code (a number). If PG starts with a digit it is assumed to be in decimal unless prefixed  by	 0x  for  hex.
	      Valid range is 0 to 255 (0x0 to 0xff) inclusive. Default is dpage 'sdp' which is page_code 0 (i.e. "Supported Diagnostic Pages") if no other op‐
	      tions are given.
	      Page  code  0xff	or abbreviation "all" is not a real dpage (as the highest real dpage is 0x3f) but instead causes all dpages whose page code is
	      0x2f or less to be output. This can be used with either the -HHHH or -rr to send either hexadecimal ASCII or binary respectively to stdout.
	      To list the available dpage abbreviations give "xxx" for PG; the same information can also be found with the --enumerate option.

       -q, --quiet
	      this suppresses the number of warnings and messages output. The exit status of the utility is unaffected by this option.

       -r, --raw
	      outputs the chosen status dpage in ASCII hex in a format suitable for a later invocation using the --data= option. A  dpage  less	 its  first  4
	      bytes (page code and length) is output. When used twice (e.g. -rr) the full dpage contents is output in binary to stdout.
	      when -rr is used together with the --data=- or --data=@FN then stdin or file FN is decoded as a binary stream that continues to be read until an
	      end  of  file (EOF). Once that data is read then the internal raw option is cleared to 0 so the output is not effected. So the -rr option either
	      changes how the input or output is treated, but not both.

       -R, --readonly
	      open the DEVICE read-only (e.g. in Unix with the O_RDONLY flag).	The default is to open it read-write.

       -A, --sas-addr=SA
	      this is an indexing method for SAS end devices (e.g. SAS disks). The utility will try to find the element or slot in the Additional Element Sta‐
	      tus dpage whose SAS address matches SA. For a SAS disk or tape that SAS address is its target port identifier for the port connected to that el‐
	      ement or slot.  Most SAS disks and tapes have two such target ports, usually numbered consecutively.
	      SATA devices in a SAS enclosure often receive "manufactured" target port identifiers from a SAS expander; typically  will	 have  a  SAS  address
	      close  to,  but  different  from, the SAS address of the expander itself. Note that this manufactured target port identifier is different from a
	      SATA disk's WWN.
	      SA is a hex number that is up to 8 digits long. It may have a leading '0x' or '0X' or a trailing 'h' or 'H'. This option is a medium level
	       indexing alternative to the low level --index= options.	See the DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS section below.

       -S, --set=STR
	      Used to set an element field in the Enclosure Control or Threshold Out dpage.  Must be used together with an indexing option  to	specify	 which
	      element  is  to  be changed. The Enclosure Control dpage is assumed if the --page=PG option is not given. See the STR FORMAT and CLEAR, GET, SET
	      sections below.

       -s, --status
	      will fetch dpage from the DEVICE via a SCSI RECEIVE DIAGNOSTIC RESULTS command (or from --data=@FN). In the absence of other options that	 imply
	      modifying	 a dpage (e.g.	--control or --set=STR) then --status is assumed, except when the --data= option is given.  When the --data= option is
	      given there is no default action: either the --control or this option must be given to distinguish between the two different ways that data will
	      be treated.

       -v, --verbose
	      increase the level of verbosity. For example when this option is given four times (in which case the short form  is  more	 convenient:  '-vvvv')
	      then if the internal join array has been generated then it is output to stderr in a form suitable for debugging.

       -V, --version
	      print the version string and then exit.

       -w, --warn
	      warn  about  certain irregularities with warnings sent to stderr. The join is a complex operation that relies on information from several dpages
	      to be synchronized. The quality of SES devices vary and to be fair, the descriptions from T10 drafts and standards  have	been  tweaked  several
	      times (see the EIIOE field) in order to clear up confusion.

INDEXES
       An  enclosure  can  have	 information about its disk and tape drives plus other supporting components like power supplies spread across several dpages.
       Addressing a specific element (overall or individual) within a dpage is complicated. This section describes low level indexing (i.e. choosing a	single
       element	(or  a group of related elements) from a large number of elements). If available, the medium level indexing described in the following section
       (DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS) might be simpler to use.

       The Configuration dpage is key to low level indexing: it contains a list of "type headers", each of which contains an Element type (e.g.	 Array	Device
       Slot),  a  Subenclosure	identifier (0 for the primary enclosure) and a "Number of possible elements". Corresponding to each type header, the Enclosure
       Status dpage has one "overall" element plus "Number of possible elements" individual elements all of which have the given Element type. For  some  Ele‐
       ment  types the "Number of possible elements" will be 0 so the Enclosure Status dpage has only one "overall" element corresponding to that type header.
       The Element Descriptor dpage and the Threshold (In and Out) dpages follow the same pattern as the Enclosure Status dpage.

       The numeric index corresponding to the overall element is "-1". If the Configuration dpage indicates a particular element type has "n" elements	and  n
       is greater than 0 then its indexes range from 0 to n-1 .

       The  Additional	Element Status dpage is a bit more complicated. It has entries for "Number of possible elements" of certain Element types. It does not
       have entries corresponding to the "overall" elements. To make the correspondence a little clearer each descriptor in this dpage optionally contains  an
       "Element Index Present" (EIP) indicator. If EIP is set then each element's "Element Index" field refers to the position of the corresponding element in
       the Enclosure Status dpage.

       Addressing  a  single  overall  element	or a single individual element is done with two indexes: TI and II. Both are origin 0. TI=0 corresponds to the
       first type header entry which must be a Device Slot or Array Device Slot Element type (according to the SES-2 standard). To address  the	 corresponding
       overall	instance,  II is set to -1, otherwise II can be set to the individual instance index. As an alternative to the type header index (TI), an Ele‐
       ment type abbreviation (A) optionally followed by a number (e.g. "ps" refers to the first Power Supply Element type; "ps1" refers to the second) can be
       given.

       One of two command lines variants can be used to specify indexes: --index=TIA,II where TIA is either an type header index (TI) or an Element  type  ab‐
       breviation  (A)	(e.g. "ps" or "ps1"). II is either an individual index or "-1" to specify the overall element. The second variant is --index=IIA where
       IIA is either an individual index (II) or an Element type abbreviation (A). When IIA is an individual index then the  option  is	 equivalent  to	 --in‐
       dex=0,II. When IIA is an Element type abbreviation then the option is equivalent to --index=A,-1.

       Wherever	 an individual index is applicable, it can be replaced by an individual index range. It has the form: <first_ii>-<last_ii>. For example: '3-5'
       will select individual indexes 3, 4 and 5 .

       To cope with vendor specific Element types (whose type codes should be in the range 128 to 255) the Element type code can be given as a number  with  a
       leading	underscore.  For  example  these  are equivalent: --index=arr and --index=_23 since the Array Device Slot Element type code is 23.  Also --in‐
       dex=ps1 and --index=_2_1 are equivalent.

       Another example: if the first type header in the Configuration dpage has has Array Device Slot Element type then --index=0,-1 is	 equivalent  to	 --in‐
       dex=arr. Also --index=arr,3 is equivalent to --index=3.

       The  --index= options  can be used to reduce the amount of output (e.g. only showing the element associated with the second 12 volt power supply). They
       may also be used together with with the --clear=STR, --get=STR and --set=STR options which are described in the STR section below.

DESCRIPTOR NAME, DEVICE SLOT NUMBER AND SAS ADDRESS
       The three options: --descriptor=DES, --dev-slot-num=SN and --sas-addr=SA allow medium level indexing, as an alternative to the low level	 --index=  op‐
       tions.  Only  one  of the three options can be used in an invocation. Each of the three options implicitly set the --join option since they need either
       the Element Descriptor dpage or the Additional Element Status dpage as well as the dpages needed by the --index= option.

       These medium level indexing options need support from the SES device and that support is optional. For example the --descriptor=DES needs  the  Element
       Descriptor dpage provided by the SES device however that is optional. Also the provided descriptor names need to be useful, and having descriptor names
       which are all "0" is not very useful. Also some elements (e.g. overall elements) may not have descriptor names.

       These  medium level indexing options can be used to reduce the amount of output (e.g. only showing the elements related to device slot number 3).  They
       may also be used together with with the --clear=STR, --get=STR and --set=STR options which are described in the following section. Note that even if  a
       field can be set (e.g. "do not remove" (dnr)) and that field can be read back with --get=STR confirming that change, the disk array may still ignore it
       (e.g. because it does not have the mechanism to lock the disk drawer).

STR FORMAT
       The STR operands of the --clear=STR, --get=STR and --set=STR options all have the same structure. There are two forms:
	     <acronym>[=<value>]
	     <start_byte>:<start_bit>[:<num_bits>][=<value>]

       The  <acronym> is one of a list of common fields (e.g. "ident" and "fault") that the utility converts internally into the second form. The <start_byte>
       is usually in the range 0 to 3, the <start_bit> must be in the range 0 to 7 and the <num_bits> must be in the range 1 to 64 (default 1). The number  of
       bits are read in the left to right sense of the element tables shown in the various SES draft documents. For example the 8 bits of byte 2 would be rep‐
       resented as 2:7:8 with the most significant bit being 2:7 and the least significant bit being 2:0 .

       The <value> is optional but is ignored if provided to --get=STR.	 For --set=STR the default <value> is 1 while for --clear=STR the default value is 0 .
       <value> is assumed to be decimal, hexadecimal values can be given in the normal fashion.

       The supported list of <acronym>s can be viewed by using the --enumerate option twice (or "-ee").

CLEAR, GET, SET
       The  --clear=STR,  --get=STR and --set=STR options can be used up to 8 times in the same invocation. Any <acronym>s used in the STR operands must refer
       to the same dpage.

       When multiple of these options are used (maximum: 8), they are applied in the order in which they appear on the command line. So if options  contradict
       each other, the last one appearing on the command line will be enforced. When there are multiple --clear=STR and --set=STR options, then the dpage they
       refer to is only written after the last one.

DATA SUPPLIED
       This  section describes the two scenarios that can occur when the --data= option is given. These scenarios are the same irrespective of whether the ar‐
       gument  to  the	--data=	 option	 is  a	string	of  hex	 bytes	on  the	 command  line,	 stdin	(indicated  by	--data=-)  or  names  a	  file	 (e.g.
       --data=@thresh_in_dpage.hex).

       The  first  scenario is flagged by the --control option. It uses the supplied data to build a 'control' dpage that will be sent to the DEVICE using the
       SCSI SCSI SEND DIAGNOSTIC command. The supplied dpage data should not include its first 4 bytes. Those 4 bytes are added	 by  this  utility  using  the
       --page=PG  option  with PG placed at byte offset 0). If needed, the --byte1=B1 option sets byte offset 1, else 0 is placed in that position. The number
       of bytes decoded from the data provided (i.e. its length) goes into byte offsets 2 and 3.

       The second scenario is flagged by the --status option. It decodes the supplied data assuming that it represents the response to one or  more  SCSI  RE‐
       CEIVE  DIAGNOSTIC RESULTS commands. Those responses have typically been captured from some earlier invocation(s) of this utility. Those earlier invoca‐
       tions could use the '-HHH' or '-HHHH' option and file redirection to capture that response (or responses) in hexadecimal. The supplied  dpage  response
       data is decoded according to the other command line options. For example the --join option could be given and that would require the data from multiple
       dpages  typically:  Configuration, Enclosure status, Element descriptor and Additional element status dpages. If in doubt use --page=all in the capture
       phase; having more dpages than needed is not a problem.

       By default the user supplied data is assumed to be ASCII hexadecimal in lines that don't exceed 512 characters. Anything on a line from and including a
       hash mark ('#') to the end of line is ignored. An end of line can be a LF or CR,LF and blank lines are ignored. Each separated pair (or	single)	 hexa‐
       decimal	digits	represent  a  byte  (and neither a leading '0x' nor a trailing 'h' should be given). Separators are either space, tab, comma or end of
       line.

       Alternatively binary can be used and this is flagged by the '-rr' option.  The --data=H,H... form cannot use binary values for  the  'H's,  only	 ASCII
       hexadecimal.  The  other	 two  forms (--data=- and --data=@FN) may contain binary data. Note that when the '-rr' option is used with --data=@FN that it
       only changes the interpretation of the input data, it does not change the decoding and output representation.

CHANGING STATE
       This utility has various techniques for changing the state of a SES device.  As noted above this is typically a read-modify-write type operation.  Most
       modifiable dpages have a "status" (or "in") page that can be read, and a corresponding "control" (or "out") dpage that can be written  back  to	change
       the state of the enclosure.

       The  lower  level technique provided by this utility involves outputting a "status" dpage in hex with --raw. Then a text editor can be used to edit the
       hex (note: to change an Enclosure Control descriptor the SELECT bit needs to be set). Next the control dpage data can fed back with  the	 --data=H,H...
       option together with the --control option; the --byte1=B1 option may need to be given as well.

       Changes to the Enclosure Control dpage (and the Threshold Out dpage) can be done at a higher level. This involves choosing a dpage (the default in this
       case is the Enclosure Control dpage). Next choose an individual or overall element index (or name it with its Element Descriptor string). Then give the
       element's  name	(e.g.  "ident" for RQST IDENT) or its position within that element (e.g. in an Array Device Slot Control element RQST IDENT is byte 2,
       bit 1 and 1 bit long ("2:1:1")). Finally a value can be given, if not the value for --set=STR defaults to 1 and for --clear=STR defaults to 0.

SETTING SUBENCLOSURE NICKNAME
       The format of the Subenclosure Nickname control dpage is different from its corresponding status dpage. The status dpage reports all Subenclosure Nick‐
       names (and Subenclosure identifier 0 is the main enclosure) while the control dpage allows only one of them to be changed. Therefore using  the	--data
       option technique to change a Subenclosure nickname is difficult (but still possible).

       To  simplify  changing a Subenclosure nickname the --nickname=SEN and --nickid=SEID options have been added. If the SEN string contains spaces or other
       punctuation, it should be quoted: surrounded by single or double quotes (or the offending characters escaped). If the --nickid=SEID is not given then a
       Subenclosure identifier of 0 is assumed. As a guard the --control option must also be given. If the --page=PG option is not given then  --page=snic  is
       assumed.

       When  --nickname=SEN  is	 given	then the Subenclosure Nickname Status dpage is read to obtain the Generation Code field. That Generation Code together
       with no more than 32 bytes from the Nickname (SEN) and the Subenclosure Identifier (SEID) are written to the Subenclosure Nickname Control dpage.

       There is an example of changing a nickname in the EXAMPLES section below.

NVME ENCLOSURES
       Support has been added to sg_ses (actually, its underlying library) for NVMe (also known as NVM Express) Enclosures. It can be considered  experimental
       in sg3_utils package version 1.43 and sg_ses version 2.34 .

       This  support is based on a decision by NVME-MI (Management Interface) developers to support the SES-3 standard. This was facilitated by adding NVME-MI
       SES Send and SES Receive commands that tunnel dpage contents as used by SES.

NOTES
       This utility can be used to fetch arbitrary (i.e. non SES) dpages (using the SCSI READ DIAGNOSTIC command). To this end the --page=PG and --hex options
       would be appropriate. Non-SES dpages can be sent to a device with the sg_senddiag utility.

       The most troublesome part of the join operation is associating Additional Element Status descriptors correctly. At least one SES device vendor has mis‐
       interpreted the SES-2 standard, specifically with its "element index" field interpretation. The code in this utility  interprets	 the  "element	index"
       field  as  per the SES-2 standard and if that yields an inappropriate Element type, adjusts its indexing to follow that vendor's misinterpretation. The
       SES-3 drafts have introduced the EIIOE (Element Index Includes Overall Elements) bit which later became a 2 bit field to resolve	 this  ambiguity.  See
       the --eiioe=A_F option.

       In  draft SES-3 revision 5 the "Door Lock" element name was changed to the "Door" (and an OPEN field was added to the status element). As a consequence
       the former 'dl' element type abbreviation has been changed to 'do'.

       There is a related command set called SAF-TE (SCSI attached fault-tolerant enclosure) for enclosure (including RAID) status and control.	 SCSI  devices
       that  support  SAF-TE  report  "Processor"  peripheral  device  type  (0x3)  in their INQUIRY response. See the sg_safte utility in this package or the
       safte-monitor utility on the Internet.

       The internal join array is statically allocated and its size is controlled by the MX_JOIN_ROWS define. Its current value is 520.

EXAMPLES
       Examples can also be found at http://sg.danny.cz/sg/sg_ses.html

       The following examples use Linux device names. For suitable device names in other supported Operating Systems see the sg3_utils(8) man page.

       To view the supported dpages:

	  sg_ses /dev/bsg/6:0:2:0

       To view the Configuration Diagnostic dpage:

	  sg_ses --page=cf /dev/bsg/6:0:2:0

       To view the Enclosure Status dpage:

	  sg_ses --page=es /dev/bsg/6:0:2:0

       To get the (attached) SAS address of that device (which is held in the Additional Element Sense dpage (dpage 10)) printed on hex:

	  sg_ses -p aes -D ArrayDevice07 -G at_sas_addr -H /dev/sg3

       To collate the information in the Enclosure Status, Element Descriptor and Additional Element Status dpages the --join option can be used:

	  sg_ses --join /dev/sg3

       This will produce a lot of output. To filter out lines that don't contain much information add the --filter option:

	  sg_ses --join --filter /dev/sg3

       Fields in the various elements of the Enclosure Control and Threshold dpages can be changed with the --clear=STR and --set=STR options. [All modifiable
       dpages can be changed with the --raw and --data=H,H... options.] The following example looks at making the "ident" LED (also called "locate") flash  on
       "ArrayDevice07" which is a disk (or more precisely the carrier drawer the disk is in):

	  sg_ses --index=7 --set=2:1:1 /dev/sg3

       If  the	Element	 Descriptor diagnostic dpage shows that "ArrayDevice07" is the descriptor name associated with element index 7 then this invocation is
       equivalent to the previous one:

	  sg_ses --descriptor=ArrayDevice07 --set=2:1:1 /dev/sg3

       Further the byte 2, bit 1 (for 1 bit) field in the Array Device Slot Control element is RQST IDENT for asking a disk carrier to flash a LED so  it  can
       be located. In this case "ident" (or "locate") is accepted as an acronym for that field:

	  sg_ses --descriptor=ArrayDevice07 --set=ident /dev/sg3

       To stop that LED flashing:

	  sg_ses --dev-slot-num=7 --clear=ident /dev/sg3

       The above assumes the descriptor name 'ArrayDevice07' corresponds to device slot number 7.

       Now for an example of a more general but lower level technique for changing a modifiable diagnostic dpage. The String (In and Out) diagnostics dpage is
       relatively  simple  (compared with the Enclosure Status/Control dpage). However the use of this lower level technique is awkward involving three steps:
       read, modify then write. First check the current String (In) dpage contents:

	  sg_ses --page=str /dev/bsg/6:0:2:0

       Now the "read" step. The following command will send the contents of the String dpage (from byte 4 onwards) to stdout. The output will be in ASCII  hex
       with pairs of hex digits representing a byte, 16 pairs per line, space separated. The redirection puts stdout in a file called "t":

	  sg_ses --page=str --raw /dev/bsg/6:0:2:0 > t

       Then  with  the	aid  of the SES-3 document (in revision 3: section 6.1.6) use your favourite editor to change t. The changes can be sent to the device
       with:

	  sg_ses --page=str --control --data=- /dev/bsg/6:0:2:0 < t

       If the above is successful, the String dpage should have been changed. To check try:

	  sg_ses --page=str /dev/bsg/6:0:2:0

       To change the nickname on the main enclosure:

	  sg_ses --nickname='1st enclosure' --control /dev/bsg/6:0:2:0

       To capture the whole state of an enclosure (from a SES perspective) for later analysis, this can be done:

	  sg_ses --page=all -HHHH /dev/sg5 > enc_sg5_all.hex

       Note that if there are errors or warnings they will be sent to stderr so they will appear on the command line (since only  stdout  is  redirected).   A
       text  editor  could  be	used  to  inspect  enc_sg5_all.hex  .  If  all	looks  in  order  at some later time, potentially on a different machine where
       enc_sg5_all.hex has been copied, a "join" could be done. Note that join reflects the state of the enclosure when the capture was done.

	  sg_ses --data=@enc_sg5_all.hex --status --join

EXIT STATUS
       The exit status of sg_ses is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2004-2021 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_inq, sg_safte, sg_senddiag, sg_ses_microcode, sg3_utils (sg3_utils); safte-monitor (Internet)

sg3_utils-1.46								 February 2021								     SG_SES(8)
