sofdsnoop(8)							    System Manager's Manual							  sofdsnoop(8)

NAME
       sofdsnoop - Trace FDs passed through unix sockets. Uses Linux eBPF/bcc.

SYNOPSIS
       sofdsnoop [-h] [-T] [-p PID] [-t TID] [-n NAME] [-d DURATION]

DESCRIPTION
       sofdsnoop traces FDs passed through unix sockets

       Every  file  descriptor	that  is  passed  via unix sockets os displayed on separate line together with process info (TID/COMM columns), ACTION details
       (SEND/RECV), file descriptor number (FD) and its translation to file if available (NAME).

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -T     Include a timestamp column.

       -p PID Trace this process ID only (filtered in-kernel).

       -t TID Trace this thread ID only (filtered in-kernel).

       -d DURATION
	      Total duration of trace in seconds.

       -n NAME
	      Only print command lines matching this command name (regex)

EXAMPLES
       Trace all sockets:
	      # sofdsnoop

       Trace all sockets, and include timestamps:
	      # sofdsnoop -T

       Only trace sockets where the process contains "server":
	      # sofdsnoop -n server

FIELDS
       TIME(s)
	      Time of SEDN/RECV actions, in seconds.

       ACTION Operation on the fd SEND/RECV.

       TID    Process TID

       COMM   Parent process/command name.

       SOCKET The socket carrier.

       FD     file descriptor number

       NAME   file name for SEND lines

SOURCE
       This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Jiri Olsa

SEE ALSO
       opensnoop(1)

USER COMMANDS								  2018-11-08								  sofdsnoop(8)
