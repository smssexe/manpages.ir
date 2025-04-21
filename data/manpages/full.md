full(4)								   Kernel Interfaces Manual							       full(4)

NAME
       full - always full device

CONFIGURATION
       If your system does not have /dev/full created already, it can be created with the following commands:

	   mknod -m 666 /dev/full c 1 7
	   chown root:root /dev/full

DESCRIPTION
       The file /dev/full has major device number 1 and minor device number 7.

       Writes to the /dev/full device fail with an ENOSPC error.  This can be used to test how a program handles disk-full errors.

       Reads from the /dev/full device will return \0 characters.

       Seeks on /dev/full will always succeed.

FILES
       /dev/full

SEE ALSO
       mknod(1), null(4), zero(4)

Linux man-pages 6.7							  2023-10-31								       full(4)
