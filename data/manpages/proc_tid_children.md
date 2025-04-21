proc_tid_children(5)						      File Formats Manual						  proc_tid_children(5)

NAME
       /proc/tid/children - child tasks

DESCRIPTION
       /proc/tid/children (since Linux 3.5)
	      A space-separated list of child tasks of this task.  Each child task is represented by its TID.

	      This  option  is	intended  for  use  by the checkpoint-restore (CRIU) system, and reliably provides a list of children only if all of the child
	      processes are stopped or frozen.	It does not work properly if children of the target task exit while the file is being read!  Exiting  children
	      may cause non-exiting children to be omitted from the list.  This makes this interface even more unreliable than classic PID-based approaches if
	      the inspected task and its children aren't frozen, and most code should probably not use this interface.

	      Until  Linux  4.2,  the presence of this file was governed by the CONFIG_CHECKPOINT_RESTORE kernel configuration option.	Since Linux 4.2, it is
	      governed by the CONFIG_PROC_CHILDREN option.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							  proc_tid_children(5)
