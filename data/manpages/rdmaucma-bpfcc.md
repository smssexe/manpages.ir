rdmaucma(8)							    System Manager's Manual							   rdmaucma(8)

NAME
       rdmaucma - Trace RDMA Userspace Connection Manager Access Event. For Linux, uses BCC, eBPF.

SYNOPSIS
       rdmaucma [-h] [-D]

DESCRIPTION
       This program traces RDMA UCMA(Userspace Connection Manager Access) events, This can be useful to analyze issues on RDMA CM.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -D     Show debug infomation of bpf text.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       zhenwei pi

SEE ALSO
       rdma(8)

USER COMMANDS								  2023-05-29								   rdmaucma(8)
