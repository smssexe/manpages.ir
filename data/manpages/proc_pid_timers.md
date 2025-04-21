proc_pid_timers(5)						      File Formats Manual						    proc_pid_timers(5)

NAME
       /proc/pid/timers - POSIX timers

DESCRIPTION
       /proc/pid/timers (since Linux 3.10)
	      A list of the POSIX timers for this process.  Each timer is listed with a line that starts with the string "ID:".	 For example:

		  ID: 1
		  signal: 60/00007fff86e452a8
		  notify: signal/pid.2634
		  ClockID: 0
		  ID: 0
		  signal: 60/00007fff86e452a8
		  notify: signal/pid.2634
		  ClockID: 1

	      The lines shown for each timer have the following meanings:

	      ID     The  ID for this timer.  This is not the same as the timer ID returned by timer_create(2); rather, it is the same kernel-internal ID that
		     is available via the si_timerid field of the siginfo_t structure (see sigaction(2)).

	      signal This is the signal number that this timer uses to deliver notifications followed by a slash, and then the sigev_value value  supplied  to
		     the signal handler.  Valid only for timers that notify via a signal.

	      notify The  part	before	the  slash specifies the mechanism that this timer uses to deliver notifications, and is one of "thread", "signal", or
		     "none".  Immediately following the slash is either the string "tid" for timers with SIGEV_THREAD_ID notification,	or  "pid"  for	timers
		     that  notify  by other mechanisms.	 Following the "." is the PID of the process (or the kernel thread ID of the thread)  that will be de‐
		     livered a signal if the timer delivers notifications via a signal.

	      ClockID
		     This field identifies the clock that the timer uses for measuring time.  For most clocks, this is a number that matches one of the	 user-
		     space   CLOCK_*  constants	 exposed  via  <time.h>.   CLOCK_PROCESS_CPUTIME_ID  timers  display  with  a  value  of  -6  in  this	field.
		     CLOCK_THREAD_CPUTIME_ID timers display with a value of -2 in this field.

	      This file is available only when the kernel was configured with CONFIG_CHECKPOINT_RESTORE.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-09-07							    proc_pid_timers(5)
