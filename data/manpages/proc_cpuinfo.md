proc_cpuinfo(5)							      File Formats Manual						       proc_cpuinfo(5)

NAME
       /proc/cpuinfo - CPU and system architecture information

DESCRIPTION
       /proc/cpuinfo
	      This  is	a collection of CPU and system architecture dependent items, for each supported architecture a different list.	Two common entries are
	      processor which gives CPU number and bogomips; a system constant that is calculated during kernel initialization.	 SMP machines have information
	      for each CPU.  The lscpu(1) command gathers its information from this file.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							       proc_cpuinfo(5)
