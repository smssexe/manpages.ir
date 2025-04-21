clear(1)								 User commands								      clear(1)

NAME
       clear - clear the terminal screen

SYNOPSIS
       clear [-x] [-T terminal-type]

       clear -V

DESCRIPTION
       clear clears your terminal's screen and its scrollback buffer, if any.  clear retrieves the terminal type from the environment variable TERM, then con‐
       sults the terminfo terminal capability database entry for that type to determine how to perform these actions.

       The capabilities to clear the screen and scrollback buffer are named “clear” and “E3”, respectively.  The latter is a user-defined capability, applying
       an extension mechanism introduced in ncurses 5.0 (1999).

OPTIONS
       clear recognizes the following options.

       -T type	produces  instructions	suitable  for the terminal type.  Normally, this option is unnecessary, because the terminal type is inferred from the
		environment variable TERM.  If this option is specified, clear ignores the environment variables LINES and COLUMNS as well.

       -V	reports the version of ncurses associated with this program and exits with a successful status.

       -x	prevents clear from attempting to clear the scrollback buffer.

PORTABILITY
       Neither IEEE Std 1003.1/The Open Group Base Specifications Issue 7 (POSIX.1-2008) nor X/Open Curses Issue 7 documents clear.

       The latter documents tput, which could be used to replace this utility either via a shell script or by an alias (such as a symbolic link) to  run  tput
       as clear.

HISTORY
       A clear command using the termcap database and library appeared in 2BSD (1979).	Eighth Edition Unix (1985) later included it.

       The  commercial Unix arm of AT&T adapted a different BSD program (tset) to make a new command, tput, and replaced the clear program with a shell script
       that called “tput clear”.

	   /usr/bin/tput ${1:+-T$1} clear 2> /dev/null
	   exit

       In 1989, when Keith Bostic revised the BSD tput command to make it similar to AT&T's tput, he added a clear shell script as well.

	   exec tput clear

       The remainder of the script in each case is a copyright notice.

       In 1995, ncurses's clear began by adapting BSD's original clear command to use terminfo.	 The E3 extension came later.

       •   In June 1999, xterm provided an extension to the standard control sequence for clearing the screen.	Rather than clearing just the visible part  of
	   the screen using

	       printf '\033[2J'

	   one could clear the scrollback buffer as well by using

	       printf '\033[3J'

	   instead.  “XTerm Control Sequences” documents this feature as originating with xterm.

       •   A few other terminal emulators adopted it, such as PuTTY in 2006.

       •   In April 2011, a Red Hat developer submitted a patch to the Linux kernel, modifying its console driver to do the same thing.	 Documentation of this
	   change, appearing in Linux 3.0, did not mention xterm, although that program was cited in the Red Hat bug report (#683733) motivating the feature.

       •   Subsequently,  more terminal developers adopted the feature.	 The next relevant step was to change the ncurses clear program in 2013 to incorporate
	   this extension.

       •   In 2013, the E3 capability was not exercised by “tput clear”.  That oversight was addressed in 2016 by reorganizing tput to share  its  logic  with
	   clear and tset.

SEE ALSO
       tput(1), xterm(1), terminfo(5)

ncurses 6.4								  2023-12-16								      clear(1)
