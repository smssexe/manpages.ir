sslsnoop.bt(8)							    System Manager's Manual							sslsnoop.bt(8)

NAME
       sslsnoop.bt - Show SSL/TLS handshake events. Uses bpftrace/eBPF.

SYNOPSIS
       sslsnoop.bt

DESCRIPTION
       sslsnoop traces OpenSSL handshake functions, and shows latency and return value. This can be used to analyze SSL/TLS performance.

       This tool works by dynamic tracing the uprobes in OpenSSL and related crypto libs, and may need updating to match future changes to these functions.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bpftrace.

EXAMPLES
       Trace SSL/TLS handshake events, printing per-line summaries:
	      # sslsnoop.bt

FIELDS
       TIME(us)
	      Time of the call completion, in microseconds since program start.

       TID    Thread ID.

       COMM   Process name.

       LAT(us)
	      Latency of the call, in microseconds.

       RET    Return value of the call.

       FUNC   Function name.

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
       biosnoop.bt(8)

USER COMMANDS								  2021-12-28								sslsnoop.bt(8)
