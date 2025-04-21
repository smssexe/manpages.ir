SETLOGCONS(8)							    System Manager's Manual							 SETLOGCONS(8)

NAME
       setlogcons - Send kernel messages to console N

SYNOPSIS
       setlogcons N

DESCRIPTION
       The command setlogcons N sets all kernel messages to the console specified as N.

       By default kernel messages are sent to the current console.

       To change the level of messages sent, use dmesg

AUTHORS
       setlogcons was originally written by Andries Brouwer for the kbd package.

       This manual page was written by Alastair McKinstry.

SEE ALSO
       dmesg(1)

kbd									  18 Apr 2004								 SETLOGCONS(8)
