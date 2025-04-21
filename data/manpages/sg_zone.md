SG_ZONE(8)								   SG3_UTILS								    SG_ZONE(8)

NAME
       sg_zone - send a SCSI ZONE modifying command

SYNOPSIS
       sg_zone	[--all]	 [--close]  [--count=ZC] [--element=EID] [--finish] [--help] [--open] [--remove] [--sequentialize] [--verbose] [--version] [--zone=ID]
       DEVICE

DESCRIPTION
       Sends a SCSI OPEN ZONE, CLOSE ZONE, FINISH ZONE, REMOVE ELEMENT AND MODIFY ZONES or SEQUENTIALIZE ZONE command to the DEVICE. All but the last two  are
       found  in the ZBC standard (INCITS 536-2016). The REMOVE ELEMENT AND MODIFY ZONES command was added in zbc2r07 while the SEQUENTIALIZE ZONE command was
       added in zbc2r01b.

       One and only one of the --open, --close, --finish, --remove and --sequentialize options can be chosen.

OPTIONS
       Arguments to long options are mandatory for short options as well.

       -a, --all
	      sets the ALL field in the cdb.

       -c, --close
	      causes the CLOSE ZONE command to be sent to the DEVICE.

       -C, --count=ZC
	      ZC is placed in the Zone Count field in the cdb of all four commands supported by this utility. ZC should be a value from 0  to  65535  (0xffff)
	      inclusive.

       -e, --element=EID
	      where EID is an element identifier which is a 32 bit unsigned integer starting at one. This field is used by the REMOVE ELEMENT AND MODIFY ZONES
	      command and its default value is zero (which is invalid). So the user needs to supply a valid element identifier when --remove is used.

       -f, --finish
	      causes the FINISH ZONE command to be sent to the DEVICE.

       -h, --help
	      output the usage message then exit.

       -o, --open
	      causes the OPEN ZONE command to be sent to the DEVICE.

       -r, --remove
	      causes the REMOVE ELEMENT AND MODIFY ZONES command to be sent to the DEVICE. In practice, --element=EID needs to be also given.

       -S, --sequentialize
	      causes the SEQUENTIALIZE ZONE command to be sent to the DEVICE.

       -v, --verbose
	      increase the level of verbosity, (i.e. debug output).

       -V, --version
	      print the version string and then exit.

       -z, --zone=ID
	      where  ID	 is placed in the cdb's ZONE ID field. A zone id is a zone start logical block address (LBA). The default value is 0. ID is assumed to
	      be in decimal unless prefixed with '0x' or has a trailing 'h' which indicate hexadecimal.

EXIT STATUS
       The exit status of sg_zone is 0 when it is successful. Otherwise see the sg3_utils(8) man page.

AUTHORS
       Written by Douglas Gilbert.

REPORTING BUGS
       Report bugs to <dgilbert at interlog dot com>.

COPYRIGHT
       Copyright © 2014-2021 Douglas Gilbert
       This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

SEE ALSO
       sg_rep_zones,sg_reset_wp(sg3_utils)

sg3_utils-1.43								 January 2021								    SG_ZONE(8)
