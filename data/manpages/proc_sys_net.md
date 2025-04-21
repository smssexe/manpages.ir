proc_sys_net(5)							      File Formats Manual						       proc_sys_net(5)

NAME
       /proc/sys/net/ - networking

DESCRIPTION
       /proc/sys/net/
	      This directory contains networking stuff.	 Explanations for some of the files under this directory can be found in tcp(7) and ip(7).

       /proc/sys/net/core/bpf_jit_enable
	      See bpf(2).

       /proc/sys/net/core/somaxconn
	      This file defines a ceiling value for the backlog argument of listen(2); see the listen(2) manual page for details.

SEE ALSO
       proc(5), proc_net(5)

Linux man-pages 6.7							  2023-09-30							       proc_sys_net(5)
