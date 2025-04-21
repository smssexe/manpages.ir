CAPTREE(8)							    System Manager's Manual							    CAPTREE(8)

NAME
       captree - display tree of process capabilities

SYNOPSIS
       captree [OPTIONS] [(pid|glob-name) ...]

DESCRIPTION
       captree displays the capabilities on the mentioned processes indicated by pid or glob-name value(s) given on the command line. If no pid etc values are
       supplied, pid=1 is implied. A pid value of 0 displays all the processes known to the kernel.

       The  POSIX.1e  capabilities  are	 displayed  in double quotes in the cap_from_text(3) format. The IAB tuple of capabilities is displayed between square
       brackets in the text format described in cap_iab(3).  Note, the IAB tuple text is omitted if it contains empty A and B components. This is because  the
       regular	POSIX.1e  text	contains information about the Inheritable flag already. This behavior can be overridden with the --verbose command line argu‐
       ment.

       Optional arguments (which must precede the list of pid|glob-name values):

       --help Displays usage information and exits. Note, modern Go runtimes exit with status 0 in this case, but older runtimes exit with status 2.

       --verbose
	      Displays capability sets and IAB tuples even when they are empty, or redundant.

       --depth=n
	      Displays the process tree to a depth of n.  Note, the default value for this parameter is 0, which implies infinite depth.

       --colo[u]r=false
	      Colo[u]rs the targeted PIDs, if stdout is a TTY, in red. This option defaults to true when running via a TTY. The	 --color=false	argument  will
	      suppress this color. Piping the output into some other program will also suppress the use of colo[u]r.

EXIT STATUS
       If  the supplied target cannot be found the exit status is 1. Should an unrecognized option be provided, the exit status is 2. Otherwise, captree exits
       with status 0.

REPORTING BUGS
       Please report bugs via:

       https://bugzilla.kernel.org/buglist.cgi?component=libcap&list_id=1090757

SEE ALSO
       cap_from_text(3), capabilities(7), and cap_iab(3).

       There is a longer article about captree, which includes some examples, here:

	  https://sites.google.com/site/fullycapable/captree

AUTHOR
       Andrew G. Morgan <morgan@kernel.org>

									  2022-04-11								    CAPTREE(8)
