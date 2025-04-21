SG_SEEK(8)								   SG3_UTILS								    SG_SEEK(8)

NAME
       sg_seek - send SCSI SEEK, PRE-FETCH(10) or PRE-FETCH(16) command

SYNOPSIS
       sg_seek [--10] [--count=NC] [--grpnum=GN] [--help] [--immed] [--lba=LBA] [--num-blocks=NUM] [--pre-fetch] [--readonly] [--skip=SB] [--time] [--verbose]
       [--version] [--wrap-offset=WO] DEVICE

DESCRIPTION
       Sends  a	 SCSI  SEEK(10), PRE-FETCH(10) or PRE-FETCH(16) command to the DEVICE. The SEEK command has been obsolete since SBC-2 (2005) but still is sup‐
       ported on some hard disks and even some SSDs (solid state disks). The PRE-FETCH command can be viewed as SEEK's modern replacement.  Instead of talking
       about moving the disk heads to the track containing the sort after LBA, it talks about bringing the sort after LBA (and a given number of blocks)  into
       the disk's cache. Also the PRE-FETCH commands have an IMMED field.

       The  PRE-FETCH commands can report "real" errors but usually they will report one of two "good" statuses. To do this they return the rarely used CONDI‐
       TION MET status. If the number of blocks does actually fit in the cache (when IMMED=0) or there is enough room in the cache when	 the  command  arrives
       (when  IMMED=1) then a CONDITION MET status is returned. If the requested number of blocks did not fit (IMMED=0) or would not fit (IMMED=1) then status
       GOOD is returned. So if a disk has a large cache and PRE-FETCH is used sparingly then the command is more likely to return  CONDITION  MET  than	 GOOD.
       This  presents  some SCSI sub-systems with problems as due to its rareness they mishandle CONDITION MET and treat it as an error (see NOTES section be‐
       low).

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -T, --10
	      use a 10 byte cdb command, either SEEK(10) or PRE-FETCH(10) command. In the absence of the --pre-fetch option, the SEEK(10) command is used.  If
	      the --pre-fetch option is given without this option then a PRE-FETCH(16) command is used.

       -c, --count=NC
	      NC is the number of commands (one of SEEK(10), PRE-FETCH(10) or PRE-FETCH(16)) that will be executed. The default value is 1. If an error occurs
	      it  is  noted and the program continues until NC is exhausted.  If NC is 0 then options are checked and the DEVICE is opened but no commands are
	      sent.

       -g, --grpnum=GN
	      GN is the group number, a value between 0 and 63 (in hex: 0x3f). The default value is 0. This option is  ignored	if  the	 selected  command  is
	      SEEK(10).

       -h, --help
	      output the usage message then exit.

       -i, --immed
	      this  option  only  applies to PRE-FETCH(10) and PRE-FETCH(16), setting the IMMED bit. Without this option, the DEVICE returns after it has com‐
	      pleted transferring all, or part of, the requested blocks into the cache. If this option is given the DEVICE returns after it  has  done	sanity
	      checks on the cdb (e.g. making sure the LBA is greater than the number of available blocks) and before it does the transfer into the cache.
	      Note that even when this option is given, the return status from the PRE-FETCH commands is still either CONDITION MET status (if the cache seems
	      to have enough free space for the transfer) or a GOOD status (if the cache does not seem to have enough free space).

       -l, --lba=LBA
	      LBA  is the starting logical block address that is placed in the command descriptor block (cdb) of the selected command. Note that the LBA field
	      in SEEK(10) and PRE-FETCH(10) is a 32 bit quantity, while with PRE-FETCH(16) it is a 64 bit quantity. The default value is 0 .

       -n, --num-blocks=NUM
	      NUM is the number of blocks, starting at and including LBA, to place in the DEVICE's cache. The SEEK(10) command does not use the NUM value. For
	      PRE-FETCH(10) NUM is a 16 bit quantity, while for PRE-FETCH(16) it is a 32 bit quantity. The default value is 1 . If NUM is 0  then  the	DEVICE
	      will attempt to transfer all blocks from the given LBA to the end of the medium.

       -p, --pre-fetch
	      this  option  selects  either  PRE-FETCH(10) or PRE-FETCH(16) commands. With the --10 also given, the PRE-FETCH(10) command is selected; without
	      that option PRE-FETCH(16) is selected. The default (in the absence of this and other 'selecting' options) the SEEK(10) command is selected.

       -r, --readonly
	      this option sets a 'read-only' flag when the underlying operating system opens the given DEVICE. This may not work since operating  systems  can
	      not  easily  determine whether a pass-through is a logical read or write operation so they take a risk averse stance and require read-write type
	      DEVICE opens irrespective of what is performed by the pass-through.

       -s, --skip=SB
	      SB is the number of logical block addresses to skip, between repeated commands when NC is greater than 1. The default value of SB is 1 . SB  may
	      be set to 0 so that all NC PRE-FETCH commands use the same LBA.

       -t, --time
	      if  given	 the  elapsed time to execute NC commands is recorded. This is printed out before this utility exits. If NC is greater than 1 then the
	      the "per command" time is also printed.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

       -w, --wrap-offset=WO
	      WO is the number of blocks, relative to LBA, that when exceeded, set the next command's logical block address back to  LBA.  Whether  this  "re‐
	      set-to-LBA" action occurs depends on the values NC and SB.

NOTES
       Prior to Linux kernel 4.17 the CONDITION MET status was logged as an error.  Recent versions of FreeBSD handle the CONDITION MET status properly.

       If either the --count=NC or --verbose option is given then a summary line like the following is output:

	   Command count=5, number of condition_mets=3, number of goods=2

       before the utility exits.

EXIT STATUS
       The  exit  status  of  sg_seek  is  0  (GOOD) or 25 (CONDITION_MET) when this utility is successful. If multiple commands are executed (e.g. when NC is
       greater than 1) then the result of the last executed SEEK or PRE-FETCH command sets the exit status. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2018 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_vpd(sg3_utils); sdparm(sdparm)

sg3_utils-1.43								September 2018								    SG_SEEK(8)
