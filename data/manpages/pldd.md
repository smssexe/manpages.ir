pldd(1)								    General Commands Manual							       pldd(1)

NAME
       pldd - display dynamic shared objects linked into a process

SYNOPSIS
       pldd pid
       pldd option

DESCRIPTION
       The  pldd  command displays a list of the dynamic shared objects (DSOs) that are linked into the process with the specified process ID (PID).  The list
       includes the libraries that have been dynamically loaded using dlopen(3).

OPTIONS
       --help
       -?     Display a help message and exit.

       --usage
	      Display a short usage message and exit.

       --version
       -V     Display program version information and exit.

EXIT STATUS
       On success, pldd exits with the status 0.  If the specified process does not exist, the user does not have permission to access its dynamic shared  ob‐
       ject list, or no command-line arguments are supplied, pldd exists with a status of 1.  If given an invalid option, it exits with the status 64.

VERSIONS
       Some other systems have a similar command.

STANDARDS
       None.

HISTORY
       glibc 2.15.

NOTES
       The command

	   lsof -p PID

       also shows output that includes the dynamic shared objects that are linked into a process.

       The  gdb(1)  info shared command also shows the shared libraries being used by a process, so that one can obtain similar output to pldd using a command
       such as the following (to monitor the process with the specified pid):

	   $ gdb -ex "set confirm off" -ex "set height 0" -ex "info shared" \
		   -ex "quit" -p $pid | grep '^0x.*0x'

BUGS
       From glibc 2.19 to glibc 2.29, pldd was broken: it just hung when executed.  This problem was fixed in glibc 2.30, and the fix has been	backported  to
       earlier glibc versions in some distributions.

EXAMPLES
       $ echo $$	       # Display PID of shell
       1143
       $ pldd $$	       # Display DSOs linked into the shell
       1143:   /usr/bin/bash
       linux-vdso.so.1
       /lib64/libtinfo.so.5
       /lib64/libdl.so.2
       /lib64/libc.so.6
       /lib64/ld-linux-x86-64.so.2
       /lib64/libnss_files.so.2

SEE ALSO
       ldd(1), lsof(1), dlopen(3), ld.so(8)

Linux man-pages 6.7							  2023-10-31								       pldd(1)
