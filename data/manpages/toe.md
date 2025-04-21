toe(1)									 User commands									toe(1)

NAME
       toe - list table of entries of terminfo terminal types

SYNOPSIS
       toe [-ahs] [-v [n]] [directory ...]

       toe [-u|-U] file

       toe -V

DESCRIPTION
       toe reports to the standard output stream the (primary) names and descriptions of the terminal types available to the terminfo library.	Each directory
       is scanned; if none are given, toe scans the default terminfo directory.

OPTIONS
       The  -h	option	can  be helpful to observe where toe is looking for terminal descriptions.  Other options support maintainers of terminfo terminal de‐
       scriptions.

       -a	lists entries from all terminal database directories that terminfo would search, instead of only the first that it finds.

		If the -s option is also given, toe adds a column to the report, showing (like conflict(1)) which entries belong to a given terminal database.
		An “*” marks entries that differ, and “+” marks equivalent entries.

		Without the -s option, toe does not attempt to merge duplicates in its report.

       -h	writes a heading naming each each directory as it is accessed.

       -s	sorts the output by the entry names.

       -u file	lists terminal type dependencies in file, a terminfo entry source or termcap database file.  The report summarizes the “use” (terminfo) and tc
		(termcap) relations: each line comprises the primary name of a terminal type employing use/tc capabilities, a colon, a	space-	and  tab-sepa‐
		rated list of primary names of terminal types thus named, and a newline.

       -U file	lists  terminal	 type  reverse	dependencies in file, a terminfo entry source or termcap database file.	 The report summarizes the “use” (ter‐
		minfo) and tc (termcap) reverse relations: each line comprises the primary name of a terminal type occurring in use/tc capabilities, a	colon,
		a space- and tab-separated list of primary names of terminal types naming them thus, and a newline.

       -v [n]	reports verbose status information to the standard error stream, showing toe's progress.

		The  optional parameter n is an integer between 1 and 10 inclusive, interpreted as for tic(1).	If ncurses is built without tracing support, n
		is ignored.

       -V	reports the version of ncurses associated with this program and exits with a successful status.

FILES
       /etc/terminfo
	      compiled terminal description database

PORTABILITY
       toe is not provided by other implementations.  There is no applicable X/Open or POSIX standard for it.

HISTORY
       toe replaces a -T option that was briefly supported by the ncurses infocmp utility in 1995.

       The -a and -s options were added in 2006 and 2011, respectively.

       The program's name originates with a developer's pun:

       •   tic,

       •   tac (now tack),

       •   toe.

EXAMPLES
       When not sorting with the -s option, the -a option reports all of the names found in all of the terminal database directories named in the TERMINFO and
       TERMINFO_DIRS environment variables.

	   xterm-color	   generic color xterm
	   xterm-xfree86   xterm terminal emulator (XFree86)
	   xterm-vt220	   xterm emulating vt220
	   xterm-256color  xterm with 256 colors
	   xterm-r6	   xterm X11R6 version
	   xterm-r5	   xterm R5 version
	   xterm-mono	   monochrome xterm
	   xterm	   xterm terminal emulator (X Window System)
	   vt220	   dec vt220
	   vt102	   dec vt102
	   vt100	   dec vt100 (w/advanced video)
	   vt52		   dec vt52
	   ...

       Use the -a and -s options together to show where each terminal description was found.

	   --> /etc/terminfo
	   ----> /lib/terminfo
	   ------> /usr/share/terminfo
	   --*---: vt100	   dec vt100 (w/advanced video)
	   --*---: vt102	   dec vt102
	   --*---: vt220	   dec vt220
	   --*---: vt52		   dec vt52
	   --*---: xterm	   xterm terminal emulator (X Window Sys‐
				   tem)
	   --*---: xterm-256color  xterm with 256 colors
	   --*---: xterm-color	   generic color xterm
	   --*---: xterm-mono	   monochrome xterm
	   --*---: xterm-r5	   xterm R5 version
	   --*---: xterm-r6	   xterm X11R6 version
	   --*---: xterm-vt220	   xterm emulating vt220
	   --*---: xterm-xfree86   xterm terminal emulator (XFree86)
	   ...

SEE ALSO
       captoinfo(1), infocmp(1), infotocap(1), tic(1), ncurses(3NCURSES), terminfo(5)

ncurses 6.4								  2024-01-13									toe(1)
