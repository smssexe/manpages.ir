Proc::Killall(3pm)					      User Contributed Perl Documentation					    Proc::Killall(3pm)

NAME
       killall - Kill all instances of a process by pattern matching the command-line

SYNOPSIS
	       use Proc::Killall;

	       killall('HUP', 'xterm'); # SIGHUP all xterms
	       killall('KILL', '^netscape$'); # SIGKILL to "netscape"

DESCRIPTION
       This module provides one function, killall(), which takes two parameters: a signal name or number (see kill()) and a process pattern. This pattern is
       matched against the process' command-line as the "ps" command would show it ("ps" is not used internally, instead a package called "Proc::ProcessTable"
       is used).

       "killall" searches the process table and sends that signal to all processes which match the pattern. The return value is the number of processes that
       were successfully signaled. If any kills failed, the $! variable will be set based on that last one that failed (even if a successful kill happened
       afterward).

AUTHOR
       Written in 2000 by Aaron Sherman <ajs@ajs.com>

       "Proc::Killall" is copyright 2000 by Aaron Sherman, and may be distributed under the same terms as Perl itself.

PREREQUISITES
       "Proc::ProcessTable" is required for "Proc::Killall" to function.

SEE ALSO
       perl, perlfunc, perlvar, Proc::ProcessTable

perl v5.38.2								  2024-03-31							    Proc::Killall(3pm)
