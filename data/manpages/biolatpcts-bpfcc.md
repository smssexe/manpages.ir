biolatpcts(8)							    System Manager's Manual							 biolatpcts(8)

NAME
       biolatpcts - Monitor IO latency distribution of a block device.

SYNOPSIS
       biolatpcts [-h] [-i INTERVAL] [-w which] [-p PCT,...] [-j] [-v] DEV

DESCRIPTION
       biolatpcts traces block device I/O (disk I/O) of the specified device, and calculates and prints the completion latency distribution percentiles per IO
       type periodically. Example:

	# biolatpcts /dev/nvme0n1
	nvme0n1	   p1	 p5   p10   p16	  p25	p50   p75   p84	  p90	p95   p99  p100
	read	 95us 175us 305us 515us 895us 985us 995us 1.5ms 2.5ms 3.5ms 4.5ms  10ms
	write	  5us	5us   5us  15us	 25us 135us 765us 855us 885us 895us 965us 1.5ms
	discard	  5us	5us   5us   5us 135us 145us 165us 205us 385us 875us 1.5ms 2.5ms
	flush	  5us	5us   5us   5us	  5us	5us   5us   5us	  5us 1.5ms 4.5ms 5.5ms
	[...]

       biolatpcts prints a number of pre-set latency percentiles in tabular form every three seconds. The interval can be changed with the -i option.

       The latency is measured between issue to the device and completion. The starting point can be changed with the -w option.

       Any number of percentiles can be specified using the -p option. The input percentile string is used verbatim in the output to ease machine consumption.

       -j option enables json output. The result for each interval is printed on a single line.

       This  tool  works by tracing blk_account_io_done() with kprobe and bucketing the completion latencies into percpu arrays. It may need updating to match
       the changes to the function.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF, CONFIG_KPROBES and bcc.

OPTIONS
       -h Print usage message.

       -i INTERVAL, --interval INTERVAL
	      Report interval. (default: 3)

       -w {from-rq-alloc,after-rq-alloc,on-device}, --which {from-rq-alloc,after-rq-alloc,on-device}
	      Which latency to measure. (default: on-device)

       -p PCT,..., --pcts PCT,...
	      Percentiles to calculate. (default: 1,5,10,16,25,50,75,84,90,95,99,100)

       -j, --json
	      Output in json.

       -v, --verbose
	      Enable debug output.

       DEV    Target block device. /dev/DEVNAME, DEVNAME or MAJ:MIN.

EXAMPLES
       Print sda's I/O latency percentiles every second
	      # biolatpcts -i 1 sda

       Print nvme0n1's all-9 I/O latency percentiles in json every second
	      # biolatpcts -p 99,99.9,99.99,99.999 -j -i 1 /dev/nvme0n1

OVERHEAD
       This traces kernel functions and maintains in-kernel per-cpu latency buckets, which are asynchronously copied to user-space. This method is very	 effi‐
       cient, and the overhead for most storage I/O rates should be negligible. If you have an extremely high IOPS storage device, test and quantify the over‐
       head before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Tejun Heo

SEE ALSO
       biolatency(8), biosnoop(8)

USER COMMANDS								  2020-04-17								 biolatpcts(8)
