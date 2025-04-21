ssllatency.bt(8)						    System Manager's Manual						      ssllatency.bt(8)

NAME
       ssllatency.bt - Show SSL/TLS handshake latency histogram. Uses bpftrace/eBPF.

SYNOPSIS
       ssllatency.bt

DESCRIPTION
       ssllatency  shows  latency  distribution	 for  OpenSSL handshake functions. This is useful for performance analysis with different crypto cipher suite,
       async SSL acceleration by CPU or offload device, etc.

       This tool works by dynamic tracing the uprobes in OpenSSL and related crypto libs, and may need updating to match future changes to these functions.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bpftrace.

EXAMPLES
       Trace SSL/TLS handshake latency, and print a histogram on Ctrl-C:
	      # ssllatency.bt

FIELDS
       0th    A function name is shown in "@hist[...]" followed by latency histogram and "@stat[...]" followed by total call count, average, total latency  in
	      microseconds. Non-zero failed calls are traced separately (in "@histF[]" and "@statF[]") for some functions.

       1st, 2nd
	      This is a range of latency, in microseconds (shown in "[...)" set notation).

       3rd    A column showing the count of operations in this range.

       4th    This is an ASCII histogram representing the count column.

OVERHEAD
       SSL/TLS	handshake  usually  contains  network latency and the traced crypto functions are CPU intensive tasks, so call frequency should be low and the
       overhead of this tool is expected to be negligible.

SOURCE
       This is from bpftrace.

	      https://github.com/iovisor/bpftrace

       Also look in the bpftrace distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

       There is a bcc tool sslsniff that can show SSL/TLS handshake event latency before sniffing the plaintext in SSL_read/write. This tool provides more de‐
       tailed crypto latency distribution during the handshake event.

	      https://github.com/iovisor/bcc

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Tao Xu

SEE ALSO
       sslsnoop.bt(8)

USER COMMANDS								  2021-12-28							      ssllatency.bt(8)
