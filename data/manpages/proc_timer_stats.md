proc_timer_stats(5)						      File Formats Manual						   proc_timer_stats(5)

NAME
       /proc/timer_stats - timer statistics

DESCRIPTION
       /proc/timer_stats (from	Linux 2.6.21 until Linux 4.10)
	      This  is a debugging facility to make timer (ab)use in a Linux system visible to kernel and user-space developers.  It can be used by kernel and
	      user-space developers to verify that their code does not make undue use of timers.  The goal is to avoid unnecessary wakeups, thereby optimizing
	      power consumption.

	      If enabled in the kernel (CONFIG_TIMER_STATS), but not used, it has almost zero run-time overhead and a relatively  small	 data-structure	 over‐
	      head.  Even if collection is enabled at run time, overhead is low: all the locking is per-CPU and lookup is hashed.

	      The /proc/timer_stats file is used both to control sampling facility and to read out the sampled information.

	      The timer_stats functionality is inactive on bootup.  A sampling period can be started using the following command:

		  # echo 1 > /proc/timer_stats

	      The following command stops a sampling period:

		  # echo 0 > /proc/timer_stats

	      The statistics can be retrieved by:

		  $ cat /proc/timer_stats

	      While sampling is enabled, each readout from /proc/timer_stats will see newly updated statistics.	 Once sampling is disabled, the sampled infor‐
	      mation is kept until a new sample period is started.  This allows multiple readouts.

	      Sample output from /proc/timer_stats:

		  $ cat /proc/timer_stats
		  Timer Stats Version: v0.3
		  Sample period: 1.764 s
		  Collection: active
		    255,     0 swapper/3	hrtimer_start_range_ns (tick_sched_timer)
		     71,     0 swapper/1	hrtimer_start_range_ns (tick_sched_timer)
		     58,     0 swapper/0	hrtimer_start_range_ns (tick_sched_timer)
		      4,  1694 gnome-shell	mod_delayed_work_on (delayed_work_timer_fn)
		     17,     7 rcu_sched	rcu_gp_kthread (process_timeout)
		  ...
		      1,  4911 kworker/u16:0	mod_delayed_work_on (delayed_work_timer_fn)
		     1D,  2522 kworker/0:0	queue_delayed_work_on (delayed_work_timer_fn)
		  1029 total events, 583.333 events/sec

	      The output columns are:

	      [1]  a count of the number of events, optionally (since Linux 2.6.23) followed by the letter 'D' if this is a deferrable timer;

	      [2]  the PID of the process that initialized the timer;

	      [3]  the name of the process that initialized the timer;

	      [4]  the function where the timer was initialized; and (in parentheses) the callback function that is associated with the timer.

	      During the Linux 4.11 development cycle, this file  was removed because of security concerns, as it exposes information across namespaces.  Fur‐
	      thermore, it is possible to obtain the same information via in-kernel tracing facilities such as ftrace.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_timer_stats(5)
