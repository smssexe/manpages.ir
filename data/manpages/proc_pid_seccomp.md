proc_pid_seccomp(5)						      File Formats Manual						   proc_pid_seccomp(5)

NAME
       /proc/pid/seccomp - secure computing mode

DESCRIPTION
       /proc/pid/seccomp (Linux 2.6.12 to Linux 2.6.22)
	      This  file  can be used to read and change the process's secure computing (seccomp) mode setting.	 It contains the value 0 if the process is not
	      in seccomp mode, and 1 if the process is in strict seccomp mode (see seccomp(2)).	 Writing 1 to this file places	the  process  irreversibly  in
	      strict seccomp mode.  (Further attempts to write to the file fail with the EPERM error.)

	      In  Linux	 2.6.23, this file went away, to be replaced by the prctl(2) PR_GET_SECCOMP and PR_SET_SECCOMP operations (and later by seccomp(2) and
	      the Seccomp field in /proc/pid/status).

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15							   proc_pid_seccomp(5)
