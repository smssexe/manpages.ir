tcpcong(8)							    System Manager's Manual							    tcpcong(8)

NAME
       tcpcong - Measure tcp congestion state duration. Uses Linux eBPF/bcc.

SYNOPSIS
       tcpcong [-h] [-T] [-L] [-R] [-u] [-d] [interval] [outputs]

DESCRIPTION
       this  tool measures tcp sockets congestion control status duration, and prints a summary of tcp congestion state durations along with the number of to‐
       tal state changes.

       It uses dynamic tracing of kernel tcp congestion control status updating functions,  and will need to be updated to match kernel changes.

       The traced functions are only called when there is congestion state update, and therefore have low overhead. we also use BPF map to store  traced  data
       to reduce overhead. See the OVERHEAD section for more details.  Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include a timestamp column.

       -L     Specify local tcp port range.

       -R     Specify remote tcp port range.

       -u     Output in microseconds.

       -d     Show congestion status duration distribution as histograms.

EXAMPLES
       Show all tcp sockets congestion status duration until Ctrl-C:
	      # tcpcongestdura

       Show all tcp sockets congestion status duration every 1 second and 10 times:
	      # tcpcong 1 10

       Show only local port 3000-3006 congestion status duration every 1 second:
	      # tcpcong -L 3000-3006 1

       Show only remote port 5000-5005 congestion status duration every 1 second:
	      # tcpcong -R 5000-5005 1

       Show 1 second summaries, printed in microseconds, with timestamps:
	      # tcpcong -uT 1

       Show all tcp sockets congestion status duration as histograms:
	      # tcpcong -d

FIELDS
       LAddrPort
	      local ip address and tcp socket port.

       RAddrPort
	      remote ip address and tcp socket port.

       Open_us
	      Total duration in open status for microseconds.

       Dod_us Total duration in disorder status for microseconds.

       Rcov_us
	      Total duration in recovery status for microseconds.

       Cwr_us Total duration in cwr status for microseconds.

       Los_us Total duration in loss status for microseconds.

       Open_ms
	      Total duration in open status for milliseconds.

       Dod_ms Total duration in disorder status for milliseconds.

       Rcov_ms
	      Total duration in recovery status for milliseconds.

       Cwr_ms Total duration in cwr status for milliseconds.

       Loss_ms
	      Total duration in loss status for milliseconds.

       Chgs   Total number of status change.

       usecs  Range of microseconds for this bucket.

       msecs  Range of milliseconds for this bucket.

       count  Number of congestion status in this time range.

       distribution
	      ASCII representation of the distribution (the count column).

OVERHEAD
       This traces the kernel tcp congestion status change functions.  As called rate per second of these functions per socket is low(<10000), the overhead is
       also expected to be negligible. If you have an application that will create thousands of tcp connections, then test and understand overhead before use.

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       jacky gan

SEE ALSO
       tcpretrans(8), tcpconnect(8), tcptop(8), tcpdrop(8)

USER COMMANDS								  2022-01-27								    tcpcong(8)
