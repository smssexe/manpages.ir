nroff(1)							    General Commands Manual							      nroff(1)

Name
       nroff - format documents with groff for TTY (terminal) devices

Synopsis
       nroff [-bcCEhikpRStUVz] [-d ctext] [-d string=text] [-K fallback-encoding] [-m macro-package] [-M macro-directory] [-n page-number] [-o page-list]
	     [-P postprocessor-argument] [-r cnumeric-expression] [-r register=numeric-expression] [-T output-device] [-w warning-category] [-W warning-
	     category] [file ...]

       nroff --help

       nroff -v
       nroff --version

Description
       nroff  formats  documents  written  in the groff(7) language for typewriter-like devices such as terminal emulators.  GNU nroff emulates the AT&T nroff
       command using groff(1).	nroff generates output via grotty(1), groff's terminal output driver, which needs to know the character encoding  scheme  used
       by  the	device.	  Consequently,	 acceptable  arguments	to  the -T option are ascii, latin1, utf8, and cp1047; any others are ignored.	If neither the
       GROFF_TYPESETTER environment variable nor the -T command-line option (which overrides the environment variable) specifies a (valid) device, nroff  con‐
       sults  the  locale  to select an appropriate output device.  It first tries the locale(1) program, then checks several locale-related environment vari‐
       ables; see section “Environment” below.	If all of the foregoing fail, -Tascii is implied.

       The -b, -c, -C, -d, -E, -i, -m, -M, -n, -o, -r, -U, -w, -W, and -z options have the effects described in troff(1).  -c and -h imply “-P-c” and  “-P-h”,
       respectively;  -c is also interpreted directly by troff.	 In addition, this implementation ignores the AT&T nroff options -e, -q, and -s (which are not
       implemented in groff).  The options -k, -K, -p, -P, -R, -t, and -S are documented in groff(1).  -V causes nroff to display the constructed  groff  com‐
       mand  on	 the  standard	output stream, but does not execute it.	 -v and --version show version information about nroff and the programs it runs, while
       --help displays a usage message; all exit afterward.

Exit status
       nroff exits with error status 2 if there was a problem parsing its arguments, with status 0 if any of the options -V, -v,  --version,  or  --help  were
       specified, and with the status of groff otherwise.

Environment
       Normally,  the  path  separator	in environment variables ending with PATH is the colon; this may vary depending on the operating system.  For example,
       Windows uses a semicolon instead.

       GROFF_BIN_PATH
	      is a colon-separated list of directories in which to search for the groff executable before searching in PATH.  If unset, /usr/bin is used.

       GROFF_TYPESETTER
	      specifies the default output device for groff.

       LC_ALL
       LC_CTYPE
       LANG
       LESSCHARSET
	      are pattern-matched in this order for contents matching standard character encodings supported by groff in the event no -T option is  given  and
	      GROFF_TYPESETTER is unset, or the values specified are invalid.

Files
       /usr/share/groff/1.23.0/tmac/tty-char.tmac
	      defines  fallback	 definitions  of  roff	special	 characters.  These definitions more poorly optically approximate typeset output than those of
	      tty.tmac in favor of communicating semantic information.	nroff loads it automatically.

Notes
       Pager programs like more(1) and less(1) may require command-line options to correctly handle some output sequences; see grotty(1).

See also
       groff(1), troff(1), grotty(1), locale(1), roff(7)

groff 1.23.0								 31 March 2024								      nroff(1)
