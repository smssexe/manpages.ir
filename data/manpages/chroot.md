CHROOT(8)								 User Commands								     CHROOT(8)

NAME
       chroot - run command or interactive shell with special root directory

SYNOPSIS
       chroot [OPTION] NEWROOT [COMMAND [ARG]...]
       chroot OPTION

DESCRIPTION
       Run COMMAND with root directory set to NEWROOT.

       --groups=G_LIST
	      specify supplementary groups as g1,g2,..,gN

       --userspec=USER:GROUP
	      specify user and group (ID or name) to use

       --skip-chdir
	      do not change working directory to '/'

       --help display this help and exit

       --version
	      output version information and exit

       If no command is given, run '"$SHELL" -i' (default: '/bin/sh -i').

   Exit status:
       125    if the chroot command itself fails

       126    if COMMAND is found but cannot be invoked

       127    if COMMAND cannot be found

       -      the exit status of COMMAND otherwise

AUTHOR
       Written by Roland McGrath.

REPORTING BUGS
       GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
       Report any translation bugs to <https://translationproject.org/team/>

COPYRIGHT
       Copyright © 2023 Free Software Foundation, Inc.	License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
       This is free software: you are free to change and redistribute it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       chroot(2)

       Full documentation <https://www.gnu.org/software/coreutils/chroot>
       or available locally via: info '(coreutils) chroot invocation'

GNU coreutils 9.4							  April 2024								     CHROOT(8)
