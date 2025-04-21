kvmexit(8)							    System Manager's Manual							    kvmexit(8)

NAME
       kvmexit - Display the exit_reason and its statistics of each vm exit.

SYNOPSIS
       kvmexit [-h] [-p PID [-v VCPU | -a] ] [-t TID | -T 'TID1,TID2'] [duration]

DESCRIPTION
       Considering  virtual  machines' frequent exits can cause performance problems, this tool aims to locate the frequent exited reasons and then find solu‐
       tions to reduce or even avoid the exit, by displaying the detail exit reasons and the counts of each vm exit for all vms running on  one	 physical  ma‐
       chine.

       This tool uses a PERCPU_ARRAY: pcpuArrayA and a percpu_hash: hashA to collaboratively store each kvm exit reason and its count. The reason is there ex‐
       ists  a	rule  when  one	 vcpu exits and re-enters, it tends to continue to run on the same physical cpu as the last cycle, which is also called 'cache
       hit'. Thus we turn to use a PERCPU_ARRAY to record the 'cache hit' situation to speed things up; and for other cases, then use a percpu_hash.

       As RAW_TRACEPOINT_PROBE(kvm_exit) consumes less cpu cycles, when this tool is used, it firstly tries to employ  raw  tracepoints	 in  modules,  and  if
       failes, then fall back to regular tracepoint.

       Limitation: In view of the hardware-assisted virtualization technology of different architectures, currently we only adapt on vmx in intel.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

       This also requires Linux 4.7+ (BPF_PROG_TYPE_TRACEPOINT support).

OPTIONS
       -h     Print usage message.

       -p PID Display process with this PID only, collpase all tids with exit reasons sorted in descending order.

       -v VCPU
	      Display this VCPU only for this PID.

       -a ALLTIDS
	      Display all TIDS for this PID.

       -t TID Display thread with this TID only with exit reasons sorted in descending order.

       -T 'TID1,TID2'
	      Display threads for a union like {395490, 395491}.

       duration
	      Duration of display, after sleeping several seconds.

EXAMPLES
       Display kvm exit reasons and statistics for all threads... Hit Ctrl-C to end:
	      # kvmexit

       Display kvm exit reasons and statistics for all threads after sleeping 6 secs:
	      # kvmexit 6

       Display kvm exit reasons and statistics for PID 1273795 after sleeping 5 secs:
	      # kvmexit -p 1273795 5

       Display kvm exit reasons and statistics for PID 1273795 and its all threads after sleeping 5 secs:
	      # kvmexit -p 1273795 5 -a

       Display kvm exit reasons and statistics for PID 1273795 VCPU 0... Hit Ctrl-C to end:
	      # kvmexit -p 1273795 -v 0

       Display kvm exit reasons and statistics for PID 1273795 VCPU 0 after sleeping 4 secs:
	      # kvmexit -p 1273795 -v 0 4

       Display kvm exit reasons and statistics for TID 1273819 after sleeping 10 secs:
	      # kvmexit -t 1273819 10

       Display kvm exit reasons and statistics for TIDS ['1273820', '1273819']... Hit Ctrl-C to end:
	      # kvmexit -T '1273820,1273819'

OVERHEAD
       This traces the "kvm_exit" kernel function, records the exit reason and calculates its counts. Contrast with filling more vm-exit reason debug entries,
       this tool is more easily and flexibly: the bcc python logic could provide nice kernel aggregation and custom output, the bpf in-kernel percpu_array and
       percpu_cache further improves performance.

       The impact of using this tool on the host should be negligible. While this tool is very efficient, it does affect the guest virtual machine itself, the
       average test results on guest vm are as follows:
		      | cpu cycles
	   no TP      |	  1127
	   regular TP |	  1277 (13% downgrade)
	   RAW TP     |	  1187 (5% downgrade)

       Host: echo 1 > /proc/sys/net/core/bpf_jit_enable

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Fei Li <lifei.shirley@bytedance.com>

USER COMMANDS								  2021-07-08								    kvmexit(8)
