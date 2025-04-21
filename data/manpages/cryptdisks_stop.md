CRYPTDISKS_STOP(8)						       cryptsetup manual						    CRYPTDISKS_STOP(8)

NAME
       cryptdisks_stop - wrapper around cryptsetup that parses /etc/crypttab.

SYNOPSIS
       cryptdisks_stop <name>

DESCRIPTION
       cryptdisks_stop is a wrapper around cryptsetup that parses /etc/crypttab just like the initscript /etc/init.d/cryptdisks does and stops the dm-crypt
       mapping that corresponds to <name>.

SEE ALSO
       cryptdisks_start(8), cryptsetup(8), crypttab(5)

AUTHOR
       This manual page was written by Jonas Meurer <mejo@debian.org> in January 2008.

cryptsetup 2:2.7.0-1ubunt						  2024-11-14							    CRYPTDISKS_STOP(8)
