GETPCAPS(8)							    System Manager's Manual							   GETPCAPS(8)

NAME
       getpcaps - display process capabilities

SYNOPSIS
       getpcaps [optional args] pid...

DESCRIPTION
       getpcaps	 displays  the capabilities on the processes indicated by the pid value(s) given on the command line.  A pid of 0 displays the capabilities of
       the process that is running getpcaps itself.

       The capabilities are displayed in the cap_from_text(3) format.

       Optional arguments:

       --help or --usage
	      Displays usage information and exits.

       --ugly or --legacy
	      Displays output in a somewhat ugly legacy format.

       --verbose
	      Displays usage in a legacy-like format but not quite so ugly in modern default terminal fonts.

       --iab  Displays IAB tuple capabilities from the process. The output format here is the text format described in cap_iab(3). Double  quotes  encase  the
	      regular process capabilities and square brackets encase the IAB tuple. This format is also used by captree(8).

REPORTING BUGS
       Please report bugs via:

       https://bugzilla.kernel.org/buglist.cgi?component=libcap&list_id=1090757

SEE ALSO
       capsh(1), cap_from_text(3), cap_iab(3), capabilities(7), captree(8), getcap(8), and setcap(8).

AUTHOR
       This manual page was originally written by Robert Bihlmeyer <robbe@debian.org>, for the Debian GNU/Linux system (but may be used by others).

									  2020-08-29								   GETPCAPS(8)
