sslsniff(8)							    System Manager's Manual							   sslsniff(8)

NAME
       sslsniff - Print data passed to OpenSSL, GnuTLS or NSS. Uses Linux eBPF/bcc.

SYNOPSIS
       sslsniff [-h] [-p PID] [-u UID] [-x] [-c COMM] [-o] [-g] [-n] [-d] [--hexdump] [--max-buffer-size SIZE] [-l] [--handshake] [--extra-lib EXTRA_LIB]

DESCRIPTION
       sslsniff	 prints	 data  sent to write/send and read/recv functions of OpenSSL, GnuTLS and NSS, allowing us to read plain text content before encryption
       (when writing) and after decryption (when reading).

       This works reading the second parameter of both functions (*buf).

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -p PID Trace only functions in this process PID.

       -u UID Trace only calls made by this UID.

       -x     Show extra fields: UID and TID.

       -c COMM
	      Show only processes that match this COMM exactly.

       -o, --no-openssl
	      Do not trace OpenSSL functions.

       -g, --no-gnutls
	      Do not trace GnuTLS functions.

       -n, --no-nss
	      Do not trace GnuTLS functions.

       --hexdump
	      Show data as hexdump instead of trying to decode it as UTF-8

       --max-buffer-size SIZE
	      Sets maximum buffer size of intercepted data. Longer values would be truncated.  Default value is 8 Kib, maximum possible value is  a  bit  less
	      than 32 Kib.

       -l, --latency
	      Show function latency in ms.

       --handshake
	      Show handshake latency, enabled only if latency option is on.

       --extra-lib EXTRA_LIB
	      Consist  type  of	 the library and library path separated by colon. Supported library types are: openssl, gnutls, nss. Can be specified multiple
	      times.

EXAMPLES
       Print all calls to SSL write/send and read/recv system-wide:
	      # sslsniff

       Print only OpenSSL calls issued by user with UID 1000
	      # sslsniff -u 1000 --no-nss --no-gnutls

       Print SSL handshake event and latency for all traced functions:
	      # sslsniff -l --handshake

       Print only calls to OpenSSL from /some/path/libssl.so
	      sslsniff --no-openssl --no-gnutls --no-nss --extra-lib openssl:/some/path/libssl.so

FIELDS
       FUNC   Which function is being called (write/send or read/recv)

       TIME   Time of the command, in seconds.

       COMM   Entered command.

       PID    Process ID calling SSL.

       LEN    Bytes written or read by SSL functions.

       UID    UID of the process, displayed only if launched with -x.

       TID    Thread ID, displayed only if launched with -x.

       LAT(ms)
	      Function latency in ms.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHORS
       Adrian Lopez and Mark Drayton

SEE ALSO
       trace(8)

USER COMMANDS								  2016-08-16								   sslsniff(8)
