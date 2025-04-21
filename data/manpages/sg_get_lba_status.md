SG_GET_LBA_STATUS(8)							   SG3_UTILS							  SG_GET_LBA_STATUS(8)

NAME
       sg_get_lba_status - send SCSI GET LBA STATUS(16 or 32) command

SYNOPSIS
       sg_get_lba_status  [--16]  [--32]  [--brief]  [--element-id=EI]	[--help]  [--hex]  [--inhex=FN] [--lba=LBA] [--maxlen=LEN] [--raw] [--readonly] [--re‐
       port-type=RT] [--scan-len=SL] [--verbose] [--version] DEVICE

DESCRIPTION
       Send the SCSI GET LBA STATUS(16) or GET LBA STATUS(32) command to the DEVICE and output the response. The 16 byte command  variant  was	introduced  in
       (draft)	SBC-3 revision 20 and devices that support logical block provisioning should support this command. The GET LBA STATUS(32) command was added in
       (draft) SBC-4 revision 14.

       The default action is to decode the response into one LBA status descriptor per line then output a header and the status descriptors to stdout. The de‐
       scriptor LBA is output in hex (prefixed by '0x') and the number of blocks is output in decimal followed by the provisioning status and additional  sta‐
       tus  in	decimal. The provisioning status can be in the range 0 to 15 of which only 0 (mapped or unknown), 1 (unmapped), 2 (anchored), 3 (mapped) and 4
       (unknown) are used currently. The amount of output can be reduced by the --brief option.

       Rather than send this SCSI command to DEVICE, if the --inhex=FN option is given, then the contents of the file named FN are decoded as  ASCII  hex  and
       then processed if it was the response of this command.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -S, --16
	      send  SCSI  GET  LBA STATUS(16) command which is the 16 byte variant. In the absence of the --16 or the --32 options the SCSI GET LBA STATUS(16)
	      command is sent. If both --16 and the --32 options are given then the GET LBA STATUS(16) command is sent.

       -T, --32
	      send SCSI GET LBA STATUS(32) command which is the 32 byte variant. When given together with the --16 option then this option is ignored (so  the
	      GET LBA STATUS(16) command is sent).

       -b, --brief
	      when  use	 once then one LBA status descriptor per line is output to stdout.  Each line has this format: "0x<descriptor_LBA>  0x<blocks> <provi‐
	      sioning_status> <additional_status>". So the descriptor's starting LBA and number of blocks are output in hex while the provisioning status  and
	      additional  status  are in decimal. When used twice (e.g. '-bb' or '--brief --brief') then the provisioning status of the given LBA (or LBA 0 if
	      the --lba option is not given) is output to stdout. A check is made that the given LBA lies in the range of the first returned  LBA  status  de‐
	      scriptor (as it should according to SBC-3 revision 20) and warnings are sent to stderr if it doesn't.

       -e, --element-id=EI
	      where  EI	 is  the  element  identifier of the physical element for which the LBAs shall be reported based on the value in the report type field
	      (i.e.  RT). This option is only active with the SCSI GET LBA STATUS(32) command (i.e. it is ignored if the GET LBA STATUS(16) command is sent).
	      Valid element identifiers are non-zero. The default value of EI is 0 which means in the context that no element identifier is specified.

       -h, --help
	      output the usage message then exit.

       -H, --hex
	      output response to this command in ASCII hex.

       -i, --inhex=FN
	      where FN is a filename whose contents are assumed to be ASCII hexadecimal bytes. See the "FORMAT OF FILES CONTAINING ASCII HEX" section  in  the
	      sg3_utils	 manpage  for  more information. If DEVICE is also given then it is ignored. If the --raw option is also given then the contents of FN
	      are treated as binary.

       -l, --lba=LBA
	      where LBA is the starting Logical Block Address (LBA) to check the provisioning status for. Note that the	 DEVICE	 chooses  how  many  following
	      blocks that it will return provisioning status for.

       -m, --maxlen=LEN
	      where  LEN  is  the (maximum) response length in bytes. It is placed in the cdb's "allocation length" field. If not given then 24 is used. 24 is
	      enough space for the response header and one LBA status descriptor.  LEN should be 8 plus a multiple of 16 (e.g. 24, 40, and 56 are suitable).

       -r, --raw
	      output response in binary (to stdout) unless the --inhex=FN option is also given. In that case the input file name (FN)  is  decoded  as	binary
	      (and the output is _not_ in binary).

       -R, --readonly
	      open the DEVICE read-only (e.g. in Unix with the O_RDONLY flag).	The default is to open it read-write.

       -t, --report-type=RT
	      where  RT	 is  0 for report all LBAs; 1 for report LBAs using non-zero provisioning status; 2 for report LBAs that are mapped; 3 for report LBAs
	      that are de-allocated; 4 for report LBAs that are anchored; 16 for report LBAs that may return an unrecovered error. The REPORT TYPE  field  was
	      added to the GET LBA STATUS cdb in sbc4r12.
	      Since  the  REPORT TYPE field is newer than the command, the response contains the RTP bit to indicate whether or not the DEVICE acts on the RE‐
	      PORT TYE field (set when it does act on it, clear otherwise).

       -s, --scan-len=SL
	      where SL is the scan length which is the maximum number of contiguous logical blocks to be scanned for logical blocks that meet the given report
	      type (i.e. RT). This option is only active with the SCSI GET LBA STATUS(32) command (i.e. it is ignored if the GET  LBA  STATUS(16)  command  is
	      sent).
	      The default value of SL is 0 which should be interpreted by the DEVICE as there is no limits to the number of LBAs that shall be scanned.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output). Additional output caused by this option is sent to stderr.

       -V, --version
	      print the version string and then exit.

NOTES
       In  SBC-3 revision 25 the calculation associated with the Parameter Data Length field in the response was modified. Prior to that the byte offset was 8
       and in revision 25 it was changed to 4.

       For a discussion of logical block provisioning see section 4.7 of sbc4r14.pdf at http://www.t10.org (or the corresponding section of a later draft).

EXIT STATUS
       The exit status of sg_get_lba_status is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2009-2019 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_write_same(8), sg_unmap(8), sg3_utils(8)

sg3_utils-1.45								  August 2019							  SG_GET_LBA_STATUS(8)
