Proc::ProcessTable::Process(3pm)			      User Contributed Perl Documentation			      Proc::ProcessTable::Process(3pm)

NAME
       Proc::ProcessTable::Process - Perl process objects

SYNOPSIS
	$process->kill(9);
	$process->priority(19);
	$process->pgrp(500);
	$uid = $process->uid;
	...

DESCRIPTION
       This is a stub module to provide OO process attribute access for Proc::ProcessTable. Proc::ProcessTable::Process objects are constructed directly by
       Proc::ProcessTable; there is no constructor method, only accessors.

METHODS
       kill
	   Sends  a  signal  to	 the  process;	just an aesthetic wrapper for perl's kill. Takes the signal (name or number) as an argument. Returns number of
	   processes signalled.

       priority
	   Get/set accessor; if called with a numeric argument, attempts to reset the process's priority to that number using perl's <B>setpriority  function.
	   Returns the process priority.

       pgrp
	   Same as above for the process group.

       all other methods...
	   are simple accessors that retrieve the process attributes for which they are named. Currently supported are:

	     uid	 UID of process
	     gid	 GID of process
	     euid	 effective UID of process	    (Solaris only)
	     egid	 effective GID of process	    (Solaris only)
	     pid	 process ID
	     ppid	 parent process ID
	     spid	 sprod ID			    (IRIX only)
	     pgrp	 process group
	     sess	 session ID
	     cpuid	 CPU ID of processor running on	    (IRIX only)
	     priority	 priority of process
	     ttynum	 tty number of process
	     flags	 flags of process
	     minflt	 minor page faults		    (Linux only)
	     cminflt	 child minor page faults	    (Linux only)
	     majflt	 major page faults		    (Linux only)
	     cmajflt	 child major page faults	    (Linux only)
	     utime	 user mode time (1/100s of seconds) (Linux only)
	     stime	 kernel mode time		    (Linux only)
	     cutime	 child utime			    (Linux only)
	     cstime	 child stime			    (Linux only)
	     time	 user + system time
	     ctime	 child user + system time
	     timensec	 user + system nanoseconds part	    (Solaris only)
	     ctimensec	 child user + system nanoseconds    (Solaris only)
	     qtime	 cumulative cpu time		    (IRIX only)
	     size	 virtual memory size (bytes)
	     rss	 resident set size (bytes)
	     wchan	 address of current system call
	     fname	 file name
	     start	 start time (seconds since the epoch)
	     pctcpu	 percent cpu used since process started
	     state	 state of process
	     pctmem	 percent memory
	     cmndline	 full command line of process
	     ttydev	 path of process's tty
	     clname	 scheduling class name		    (IRIX only)

	   See the "README.osname" files in the distribution for more up-to-date information.

AUTHOR
       J. Bargsten, D. Urist

SEE ALSO
       Proc::ProcessTable, perl(1).

perl v5.38.2								  2024-03-31					      Proc::ProcessTable::Process(3pm)
