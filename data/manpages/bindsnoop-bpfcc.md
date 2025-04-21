bindsnoop(8)																	  bindsnoop(8)

NAME
       bindsnoop - Trace bind() system calls.

SYNOPSIS
       bindsnoop [-h] [-w] [-t] [-p PID] [-P PORT] [-E] [-U] [-u UID] [--count] [--cgroupmap MAP] [--mntnsmap MNTNSMAP]

DESCRIPTION
       bindsnoop reports socket options set before the bind call that would impact this system call behavior.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS:
	      Show help message and exit:

	      -h, --help

	      Include timestamp on output:

	      -t, --timestamp

	      Wider columns (fit IPv6):

	      -w, --wide

	      Trace this PID only:

	      -p PID, --pid PID

	      Comma-separated list of ports to trace:

	      -P PORT, --port PORT

	      Trace cgroups in this BPF map:

	      --cgroupmap MAP

	      Trace mount namespaces in this BPF map:

	      --mntnsmap MNTNSMAP

	      Include errors in the output:

	      -E, --errors

	      Include UID on output:

	      -U, --print-uid

	      Trace this UID only:

	      -u UID, --uid UID

	      Count binds per src ip and port:

	      --count

EXAMPLES:
	      Trace all IPv4 and IPv6 bind()s

	      bindsnoop

	      Include timestamps

	      bindsnoop -t

	      Trace PID 181

	      bindsnoop -p 181

	      Trace port 80

	      bindsnoop -P 80

	      Trace port 80 and 81

	      bindsnoop -P 80,81

	      Include UID

	      bindsnoop -U

	      Trace UID 1000

	      bindsnoop -u 1000

	      Report bind errors

	      bindsnoop -E

	      Count bind per src ip

	      bindsnoop --count

       Trace IPv4 and IPv6 bind system calls and report socket options that would impact bind call behavior:

	      SOL_IP IP_FREEBIND	      F....

	      SOL_IP IP_TRANSPARENT	      .T...

	      SOL_IP IP_BIND_ADDRESS_NO_PORT  ..N..

	      SOL_SOCKET SO_REUSEADDR	      ...R.

	      SOL_SOCKET SO_REUSEPORT	      ....r

	      SO_BINDTODEVICE interface is reported as "IF" index

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Pavel Dubovitsky

SEE ALSO
       tcpaccept(8)

								       12 February 2020								  bindsnoop(8)
