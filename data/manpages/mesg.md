MESG(1)									 User Commands								       MESG(1)

NAME
       mesg - display (or do not display) messages from other users

SYNOPSIS
       mesg [option] [n|y]

DESCRIPTION
       The mesg utility is invoked by a user to control write access others have to the terminal device associated with standard error output. If write access
       is allowed, then programs such as talk(1) and write(1) may display messages on the terminal.

       Traditionally, write access is allowed by default. However, as users become more conscious of various security risks, there is a trend to remove write
       access by default, at least for the primary login shell. To make sure your ttys are set the way you want them to be set, mesg should be executed in
       your login scripts.

       The mesg utility silently exits with error status 2 if not executed on a terminal. In this case executing mesg is pointless. The command line option
       --verbose forces mesg to print a warning in this situation. This behaviour has been introduced in version 2.33.

ARGUMENTS
       n
	   Disallow messages.

       y
	   Allow messages to be displayed.

       If no arguments are given, mesg shows the current message status on standard error output.

OPTIONS
       -v, --verbose
	   Explain what is being done.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       The mesg utility exits with one of the following values:

       0
	   Messages are allowed.

       1
	   Messages are not allowed.

       >1
	   An error has occurred.

FILES
       /dev/[pt]ty*, /dev/pts/[0-9]*

HISTORY
       mesg (I) appears in the UNIX Programmer’s Manual. It used to invert the current state with no argument before Version 7 AT&T UNIX.

SEE ALSO
       login(1), talk(1), write(1), wall(1), xterm(1)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The mesg command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								       MESG(1)
