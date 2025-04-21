mtrace(1)							    General Commands Manual							     mtrace(1)

NAME
       mtrace - interpret the malloc trace log

SYNOPSIS
       mtrace [option]... [binary] mtracedata

DESCRIPTION
       mtrace is a Perl script used to interpret and provide human readable output of the trace log contained in the file mtracedata, whose contents were pro‐
       duced  by mtrace(3).  If binary is provided, the output of mtrace also contains the source file name with line number information for problem locations
       (assuming that binary was compiled with debugging information).

       For more information about the mtrace(3) function and mtrace script usage, see mtrace(3).

OPTIONS
       --help Print help and exit.

       --version
	      Print version information and exit.

BUGS
       For bug reporting instructions, please see: http://www.gnu.org/software/libc/bugs.html.

SEE ALSO
       memusage(1), mtrace(3)

Linux man-pages 6.7							  2023-10-31								     mtrace(1)
