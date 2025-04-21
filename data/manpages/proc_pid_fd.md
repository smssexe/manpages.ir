proc_pid_fd(5)							      File Formats Manual							proc_pid_fd(5)

NAME
       /proc/pid/fd/ - file descriptors

DESCRIPTION
       /proc/pid/fd/
	      This is a subdirectory containing one entry for each file which the process has open, named by its file descriptor, and which is a symbolic link
	      to the actual file.  Thus, 0 is standard input, 1 standard output, 2 standard error, and so on.

	      For  file	 descriptors  for  pipes and sockets, the entries will be symbolic links whose content is the file type with the inode.	 A readlink(2)
	      call on this file returns a string in the format:

		  type:[inode]

	      For example, socket:[2248868] will be a socket and its inode is 2248868.	For sockets, that inode can be used to find more information in one of
	      the files under /proc/net/.

	      For file descriptors that have no corresponding inode (e.g., file descriptors produced by bpf(2), epoll_create(2), eventfd(2),  inotify_init(2),
	      perf_event_open(2), signalfd(2), timerfd_create(2), and userfaultfd(2)), the entry will be a symbolic link with contents of the form

		  anon_inode:file-type

	      In many cases (but not all), the file-type is surrounded by square brackets.

	      For example, an epoll file descriptor will have a symbolic link whose content is the string anon_inode:[eventpoll].

	      In  a  multithreaded  process,  the contents of this directory are not available if the main thread has already terminated (typically by calling
	      pthread_exit(3)).

	      Programs that take a filename as a command-line argument, but don't take input from standard input if no argument is supplied, and programs that
	      write to a file named as a command-line argument, but don't send their output to standard output if no argument is supplied, can nevertheless be
	      made to use standard input or standard output by using /proc/pid/fd files as command-line arguments.  For example, assuming that -i is the  flag
	      designating an input file and -o is the flag designating an output file:

		  $ foobar -i /proc/self/fd/0 -o /proc/self/fd/1 ...

	      and you have a working filter.

	      /proc/self/fd/N is approximately the same as /dev/fd/N in some UNIX and UNIX-like systems.  Most Linux MAKEDEV scripts symbolically link /dev/fd
	      to /proc/self/fd, in fact.

	      Most systems provide symbolic links /dev/stdin, /dev/stdout, and /dev/stderr, which respectively link to the files 0, 1, and 2 in /proc/self/fd.
	      Thus the example command above could be written as:

		  $ foobar -i /dev/stdin -o /dev/stdout ...

	      Permission  to  dereference  or read (readlink(2)) the symbolic links in this directory is governed by a ptrace access mode PTRACE_MODE_READ_FS‐
	      CREDS check; see ptrace(2).

	      Note that for file descriptors referring to inodes (pipes and sockets, see above), those inodes still have permission bits and ownership	infor‐
	      mation distinct from those of the /proc/pid/fd entry, and that the owner may differ from the user and group IDs of the process.  An unprivileged
	      process may lack permissions to open them, as in this example:

		  $ echo test | sudo -u nobody cat
		  test
		  $ echo test | sudo -u nobody cat /proc/self/fd/0
		  cat: /proc/self/fd/0: Permission denied

	      File  descriptor	0 refers to the pipe created by the shell and owned by that shell's user, which is not nobody, so cat does not have permission
	      to create a new file descriptor to read from that inode, even though it can still read from its existing file descriptor 0.

SEE ALSO
       proc(5)

Linux man-pages 6.7							  2023-08-15								proc_pid_fd(5)
