infotocap(1)								 User commands								  infotocap(1)

NAME
       infotocap - convert a terminfo description into a termcap description

SYNOPSIS
       infotocap [tic-option] file ...

       infotocap -V

DESCRIPTION
       infotocap  translates  terminal	descriptions.	It  looks in each given text file for terminfo entries and, For each one found, it writes an analogous
       termcap description to the standard output stream.  terminfo “use” capabilities translate to termcap tc capabilities.  Because termcap is  a  less  ex‐
       pressive format than terminfo, some capabilities cannot be translated.

       This  utility  is  implemented as a link to tic(1), with the latter's -C option implied.	 You can use other tic options such as -1, -f, -v, -w, and -x.
       The -V option reports the version of ncurses associated with this program and exits with a successful status.

FILES
       /etc/terminfo
	      compiled terminal description database

PORTABILITY
       None of X/Open Curses, Issue 7 (2009), SVr4, or NetBSD document this application.

AUTHORS
       Eric S. Raymond <esr@snark.thyrsus.com> and
       Thomas E. Dickey <dickey@invisible-island.net>

SEE ALSO
       infocmp(1), tic(1), ncurses(3NCURSES), terminfo(5)

ncurses 6.4								  2023-12-10								  infotocap(1)
