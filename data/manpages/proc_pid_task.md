proc_pid_task(5)						      File Formats Manual						      proc_pid_task(5)

NAME
       /proc/pid/task/, /proc/tid/, /proc/thread-self/ - thread information

DESCRIPTION
       /proc/pid/task/ (since Linux 2.6.0)
	      This  is	a  directory  that contains one subdirectory for each thread in the process.  The name of each subdirectory is the numerical thread ID
	      (tid) of the thread (see gettid(2)).

	      Within each of these subdirectories, there is a set of files with the same names and contents as under the /proc/pid directories.	  For  attrib‐
	      utes that are shared by all threads, the contents for each of the files under the task/tid subdirectories will be the same as in the correspond‐
	      ing  file	 in  the  parent  /proc/pid directory (e.g., in a multithreaded process, all of the task/tid/cwd files will have the same value as the
	      /proc/pid/cwd file in the parent directory, since all of the threads in a process share a working directory).  For attributes that are  distinct
	      for each thread, the corresponding files under task/tid may have different values (e.g., various fields in each of the task/tid/status files may
	      be different for each thread), or they might not exist in /proc/pid at all.

	      In  a multithreaded process, the contents of the /proc/pid/task directory are not available if the main thread has already terminated (typically
	      by calling pthread_exit(3)).

       /proc/tid/
	      There  is a numerical subdirectory for each running thread that is not a thread group leader (i.e., a thread whose thread ID is not the same  as
	      its process ID); the subdirectory is named by the thread ID.  Each one of these subdirectories contains files and subdirectories exposing infor‐
	      mation about the thread with the thread ID tid.  The contents of these directories are the same as the corresponding /proc/pid/task/tid directo‐
	      ries.

	      The /proc/tid subdirectories are not visible when iterating through /proc with getdents(2) (and thus are not visible when one uses ls(1) to view
	      the  contents of /proc).	However, the pathnames of these directories are visible to (i.e., usable as arguments in) system calls that operate on
	      pathnames.

       /proc/thread-self/ (since Linux 3.17)
	      This directory refers to the thread accessing the /proc filesystem, and is identical to the /proc/self/task/tid directory named by  the  process
	      thread ID (tid) of the same thread.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							      proc_pid_task(5)
