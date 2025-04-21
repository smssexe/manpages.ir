proc_loadavg(5)							      File Formats Manual						       proc_loadavg(5)

NAME
       /proc/loadavg - load average

DESCRIPTION
       /proc/loadavg
	      The first three fields in this file are load average figures giving the number of jobs in the run queue (state R) or waiting for disk I/O (state
	      D)  averaged  over 1, 5, and 15 minutes.	They are the same as the load average numbers given by uptime(1) and other programs.  The fourth field
	      consists of two numbers separated by a slash (/).	 The first of these is the number of currently runnable kernel scheduling entities (processes,
	      threads).	 The value after the slash is the number of kernel scheduling entities that currently exist on the system.  The fifth field is the PID
	      of the process that was most recently created on the system.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_loadavg(5)
