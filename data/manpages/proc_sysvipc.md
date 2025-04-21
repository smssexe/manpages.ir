proc_sysvipc(5)							      File Formats Manual						       proc_sysvipc(5)

NAME
       /proc/sysvipc/ - System V IPC

DESCRIPTION
       /proc/sysvipc/
	      Subdirectory  containing	the  pseudo-files  msg,	 sem and shm.  These files list the System V Interprocess Communication (IPC) objects (respec‐
	      tively: message queues, semaphores, and shared memory) that currently exist on the system, providing similar information to that	available  via
	      ipcs(1).	 These	files have headers and are formatted (one IPC object per line) for easy understanding.	sysvipc(7) provides further background
	      on the information shown by these files.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_sysvipc(5)
