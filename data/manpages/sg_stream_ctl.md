SG_STREAM_CTL(8)							   SG3_UTILS							      SG_STREAM_CTL(8)

NAME
       sg_stream_ctl - send SCSI STREAM CONTROL or GET STREAM STATUS command

SYNOPSIS
       sg_stream_ctl [--brief] [--close] [--ctl=CTL] [--get] [--help] [--id=SID] [--maxlen=LEN] [--open] [--readonly] [--verbose] [--version] DEVICE

DESCRIPTION
       Sends  a	 SCSI  STREAM CONTROL or GET STREAM STATUS command to the DEVICE.  These commands, together with WRITE STREAM(16 and 32) and several fields in
       the Block Limits Extension VPD page [0xb7] support the streams concept.	The stream commands were added in SBC-4 draft 8 (September 2015).

       Both STREAM CONTROL and GET STREAM STATUS commands expect data from the DEVICE (referred to as 'data-in'). In the  case	of  STREAM  CONTROL  only  the
       'open'  (STR_CTL<--0x1) actually needs the data-in as it contains the "Assigned stream id" if the open was successful. The assigned stream id should be
       used by subsequent WRITE STREAM commands and ultimately by the STREAM CONTROL close (STR_CTL<--0x2). Valid stream ids are between 1  and	 65535	inclu‐
       sive.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -b, --brief
	      this  option  reduces the output of the GET STREAM STATUS command to just one number (in decimal) per line sent to stdout. Those numbers are the
	      currently open stream ids. If an error occurs then -1 is sent to stdout and error related messages are sent to stderr. The default is  to	 print
	      more words (and fields) from the GET STREAM STATUS response.

       -c, --close
	      selects  the  STREAM  CONTROL  command and sets STR_CTL<--0x2 (i.e. 'close').  The --id=SID option should also be given because it defaults to 0
	      which is not a valid stream id.

       -C, --ctl=CTL
	      CTL is the value placed in the STR_CTL field of the STREAM CONTROL command (cdb). It is a two bit field so has 4 variants: 0 and 3 are reserved;
	      1 opens are new stream and 2 closes the given stream id. '--ctl=1' is equivalent to '--open' while '--ctl=2' is equivalent to '--close'.

       -g, --get
	      selects the GET STREAM STATUS command. If the --id=SID option is also given the the response starts lists open stream  ids  from	and  including
	      SID. If the --id=SID option is not given (or SID is 0) then all open stream id will be returned in the response (data-in) as long as the alloca‐
	      tion  length (defaults to 248 bytes which can be overridden by the --maxlen=LEN option) is long enough. This is the default action of this util‐
	      ity (i.e. GET STREAM STATUS command) if no "selecting" options are given.

       -h, --help
	      output the usage message then exit.

       -i, --id=SID
	      SID is a stream id, a value between 1 and 65535. It is used by STREAM CONTROL (close) to identify the stream to close. It is  used  by  the  GET
	      STREAM STATUS command as the starting stream id (from and including); so stream ids that are less than SID will not appear in the response.

       -m, --maxlen=LEN
	      LEN  is the maximum length the response can be. It becomes the ALLOCATION LENGTH field in both commands. The default (in the absence of this op‐
	      tion) is 8 bytes for STREAM CONTROL and 248 bytes for GET STREAM STATUS.

       -o, --open
	      selects the STREAM CONTROL command and sets STR_CTL<--0x1 (i.e. 'open').	If the --id=SID option is given then it is ignored.  The  user	should
	      observe  the  response  as the "Assigned stream id" is printed on stdout if the open is successful, if not '-1' is sent to stdout and error mes‐
	      sages are sent to stderr. If the --brief option is also given then the only thing sent to stdout is a number of the assigned  stream  id	(1  to
	      65535 inclusive) or '-1' if there is an error.

       -r, --readonly
	      this  option  sets a 'read-only' flag when the underlying operating system opens the given DEVICE. This may not work since operating systems can
	      not easily determine whether a pass-through command is a logical read or write operation on the media (or its metadata)  so  they	 take  a  risk
	      averse stance and require read-write type permissions on the DEVICE open irrespective of what is performed by the pass-through.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

NOTES
       There  are no special read commands for streams. This implies that "normal" READs (6, 10, 12, 16 or 32) can be used. Note that when a stream is closed,
       all resources associated with that stream id are removed, apart from the data in the written LBAs. To make sure the reading back data  is  not  delayed
       too  much by error recovery (in the presence of media errors) the user may set the RECOVERY TIME LIMIT field (RTL, units for non-zero values: millisec‐
       onds) in the 'Read-write error recovery' mode page. This can be done with the sdparm utility.

       The SCSI WRITE STREAM (16 and 32) commands can be found in the sg_write_x utility in this package.

EXIT STATUS
       The exit status of sg_stream_ctl is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2018 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_vpd,sg_write_x(sg3_utils); sdparm(sdparm)

sg3_utils-1.43								  March 2018							      SG_STREAM_CTL(8)
