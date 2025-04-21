readahead(8)							    System Manager's Manual							  readahead(8)

NAME
       readahead - Show performance of read-ahead cache

SYNOPSIS
       readahead [-d DURATION]

DESCRIPTION
       The  tool  shows	 the  performance of read-ahead caching on the system under a given load to investigate any caching issues. It shows a count of unused
       pages in the cache and also prints a histogram showing how long they have remained there.

       This tool traces the __do_page_cache_readahead() kernel function to track entry and exit in the	readahead  mechanism  in  the  kernel  and  then  uses
       __page_cache_alloc() and mark_page_accessed() functions to calculate the age of the page in the cache as well as see how many are left unaccessed.

       Since this uses BPF, only the root user can use this tool.

   NOTE ON KPROBES USAGE
       Since  the  tool uses Kprobes, depending on your linux kernel's compilation, these functions may be inlined and hence not available for Kprobes. To see
       whether you have the functions available, check vmlinux source and binary to confirm  whether  inlining	is  happening  or  not.	 You  can  also	 check
       /proc/kallsyms on the host and verify if the target functions are present there before using this.

REQUIREMENTS
       CONFIG_BPF, bcc

OPTIONS
       -h Print usage message

       -d DURATION
	      Trace the read-ahead caching system for DURATION seconds

EXAMPLES
       Trace for 30 seconds and show  histogram of page age (ms) in read-ahead cache along with unused page count:
	      # readahead -d 30

OVERHEAD
       The  kernel  functions instrumented by this program could be high-frequency depending on the profile of the application (for example sequential IO). We
       advise the users to measure and monitor the overhead before leaving this turned on in production environments.

SOURCE
       This originated as a bpftrace tool from the book "BPF Performance Tools", published by Addison Wesley (2019):

	      http://www.brendangregg.com/bpf-performance-tools-book.html

       See the book for more documentation on this tool.

       This version is in the BCC repository:

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Suchakra Sharma

SEE ALSO
       readahead(2), madvise(2)

USER COMMANDS								  2020-08-20								  readahead(8)
