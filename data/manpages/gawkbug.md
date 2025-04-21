GAWKBUG(1)							    General Commands Manual							    GAWKBUG(1)

NAME
       gawkbug - report a bug in gawk

SYNOPSIS
       gawkbug [--version] [--help] [email-address]

DESCRIPTION
       gawkbug	is a shell script to help the user compose and mail bug reports concerning gawk in a standard format.  gawkbug invokes the editor specified by
       the environment variable EDITOR on a temporary copy of the bug report format outline. The user must fill in the appropriate fields and exit the editor.
       gawkbug then mails the completed report to bug-gawk@gnu.org, or email-address.  If the report cannot be mailed, it is saved in the file dead.gawkbug in
       the invoking user's home directory.

       The bug report format outline consists of several sections.  The first section provides information about the machine, operating system, the gawk  ver‐
       sion,  and  the compilation environment.	 The second section should be filled in with a description of the bug.	The third section should be a descrip‐
       tion of how to reproduce the bug.  The optional fourth section is for a proposed fix.  Fixes are encouraged.

ENVIRONMENT
       gawkbug will utilize the following environment variables if they exist:

       EDITOR Specifies the preferred editor. If EDITOR is not set, gawkbug attempts to locate a number of alternative editors, including vim, and if it must,
	      emacs.  If gawkbug cannot locate any of the alternative editors, it attempts to execute vi.

       HOME   Directory in which the failed bug report is saved if the mail fails.

       TMPDIR Directory in which to create temporary files and directories.

SEE ALSO
       gawk(1)

AUTHORS
       Brian Fox, Free Software Foundation
       bfox@gnu.org

       Chet Ramey, Case Western Reserve University
       chet@po.cwru.edu

       Arnold Robbins
       bug-gawk@gnu.org

GNU Awk 5.2								  2022 Apr 18								    GAWKBUG(1)
