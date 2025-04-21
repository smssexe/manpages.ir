E2LABEL(8)							    System Manager's Manual							    E2LABEL(8)

NAME
       e2label - Change the label on an ext2/ext3/ext4 file system

SYNOPSIS
       e2label device [ volume-label ]

DESCRIPTION
       e2label will display or change the volume label on the ext2, ext3, or ext4 file system located on device.

       If the optional argument volume-label is not present, e2label will simply display the current volume label.

       If  the	optional  argument  volume-label  is present, then e2label will set the volume label to be volume-label.  Ext2 volume labels can be at most 16
       characters long; if volume-label is longer than 16 characters, e2label will truncate it and print a warning message.  For other file systems that  sup‐
       port online label manipulation and are mounted e2label will work as well, but it will not attempt to truncate the volume-label at all.

       It is also possible to set the volume label using the -L option of tune2fs(8).

AUTHOR
       e2label was written by Theodore Ts'o (tytso@mit.edu).

AVAILABILITY
       e2label is part of the e2fsprogs package and is available from http://e2fsprogs.sourceforge.net.

SEE ALSO
       mke2fs(8), tune2fs(8)

E2fsprogs version 1.47.0						 February 2023								    E2LABEL(8)
