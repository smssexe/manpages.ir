SG_GET_ELEM_STATUS(8)							   SG3_UTILS							 SG_GET_ELEM_STATUS(8)

NAME
       sg_get_elem_status - send SCSI GET PHYSICAL ELEMENT STATUS command

SYNOPSIS
       sg_get_elem_status  [--brief]  [--filter=FLT]  [--help]	[--hex]	 [--inhex=FN] [--maxlen=LEN] [--raw] [--readonly] [--report-type=RT] [--starting=ELEM]
       [--verbose] [--version] DEVICE

DESCRIPTION
       Send the SCSI GET PHYSICAL ELEMENT STATUS command to the DEVICE and output the response. The command was introduced in (draft) SBC-4 revision 16.

       The default action is to decode the response into one physical element status descriptor per line then output a header and the  status  descriptors  to
       stdout.	The amount of output can be reduced by the --brief option.

       Rather  than  send  this SCSI command to DEVICE, if the --inhex=FN option is given, then the contents of the file named FN are decoded as ASCII hex and
       then processed if it was the response of this command.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -b, --brief
	      tbd

       -f, --filter=FLT
	      where FLT is placed in a two bit field called FILTER in the GET PHYSICAL ELEMENT STATUS command. Only two values are defined for that  field:  0
	      for  all	element descriptors; 1 for those element descriptors that are outside 'spec' or have depopulation information to report. In both cases
	      the REPORT TYPE and STARTING ELEMENT fields may further restrict (reduce) the number of element descriptors returned. The default value is zero.

       -h, --help
	      output the usage message then exit.

       -H, --hex
	      output response to this command in ASCII hex.

       -i, --inhex=FN
	      where FN is a function name whose contents are assumed to be ASCII hexadecimal. If DEVICE is also given then DEVICE is ignored, a warning is is‐
	      sued and the utility continues, decoding the file named FN. See the "FORMAT OF FILES CONTAINING ASCII HEX" section in the sg3_utils manpage  for
	      more information. If the --raw option is also given then the contents of FN are treated as binary.

       -m, --maxlen=LEN
	      where  LEN  is  the (maximum) response length in bytes. It is placed in the cdb's "allocation length" field. If not given then 32 is used. 32 is
	      enough space for the response header only.  LEN should be a multiple of 32 (e.g. 32, 64, and 96 are suitable).

       -r, --raw
	      output response in binary (to stdout) unless the --inhex=FN option is also given. In that case the input file name (FN)  is  decoded  as	binary
	      (and the output is _not_ in binary).

       -R, --readonly
	      open the DEVICE read-only (e.g. in Unix with the O_RDONLY flag).	The default is to open it read-write.

       -t, --report-type=RT
	      where RT will be placed in the REPORT TYPE field of the GET PHYSICAL ELEMENT STATUS command. Currently only two values are defined: 0 for 'phys‐
	      ical element' and 1: for 'storage element'. The default value is 1 .

       -s, --starting=ELEM
	      where ELEM is the placed in the STARTING ELEMENT field of the GET PHYSICAL ELEMENT STATUS command. Only physical elements with identifiers equal
	      to or greater than ELEM are returned. The default value is zero which while it isn't a valid element identifier (since they must be non-zero) is
	      given in an example in Annex L of SBC-4 revision 17. So an ELEM of zero is assumed to be valid in this context.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output). Additional output caused by this option is sent to stderr.

       -V, --version
	      print the version string and then exit.

EXIT STATUS
       The exit status of sg_get_elem_status is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2019 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_get_lba_status(8), sg3_utils(8)

sg3_utils-1.45								  August 2019							 SG_GET_ELEM_STATUS(8)
