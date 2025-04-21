GPG-CHECK-PATTERN(1)						     GNU Privacy Guard 2.4						  GPG-CHECK-PATTERN(1)

NAME
       gpg-check-pattern - Check a passphrase on stdin against the patternfile

SYNOPSIS
       gpg-check-pattern [options] patternfile

DESCRIPTION
       gpg-check-pattern checks a passphrase given on stdin against a specified pattern file.

       The  pattern file is line based with comment lines beginning on the first position with a #.  Empty lines and lines with only white spaces are ignored.
       The actual pattern lines may either be verbatim string pattern and match as they are (trailing spaces are ignored) or extended regular expressions  in‐
       dicated	by  a  / or !/ in the first column and terminated by another / or end of line.	If a regular expression starts with !/ the match result is re‐
       versed. By default all comparisons are case insensitive.

       Tag lines may be used to further control the operation of this tool.  The currently defined tags are:

       [icase]
	      Switch to case insensitive comparison for all further patterns.  This is the default.

       [case] Switch to case sensitive comparison for all further patterns.

       [reject]
	      Switch to reject mode.  This is the default mode.

       [accept]
	      Switch to accept mode.

       In the future more tags may be introduced and thus it is advisable not to start a plain pattern string with an open bracket.  The tags  must  be	 given
       verbatim on the line with no spaces to the left or any non white space characters to the right.

       In  reject  mode the program exits on the first match with an exit code of 1 (failure).	If at the end of the pattern list the reject mode is still ac‐
       tive the program exits with code 0 (success).

       In accept mode blocks of patterns are used.  A block starts at the next pattern after an "accept" tag and ends with the last pattern  before  the  next
       "accept"	 or  "reject" tag or at the end of the pattern list.  If all patterns in a block match the program exits with an exit code of 0 (success).  If
       any pattern in a block do not match the next pattern block is evaluated.	 If at the end of the pattern list the accept mode is still active the program
       exits with code 1 (failure).

OPTIONS
       --verbose
	      Enable extra informational output.

       --check
	      Run only a syntax check on the patternfile.

       --null Input is expected to be null delimited.

SEE ALSO
       gpg-agent(1),

       The full documentation for this tool is maintained as a Texinfo manual.	If GnuPG and the info program are properly installed at your site, the command

	 info gnupg

       should give you access to the complete manual including a menu structure and an index.

GnuPG 2.4.4								  2024-01-25							  GPG-CHECK-PATTERN(1)
