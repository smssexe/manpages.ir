SG_TIMESTAMP(8)								   SG3_UTILS							       SG_TIMESTAMP(8)

NAME
       sg_timestamp - report or set timestamp on SCSI device

SYNOPSIS
       sg_timestamp  [--elapsed]  [--help]  [--hex] [--milliseconds=MS] [--no-timestamp] [--origin] [--raw] [--readonly] [--seconds=SECS] [--srep] [--verbose]
       [--version] DEVICE

DESCRIPTION
       Sends a SCSI REPORT TIMESTAMP or SET TIMESTAMP command to the DEVICE.  These commands are found in the SPC-5 draft standard revision 7 (spc5r07.pdf).

       If either the --milliseconds=MS or --seconds=SECS option is given (and both can't be given) then the SET TIMESTAMP command is sent; otherwise  the  RE‐
       PORT TIMESTAMP command is sent.

       The timestamp is sent and received from the DEVICE as the number of milliseconds since the epoch of 1970-01-01 00:00:00 UTC and is held in a 48 bit un‐
       signed integer. That same epoch is used by Unix machines, but they usually hold the number of seconds since that epoch. The Unix date command and espe‐
       cially its "+%s" format is useful in converting to and from timestamps and more humanly readable forms. See the EXAMPLES section below.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -e, --elapsed
	      assume  the timestamp in the REPORT TIMESTAMP is an elapsed time from an event such as a power cycle or hard reset and format the output as '<n>
	      days hh:mm:ss.xxx' where hh is hours (00 to 23 inclusive); mm is minutes (00 to 59 inclusive); ss is seconds (00 to 59  inclusive)  and  xxx  is
	      milliseconds (000 to 999 inclusive). If the number of days is 0 then '0 days' is not output unless this option is given two or more times.

       -h, --help
	      output the usage message then exit.

       -H, --hex
	      output the response to REPORT TIMESTAMP in ASCII hexadecimal on stderr. The response is not decoded.

       -m, --milliseconds=MS
	      where MS is the number of milliseconds since 1970-01-01 00:00:00 UTC to set in the DEVICE with the SCSI SET TIMESTAMP command.

       -N, --no-timestamp
	      when  REPORT  TIMESTAMP is called this option suppress the output of the timestamp value (in either seconds or milliseconds). This may be useful
	      in uncluttering the output when trying to decode the timestamp origin (see the --origin option).

       -o, --origin
	      the REPORT TIMESTAMP returned parameter data contains a "timestamp origin" field. When this option is given, that field is decoded  and  printed
	      out before the timestamp value is output. The default action (i.e. when the option is not given) is not to print out this decoded field.
	      T10  defines  this  field	 as "the most recent event that initialized the returned device clock". The value 0 indicates a power up of hard reset
	      initialized the clock; 2 indicates a SET TIMESTAMP initialized the clock while 3 indicates some other method initialized the clock.
	      When used once a descriptive string is output (in a line before the timestamp value). When used twice the value of the TIMESTAMP ORIGIN field is
	      output (in decimal, a value between 0 and 7 inclusive). When used thrice a line of the form 'TIMESTAMP_ORIGIN=<value>' is output.

       -r, --raw
	      output the SCSI REPORT TIMESTAMP response (i.e. the data-out buffer) in binary (to stdout). Note that the --origin and --srep  options  are  ig‐
	      nored when this option is given. Also all error and verbose messages are output to stderr.

       -R, --readonly
	      open the DEVICE read-only. The default action is to open the DEVICE read-write.

       -s, --seconds=SECS
	      where  SECS  is the number of seconds since 1970-01-01 00:00:00 UTC to set in the DEVICE with the SCSI SET TIMESTAMP command. SECS is multiplied
	      by 1000 before being used in the SET TIMESTAMP command.

       -S, --srep
	      report the number of seconds since 1970-01-01 00:00:00 UTC. This is done by dividing by 1000 the value returned by  the  SCSI  REPORT  TIMESTAMP
	      command.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

EXIT STATUS
       The exit status of sg_timestamp is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

NOTES
       The TCMOS and the SCSIP bits in the Control extension mode page (see sdparm) modify the actions of the timestamp held by a DEVICE.

       Currently  only	the  "Utilization  usage rate based on date and time" parameters within the Utilization log page (sbc4r09.pdf) use timestamps. See the
       sg_logs utility. Vendor specific commands and pages may also be using timestamps.

EXAMPLES
       On Unix machines (e.g. Linux, FreeBSD and Solaris) the date command is useful when working with timestamps.

       To fetch the timestamp from a DEVICE and display it in a humanly readable form the following could be used:

	  # sg_timestamp -S /dev/sdb
       1448993950
	  # date --date=@1448993950
       Tue Dec	1 13:19:10 EST 2015
	  # date -R --date="@1448993950"
       Tue, 01 Dec 2015 13:19:10 -0500

       The latter two date commands show different forms of the same date (i.e.	 1448993950 seconds since 1970-01-01 00:00:00 UTC). The sg_timestamp and  date
       commands can be combined using backquotes:

	  # date -R --date=@`sg_timestamp -S /dev/sdc`
       Wed, 16 Dec 2015 20:12:59 -0500

       To set the timestamp on the DEVICE to now (approximately) the following could be used:

	  # date +%s
       1448993955
	  # sg_timestamp --seconds=1448993955 /dev/sdb

       Those two command lines could be combined into one by using backquotes:

	  # sg_timestamp --seconds=`date +%s` /dev/sdb

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2015-2018 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sdparm(sdparm), sg_logs(sg3_utils)

sg3_utils-1.43								  April 2018							       SG_TIMESTAMP(8)
