SG_REP_PIP(8)								   SG3_UTILS								 SG_REP_PIP(8)

NAME
       sg_rep_pip - send SCSI REPORT PROVISIONING INITIALIZATION PATTERN command

SYNOPSIS
       sg_rep_pip [--help] [--hex] [--maxlen=LEN] [--raw] [--readonly] [--verbose] [--version] DEVICE

DESCRIPTION
       Sends a SCSI REPORT PROVISIONING INITIALIZATION PATTERN command to DEVICE and outputs the data returned. This command is found in the SBC-4 draft stan‐
       dard, revision 21 (sbc4r21.pdf).

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -h, --help
	      output the usage message then exit.

       -H, --hex
	      output the response in hexadecimal to stdout. When used once the whole response is output in ASCII hexadecimal, prefixed by an address (starting
	      at  0)  on  each line. When used twice the whole response is output in hexadecimal with no leading address (on each line). The default action is
	      the same as giving the --hex option once.

       -m, --maxlen=LEN
	      where LEN is the (maximum) response length in bytes. It is placed in the cdb's "allocation length" field. If not given (or  LEN  is  zero)  then
	      8192 is used. The maximum allowed value of LEN is 1048576.

       -r, --raw
	      output the SCSI response (i.e. the data-out buffer) in binary (to stdout).

       -R, --readonly
	      open the DEVICE read-only (e.g. in Unix with the O_RDONLY flag).	The default is to open it read-write.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

EXIT STATUS
       The exit status of sg_rep_pip is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2020 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg3_utils(sg3_utils)

sg3_utils-1.46								   July 2020								 SG_REP_PIP(8)
