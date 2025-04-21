filegone(8)							    System Manager's Manual							   filegone(8)

NAME
       filegone - Trace why file gone (deleted or renamed). Uses Linux eBPF/bcc.

SYNOPSIS
       filegone [-h] [-p PID]

DESCRIPTION
       This traces why file gone/vanished, providing information on who deleted or renamed the file.

       This works by tracing the kernel vfs_unlink() , vfs_rmdir() , vfs_rename functions.

       Since this uses BPF, only the root user can use this tool.

REQUIREMENTS
       CONFIG_BPF and bcc.

OPTIONS
       -h     Print usage message.

       -p PID Trace this process ID only (filtered in-kernel).

EXAMPLES
       Trace all file gone events
	      # filegone

       Trace file gone events caused by PID 181:
	      # filegone -p 181

FIELDS
       TIME   Time of the event.

       PID    Process ID that renamed/deleted the file.

       COMM   Process name for the PID.

       ACTION action on file: 'DELETE' or 'RENAME'

       FILE   Filename.

OVERHEAD
       This  traces  the  kernel VFS file rename and delete functions and prints output for each event. As the rate of this is generally expected to be low (<
       1000/s), the overhead is also expected to be negligible.	 This is from bcc.

	      https://github.com/iovisor/bcc

       Also look in the bcc distribution for a companion _examples.txt file containing example usage, output, and commentary for this tool.

OS
       Linux

STABILITY
       Unstable - in development.

AUTHOR
       Curu Wong

SEE ALSO
       filelife(8)

USER COMMANDS								  2022-11-18								   filegone(8)
