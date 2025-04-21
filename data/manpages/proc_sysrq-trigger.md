proc_sysrq-trigger(5)						      File Formats Manual						 proc_sysrq-trigger(5)

NAME
       /proc/sysrq-trigger - SysRq function

DESCRIPTION
       /proc/sysrq-trigger (since Linux 2.4.21)
	      Writing  a  character  to	 this  file  triggers  the  same SysRq function as typing ALT-SysRq-<character> (see the description of /proc/sys/ker‐
	      nel/sysrq).  This file is	 normally  writable  only  by  root.   For  further  details  see  the	Linux  kernel  source  file  Documentation/ad‐
	      min-guide/sysrq.rst (or Documentation/sysrq.txt before Linux 4.10).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							 proc_sysrq-trigger(5)
