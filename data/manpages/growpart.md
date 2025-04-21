growpart(1)								  cloud-utils								   growpart(1)

NAME
       growpart - extend a partition in a partition table to fill available space

SYNOPSIS
       growpart [OPTIONS] DISK PARTITION-NUMBER

       growpart partition
	  rewrite partition table so that partition takes up all the space it can
	  options:
	   -h | --help	    print Usage an exit
		--fudge F   if part could be resized, but change would be
			    less than 'F', do not resize (default: 20480)
	   -N | --dry-run   only report what would be done, show new 'sfdisk -d'
	   -v | --verbose   increase verbosity / debug

OPTIONS
       -h | --help
	      Show usage and exit

       -N | --dry-run
	      Only report what would be done

       --fudge COUNT
	      Only  modify  partition table if the given partition would grow more than COUNT sectors (512 bytes).  The default value is 20480 indicating that
	      no change will be made unless more than 10M of space would be gained.

       -v | --verbose
	      Give more information to stderr.

ARGUMENTS
       DISK   The device or disk image to operate on

       PARTITION-NUMBER
	      The number of the partition to resize (counting from 1)

DESCRIPTION
       Rewrite a partition table in a disk or disk image so that the given partition takes up as much space as it can.	After running, the partition will  end
       at the end of the disk, or at the beginning of the next partition.

EXAMPLES
       Extend partition 1 in /dev/sda to fill empty space until end of disk or next partition
		 growpart /dev/sda 1

       Extend partition 2 in disk image my.image.
		 growpart my.image 2

EXIT STATUS
       The exit status is 0 if the partition was successfully grown or if --dry-run was specified and it could be grown. The exit status is 1 if the partition
       could not be grown due to lack of available space. The exit status is 2 if an error occurred.

AUTHOR
       This manpage was written by Scott Moser <smoser@canonical.com> for Ubuntu systems (but may be used by others).  Permission is granted to copy, distrib‐
       ute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation.

       On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.

cloud-utils								  25 Feb 2011								   growpart(1)
