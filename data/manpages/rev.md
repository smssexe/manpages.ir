REV(1)									 User Commands									REV(1)

NAME
       rev - reverse lines characterwise

SYNOPSIS
       rev [option] [file...]

DESCRIPTION
       The rev utility copies the specified files to standard output, reversing the order of characters in every line. If no files are specified, standard
       input is read.

       This utility is a line-oriented tool and it uses in-memory allocated buffer for a whole wide-char line. If the input file is huge and without line
       breaks then allocating the memory for the file may be unsuccessful.

OPTIONS
       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

       -0, --zero
	   Zero termination. Use the byte '\0' as line separator.

SEE ALSO
       tac(1)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The rev command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21									REV(1)
