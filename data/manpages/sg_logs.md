SG_LOGS(8)								   SG3_UTILS								    SG_LOGS(8)

NAME
       sg_logs - access log pages with SCSI LOG SENSE command

SYNOPSIS
       sg_logs	[--All]	 [--all]  [--brief]  [--filter=FL]  [--hex]  [--list]  [--maxlen=LEN]  [--name]	 [--no_inq]  [--page=PG] [--paramp=PP] [--pcb] [--ppc]
       [--pdt=DT] [--raw] [--readonly] [--sp] [--temperature] [--transport] [--vendor=VP] [--verbose] DEVICE

       sg_logs [--brief] [--filter=FL] [--hex] --in=FN [--name] [--pdt=DT] [--raw] [--vendor=VP]

       sg_logs [--control=PC] [--in=FN] [--page=PG] [--raw] [--reset] --select [--sp] [--verbose] DEVICE

       sg_logs [--enumerate] [--filter=FL] [--help] [--vendor=VP] [--version]

       sg_logs [-a] [-A] [-b] [-D=DT] [-c=PC] [-e] [-f=FL] [-h] [-H] [-i=FN] [-l] [-L] [-m=LEN] [-M=VP] [-n] [-p=PG]  [-paramp=PP]  [-pcb]  [-ppc]  [-r]  [-R]
       [-select] [-sp] [-t] [-T] [-v] [-V] [-?]	 [-x] DEVICE

DESCRIPTION
       This  utility  sends  a	SCSI LOG SENSE command to the DEVICE and then outputs the response. The LOG SENSE command is used to fetch log pages which, if
       known, are decoded by default. When the --reset and/or --select option is given then a SCSI LOG SELECT command is issued to the	DEVICE.	 Alternatively
       one  or	more  log  page responses can be in a file read using the --in=FN option; in this case those responses are decoded and the DEVICE argument, if
       given, is ignored.

       In SPC-4 revision 5 a subpage code was introduced to both the LOG SENSE and LOG SELECT command. At the same time a page code field  was	introduced  to
       the  to	the LOG SELECT command. The log subpage code can range from 0 to 255 (0xff) inclusive. The subpage code value 255 can be thought of as a wild‐
       card.

       The SYNOPSIS section above is divided into five forms. The first form shows the options that can be used to send a LOG SENSE command to the DEVICE  and
       decode  its  response.  The second form fetches data from a file (named FN) and decodes it as if it were a response from a LOG SENSE command. The third
       form shows the options that can be used to send a LOG SELECT command. The fourth form groups various management	options.   The	last  form  shows  the
       older, deprecated command line interface which is maintained for backward compatibility.

OPTIONS
       Arguments to long options are mandatory for short options as well.  The options are arranged in alphabetical order based on the long option name.

       -A, --All
	      fetch  and decode all the log pages and subpages supported by the DEVICE.	 This requires a two stage process: first the "supported log pages and
	      subpages" log page is fetched, then for each entry in its response, the corresponding log page (or subpage) is fetched and displayed. Note  that
	      there  are many SCSI devices that do not support LOG SENSE subpages and respond to this option with an illegal request sense key (or ignored the
	      subpage field).

       -a, --all
	      outputs all the log pages supported by the DEVICE. This requires a two stage process: first the "supported log pages" log page is fetched,  then
	      for each entry in its response, the corresponding log page is fetched and displayed. When used twice (e.g. '-aa') all log pages and subpages are
	      fetched.

       -b, --brief
	      shorten the amount of output for some log pages. For example the Tape Alert log page only outputs parameters whose flags are set when --brief is
	      given.

       -c, --control=PC
	      accepts 0, 1, 2 or 3 for the PC argument:
		0 : current threshold values
		1 : current cumulative values
		2 : default threshold values
		3 : default cumulative values
	      The default value is 1 (i.e. current cumulative values).

       -e, --enumerate
	      this option is used to output information held in this utility's internal tables about known log pages including their name, acronym and fields.
	      If  given,  the DEVICE argument is ignored. When given once (e.g. '-e') all known pages are listed, sorted in ascending alphabetical acronym or‐
	      der.
	      When given twice, vendor pages are excluded.  When given three times, all known pages are listed, sorted in ascending numeric order listed; when
	      given four times, vendor pages are excluded from the numeric order.
	      The --filter=FL and --verbose options reduce the output of the enumeration.

       -f, --filter=FL
	      FL is either a parameter code when DEVICE is given, or a peripheral device type (pdt) (or other) if --enumerate is given.
	      In the parameter code case FL is a value between 0 and 65535 (0xffff) and only the parameter section matching that code is output. If the	 --hex
	      option  is  given the log parameter is output in hexadecimal rather than decoding it. If the --hex option is used twice then the leading address
	      on each line of hex is removed. If the --raw option is given then the log parameter is output in binary. Most log pages contain one or more  log
	      parameters. Examples of those that don't follow that convention are those pages that list supported log pages (and subpages).
	      In the --enumerate case, when FL >= zero it is taken as a pdt value and only log pages associated with that pdt plus generic pages listed in SPC
	      are  enumerated.	If  FL	is  -1 then the filter does nothing which is the same as not giving this option; when FL is -2 then only generic pages
	      listed in SPC are enumerated. If FL is -10 then only generic direct access like (e.g. disk) pages are enumerated. If FL is -11 then only generic
	      tape like pages (e.g. includes ADC) are enumerated.

       -h, --help
	      print out the usage message then exit.

       -H, --hex
	      The default action is to decode known log page numbers (and subpage numbers) into text. When this option is used once, the response is output in
	      hexadecimal. When used twice, each line of hex has the ASCII equivalent shown to the right. When used three times, the hex has  no  leading  ad‐
	      dress  nor  trailing  ASCII  making it suitable to be placed in a file (or piped). That file might later be used by another invocation using the
	      --in=FN option.

       -i, --in=FN
	      This option may be used in two different contexts. One is with the --select to send a LOG SELECT command to the given DEVICE; see the LOG SELECT
	      section below.
	      The other context is with no DEVICE argument given in which case the contents of FN are decoded as if it were the response of a LOG  SENSE  com‐
	      mand  (i.e.  a  log  page). For decoding the page and subpage numbers are taken from FN while the peripheral device type is either generic (i.e.
	      from SPC) or the value given by --pdt=DT.
	      FN is treated as a file name (or '-' for stdin) which contains ASCII hexadecimal or binary representing a log page. The  hexadecimal  should  be
	      arranged as 1 or 2 digits representing a byte each of which is whitespace or comma separated. Anything from and including a hash mark to the end
	      of line is ignored. If the --raw option is also given then FN is treated as binary.

       -l, --list
	      lists  the  names	 of all logs sense pages supported by this device. This is done by reading the "supported log pages" log page. When used twice
	      (e.g. '-ll') lists the names of all logs sense pages and subpages supported by this device, excluding pages whose subpage number is 0xff	(apart
	      from  page 0x0,0xff). When used three times then all supported pages and subpages reported by the device are list. So the page/subpage names and
	      not thrie content is shown with this option. There is a list of common log page codes below.

       -m, --maxlen=LEN
	      sets the "allocation length" field in the LOG SENSE cdb. The is the maximum length in bytes that the response will be. Without this  option  (or
	      LEN  equal  to  0)  this utility first fetches the 4 byte response then does a second access with the length indicated in the first (4 byte) re‐
	      sponse. Negative values and 1 for LEN are not accepted. LEN cannot exceed 65535 (0xffff).	 Responses can be quite	 large	(e.g.  the  background
	      scan results log page) and this option can be used to limit the amount of information returned.

       -n, --name
	      decode some log pages into 'name=value' entries, one per line. The name contains no space and may be abbreviated and the value is decimal unless
	      prefixed by '0x'. Nesting is indicated by leading spaces. This form is meant to be relatively easy to parse.

       -x, --no_inq
	      suppresses  the output of information obtained from an initial call to the INQUIRY command for the standard response. The default (assuming some
	      other options that suppress this output are also not given) is to output several device identification strings.
	      If this option is given twice (or more) then no INQUIRY command is sent hence there will be no device identification string output either.  Also
	      the  peripheral  device  type (PDT) field will not be obtained so this utility will not be able to differentiate between some log pages that are
	      device dependent. It will assume a PDT of 0 (i.e. a disk).

       -O, --old
	      Switch to older style options. Please use as first option.

       -p, --page=PG
	      log page name/number to access. PG is either an acronym, a page number, or a page, subpage number pair. Available acronyms can  be  listed  with
	      the  --enumerate	option. Page (0 to 63) and subpage (0 to 255) numbers are comma separated. They are decimal unless a hexadecimal indication is
	      given. A hexadecimal number can be specified by a leading "0x" or a trailing "h".
	      A few acronyms specify a range of subpage values in which case the acronym may be followed by a comma then a subpage  number.  This  method  can
	      also be used to fetch the Supported subpages log page (e.g. --page=temp,0xff).

       -P, --paramp=PP
	      PP  is  the  parameter pointer value to place in a field of that name in the LOG SENSE cdb. A decimal number in the range 0 to 65535 (0xffff) is
	      expected. When a value greater than 0 is given the --ppc option should be selected. The default value is 0.

       -q, --pcb
	      show Parameter Control Byte settings (only relevant when log parameters being output in ASCII).

       -Q, --ppc
	      sets the Parameter Pointer Control (PPC) bit in the LOG SENSE cdb. Default is 0 (i.e. cleared). This bit was made obsolete in SPC-4 revision 18.

       -D, --pdt=DT
	      DT is the peripheral device type that is used when it is not available from the DEVICE. There are two main cases	of  this:  with	 the  --pdt=DT
	      without a DEVICE and when --no_inq is used with a DEVICE.

       -r, --raw
	      output the response in binary to stdout. Error messages and warnings are output to stderr.
	      This option may also be given together with --in=FN in which case the contents of FN are interpreted as binary data (and the response is decoded
	      as normal, not dumped as binary).

       -R, --readonly
	      open  the DEVICE read-only (e.g. in Unix with the O_RDONLY flag). The default action is to try and open DEVICE read-write then if that fails try
	      to open again with read-only. However when a read-write open succeeds there may still be unwanted actions on the close (e.g. some OSes try to do
	      a SYNCHRONIZE CACHE command). So this option forces a read-only open on DEVICE and if it fails, this utility will exit. Note that	 options  like
	      --select most likely need a read-write open.

       -R, --reset
	      use SCSI LOG SELECT command (with the PCR bit set) to reset the all log pages (or the given page). Exactly what is reset depends on the accompa‐
	      nying  SP	 bit (i.e. --sp option which defaults to 0) and the PC ("page control") value (which defaults to 1). Supplying this option implies the
	      --select option as well. This option seems to clear error counter log pages but leaves pages like self-test results,  start-stop	cycle  counter
	      and  temperature	log pages unaffected. This option may be required to clear log pages if a counter reaches its maximum value since the log page
	      in which the counter is found will remain "stuck" at its maximum value until some user interaction (e.g. calling sg_logs with this option).

       -S, --select
	      use a LOG SELECT command. The default action (i.e. when neither this option nor --reset is given) is to do a LOG SENSE command. See the LOG  SE‐
	      LECT section.

       -s, --sp
	      sets  the	 Saving	 Parameters (SP) bit. Default is 0 (i.e. cleared). When set this instructs the device to store the current log page parameters
	      (as indicated by the DS and TSD parameter codes) in some non-volatile location.  Hence the log parameters will be preserved across power cycles.
	      This option is typically not needed, especially if the GLTSD flag is clear in the control mode page as this instructs the device to periodically
	      save all saveable log parameters to non-volatile locations.

       -t, --temperature
	      outputs the temperature. First looks in the temperature log page and if that is not available tries the Informational Exceptions log page	 which
	      may also have the current temperature (especially on older disks).

       -T, --transport
	      outputs the transport ('Protocol specific port') log page. Equivalent to setting '--page=18h'.

       -M, --vendor=VP
	      where  VP	 is  a	vendor/manufacturer (e.g. "sea" for Seagate) or product (group) acronym (e.g. "lto5" for the 5th generation LTO (tape) consor‐
	      tium). Either the whole log page is vendor specific (e.g. page numbers 0x30 to 0x3f) or part of a T10 defined log page is vendor specific.   For
	      example  SPC-5  defines  parameter  code	0x0 of page 0x2f (the Informational Exceptions log page) and states that the remaining parameter codes
	      (i.e. 0x1 to 0xffff) are vendor specific. Using a VP of "xxx" will list the available acronyms.
	      If this option is used with --page=PG and PG is an acronym then this option is ignored. If PG is a number (e.g. 0xc0) then VP is used to	choose
	      the which vendor specific page (e.g. sharing page number 0xc0) to decode.

       -v, --verbose
	      increase	level  of  verbosity.  When used with --enumerate, in the list of known log page names, those that have no associated decode logic are
	      followed by "[hex only]".

       -V, --version
	      print out version string then exit.

LOG SELECT
       The SCSI LOG SELECT command can be used to reset certain parameters to vendor specific defaults, save them to non-volatile storage (i.e. the media), or
       supply new page contents. This command has changed between SPC-3 and SPC-4 with the addition of the Page and Subpage Code fields which can only be  non
       zero when the Parameter list length is zero.

       The  --select  (or  --reset) option is required to issue a LOG SELECT command. If the --in=FN option is not given (or FN is effectively empty) then the
       Parameter list length field is set to zero. If the --in=FN option is is given then its decoded data is placed in the data-out buffer and its length  in
       bytes is placed in the Parameter list length field.

       Other options that are active with the LOG SELECT command are --control=PC, --reset (which sets the PCR bit) and --sp.

APPLICATION CLIENT
       This is the name of a log page that acts as a container for data provided by the user. An application client is a SCSI term for the program that issues
       commands to a SCSI initiator (often known as a Host Bus Adapter (HBA)). So, for example, this utility is a SCSI application client.

       The  Application	 Client	 log page has 64 log parameters with parameters codes 0 to 63. Each can hold 252 bytes of user binary data. That 252 bytes (or
       less) of user data, with a 4 byte prefix (for a total of 256 bytes) can be provided with the --in=FN option. A typical prefix would be '0,n,83,fc'. The
       "n" is the parameter code in hex so the last log parameter would be '0,3f,83,fc'. That log parameter could  be  read  back  at  some  later  time  with
       '--page=0xf --filter=0x<n>'.

NOTES
       This  utility  will usually do a double fetch of log pages with the SCSI LOG SENSE command. The first fetch requests a 4 byte response (i.e. place 4 in
       the "allocation length" field in the cdb). From that response it can calculate the actual length of the response which is what it asks for on the  sec‐
       ond  fetch.  This is typical practice in SCSI and guaranteed to work in the standards. However some older devices don't comply. For those devices using
       the --maxlen=LEN option will do a single fetch.	A value of 252 should be a safe starting point.

       Various log pages hold information error rates, device temperature, start stop cycles since the device was produced and the results of the last 20 self
       tests. Self tests can be initiated by the sg_senddiag(8) utility.  The smartmontools package provides much of the information found with sg_logs	 in  a
       form suitable for monitoring the health of SCSI disks and tape drives.

       The simplest way to find which log pages can be decoded by this utility is to use the --enumerate option. Some page names are known but there is no de‐
       code logic; such cases have "[hex only]" after the log page name when the --verbose option is given with --enumerate.

EXIT STATUS
       The exit status of sg_logs is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

OLDER COMMAND LINE OPTIONS
       The  options  in this section were the only ones available prior to sg3_utils version 1.23 . Since then this utility defaults to the newer command line
       options which can be overridden by using --old (or -O) as the first option. See the ENVIRONMENT VARIABLES section for another way to force the  use  of
       these older command line options.

       Options with arguments or with two or more letters can have an extra '-' prepended. For example: both '-pcb' and '--pcb' are acceptable.

       -a     outputs all the log pages supported by the device.  Equivalent to --all in the main description.

       -A     outputs all the log pages and subpages supported by the device.  Equivalent to '--all --all' in the main description.

       -c=PC  Equivalent to --control=PC in the main description.

       -e     enumerate internal tables to show information about known log pages.  Equivalent to --enumerate in the main description.

       -h     suppresses decoding of known log sense pages and prints out the response in hex instead.

       -i=FN  FN  is treated as a file name (or '-' for stdin) which contains ASCII hexadecimal representing a log page that will be sent as parameter data of
	      a LOG SELECT command. See the LOG SELECT section.

       -H     same action as '-h' in this section and equivalent to --hex in the main description.

       -l     lists the names of all logs sense pages supported by this device.	 Equivalent to --list in the main description.

       -L     lists the names of all logs sense pages and subpages supported by this device. Equivalent to '--list --list' in the main description.

       -m=LEN request only LEN bytes of response data. Default is 0 which is interpreted as all that is available. LEN is decimal unless it has a leading '0x'
	      or trailing 'h'.	Equivalent to --maxlen=LEN in the main description.

       -M=VP  Equivalent to --vendor=VP in the main description.

       -n     Equivalent to --name in the main description.

       -N, --new
	      Switch to the newer style options.

       -p=PG  log page code to access. PG is either an acronym, a page number, or a page, subpage pair. Available acronyms can be listed with the  --enumerate
	      option. Page (0 to 3f) and subpage (0 to ff) numbers are comma separated. The numbers are assumed to be hexadecimal.

       -paramp=PP
	      PP is the parameter pointer value (in hex) to place in command.  Should be a number between 0 and ffff inclusive.

       -pcb   show Parameter Control Byte settings (only relevant when log parameters being output in ASCII).

       -ppc   sets the Parameter Pointer Control (PPC) bit. Default is 0 (i.e. cleared).

       -r     use SCSI LOG SELECT command (PCR bit set) to reset the all log pages (or the given page). Equivalent to --reset in the main description.

       -R     Equivalent to --readonly in the main description.

       -select
	      use a LOG SELECT command. Equivalent to --select in the main description.

       -sp    sets the Saving Parameters (SP) bit. Default is 0 (i.e. cleared).	 Equivalent to --sp in the main description.

       -t     outputs the temperature. Equivalent to --temperature in the main description.

       -T     outputs the transport ('Protocol specific port') log page. Equivalent to --transport in the main description.

       -v     increase level of verbosity.

       -V     print out version string then exit.

       -x     suppress the INQUIRY command. Equivalent to --no_inq in the main description.

       -?     output usage message then exit.

ENVIRONMENT VARIABLES
       Since  sg3_utils	 version  1.23 the environment variable SG3_UTILS_OLD_OPTS can be given. When it is present this utility will expect the older command
       line options. So the presence of this environment variable is equivalent to using --old (or -O) as the first command line option.

AUTHOR
       Written by Douglas Gilbert

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2002-2020 Douglas Gilbert
       This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       smartctl(smartmontools), sg_senddiag(8)

sg3_utils-1.45								 January 2020								    SG_LOGS(8)
