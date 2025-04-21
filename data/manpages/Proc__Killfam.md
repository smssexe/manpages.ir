Proc::Killfam(3pm)					      User Contributed Perl Documentation					    Proc::Killfam(3pm)

NAME
       Proc::Killfam - kill a list of pids, and all their sub-children

SYNOPSIS
	use Proc::Killfam;
	killfam $signal, @pids;

DESCRIPTION
       killfam accepts the same arguments as the Perl builtin kill command, but, additionally, recursively searches the process table for children and kills
       them as well.

EXAMPLE
       killfam 'TERM', ($pid1, $pid2, @more_pids);

KEYWORDS
       kill, signal

perl v5.38.2								  2024-03-31							    Proc::Killfam(3pm)
