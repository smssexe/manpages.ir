proc_pid_oom_score(5)						      File Formats Manual						 proc_pid_oom_score(5)

NAME
       /proc/pid/oom_score - OOM-killer score

DESCRIPTION
       /proc/pid/oom_score (since Linux 2.6.11)
	      This  file displays the current score that the kernel gives to this process for the purpose of selecting a process for the OOM-killer.  A higher
	      score means that the process is more likely to be selected by the OOM-killer.  The basis for this score is the amount  of	 memory	 used  by  the
	      process, with increases (+) or decreases (-) for factors including:

	      •	 whether the process is privileged (-).

	      Before Linux 2.6.36 the following factors were also used in the calculation of oom_score:

	      •	 whether the process creates a lot of children using fork(2) (+);

	      •	 whether the process has been running a long time, or has used a lot of CPU time (-);

	      •	 whether the process has a low nice value (i.e., > 0) (+); and

	      •	 whether the process is making direct hardware access (-).

	      The oom_score also reflects the adjustment specified by the oom_score_adj or oom_adj setting for the process.

SEE ALSO
       proc(5), proc_pid_oom_score_adj(5)

Linux man-pages 6.7							  2023-08-15							 proc_pid_oom_score(5)
