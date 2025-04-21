CTRLALTDEL(8)							     System Administration							 CTRLALTDEL(8)

NAME
       ctrlaltdel - set the function of the Ctrl-Alt-Del combination

SYNOPSIS
       ctrlaltdel hard|soft

DESCRIPTION
       Based on examination of the linux/kernel/reboot.c code, it is clear that there are two supported functions that the <Ctrl-Alt-Del> sequence can
       perform.

       hard
	   Immediately reboot the computer without calling sync(2) and without any other preparation. This is the default.

       soft
	   Make the kernel send the SIGINT (interrupt) signal to the init process (this is always the process with PID 1). If this option is used, the init(8)
	   program must support this feature. Since there are now several init(8) programs in the Linux community, please consult the documentation for the
	   version that you are currently using.

       When the command is run without any argument, it will display the current setting.

       The function of ctrlaltdel is usually set in the /etc/rc.local file.

OPTIONS
       -h, --help
	   Display help text and exit.

       -V, --version
	   Print version and exit.

FILES
       /etc/rc.local

AUTHORS
       Peter Orbaek <poe@daimi.aau.dk>

SEE ALSO
       init(8), systemd(1)

REPORTING BUGS
       For bug reports, use the issue tracker at https://github.com/util-linux/util-linux/issues.

AVAILABILITY
       The ctrlaltdel command is part of the util-linux package which can be downloaded from Linux Kernel Archive
       <https://www.kernel.org/pub/linux/utils/util-linux/>.

util-linux 2.39.3							  2023-10-23								 CTRLALTDEL(8)
