probe-bcache(8)							    System Manager's Manual						       probe-bcache(8)

NAME
       probe-bcache - probe a bcache device

SYNOPSIS
       probe-bcache [ -o udev ] device

OPTIONS
       -o     return UUID in udev style for invocation by udev rule as IMPORT{program}

USAGE
       Return UUID if device identified as bcache-formatted.

       Only  necessary	until support for the bcache superblock is included in blkid; in the meantime, provides just enough functionality for a udev script to
       create the /dev/disk/by-uuid symlink.

																	       probe-bcache(8)
