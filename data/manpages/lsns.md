LSNS(8)								     System Administration							       LSNS(8)

NAME
       lsns - list namespaces

SYNOPSIS
       lsns [options] namespace

DESCRIPTION
       lsns lists information about all the currently accessible namespaces or about the given namespace. The namespace identifier is an inode number.

       The default output is subject to change. So whenever possible, you should avoid using default outputs in your scripts. Always explicitly define
       expected output mode (--tree or --list) and columns by using the --output option together with a columns list in environments where a stable output is
       required.

       The NSFS column, printed when net is specified for the --type option, is special; it uses multi-line cells. Use the option --nowrap to switch to
       ","-separated single-line representation.

       Note that lsns reads information directly from the /proc filesystem and for non-root users it may return incomplete information. The current /proc
       filesystem may be unshared and affected by a PID namespace (see unshare --mount-proc for more details). lsns is not able to see persistent namespaces
       without processes where the namespace instance is held by a bind mount to /proc/pid/ns/type.

OPTIONS
       -J, --json
	   Use JSON output format.

       -l, --list
	   Use list output format.

       -n, --noheadings
	   Do not print a header line.

       -o, --output list
	   Specify which output columns to print. Use --help to get a list of all supported columns.

	   The default list of columns may be extended if list is specified in the format +list (e.g., lsns -o +PATH).

       --output-all
	   Output all available columns.

       -P, --persistent
	   Display only the namespaces without processes (aka persistent namespaces), created by bind mounting /proc/pid/ns/type files to a filesystem path.

       -p, --task PID
	   Display only the namespaces held by the process with this PID.

       -r, --raw
	   Use the raw output format.

       -t, --type type
	   Display the specified type of namespaces only. The supported types are mnt, net, ipc, user, pid, uts, cgroup and time. This option may be given
	   more than once.

       -u, --notruncate
	   Do not truncate text in columns.

       -W, --nowrap
	   Do not use multi-line text in columns.

       -T, --tree rel
	   Use tree-like output format. If process is given as rel, print process tree(s) in each name space. This is default when --tree is not specified. If
	   parent is given, print tree(s) constructed by the parent/child relationship. If owner is given, print tree(s) constructed by the owner/owned
	   relationship. owner is used as default when rel is omitted.

       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

EXIT STATUS
       The lsns utility exits with one of the following values:

       0
	   Success.

       1
	   General error.

       2
	   An ioctl was unknown to the kernel.

AUTHORS
       Karel Zak <kzak@redhat.com>

SEE ALSO
       nsenter(1), unshare(1), clone(2), namespaces(7), ioctl_ns(2), ip-netns(8)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The lsns command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-11-21								       LSNS(8)
