WATCHGNUPG(1)							     GNU Privacy Guard 2.4							 WATCHGNUPG(1)

NAME
       watchgnupg - Read and print logs from a socket

SYNOPSIS
       watchgnupg [--force] [--verbose] socketname

DESCRIPTION
       Most  of the main utilities are able to write their log files to a Unix Domain socket if configured that way.  watchgnupg is a simple listener for such
       a socket.  It ameliorates the output with a time stamp and makes sure that long lines are not interspersed with log output from other utilities.	  This
       tool is not available for Windows.

       watchgnupg is commonly invoked as

	 watchgnupg

       which is a shorthand for

	 watchgnupg --force $(gpgconf --list-dirs socketdir)/S.log

       To watch GnuPG running with a different home directory, use

	 watchgnupg --homedir DIR

OPTIONS
       watchgnupg understands these options:

       --force
	      Delete an already existing socket file.  This option is implicitly used if no socket name has been given on the command line.

       --homedir DIR
	      If  no  socket  name is given on the command line, pass DIR to gpgconf so that the socket for a GnuPG running with DIR has its home directory is
	      used.  Note that the environment variable GNUPGHOME is ignored by watchgnupg.

       --tcp n
	      Instead of reading from a local socket, listen for connects on TCP port n.  A Unix domain socket can  optionally	also  be  given	 as  a	second
	      source.  This option does not use a default socket name.

       --time-only
	      Do not print the date part of the timestamp.

       --verbose
	      Enable extra informational output.

       --version
	      Print version of the program and exit.

       --help Display a brief help page and exit.

EXAMPLES
	 $ watchgnupg --time-only

       This  waits  for	 connections on the local socket (e.g. ‘/var/run/user/1234/gnupg/S.log’) and shows all log entries.  To make this work the option log-
       file needs to be used with all modules which logs are to be shown.  The suggested entry for the configuration files is:

	 log-file socket://

       If the default socket as given above and returned by "echo $(gpgconf --list-dirs socketdir)/S.log" is not desired an arbitrary socket name can be spec‐
       ified, for example ‘socket:///home/foo/bar/mysocket’.  For debugging purposes it is also possible to do remote logging.	Take care if you use this fea‐
       ture because the information is send in the clear over the network.  Use this syntax in the conf files:

	 log-file tcp://192.168.1.1:4711

       You may use any port and not just 4711 as shown above; only IP addresses are supported (v4 and v6) and no host names.  You  need	 to  start  watchgnupg
       with  the  tcp  option.	Note that under Windows the registry entry HKCU\Software\GNU\GnuPG:DefaultLogFile can be used to change the default log output
       from stderr to whatever is given by that entry.	However the only useful entry is a TCP name for remote debugging.

SEE ALSO
       gpg(1), gpgsm(1), gpg-agent(1), scdaemon(1)

       The full documentation for this tool is maintained as a Texinfo manual.	If GnuPG and the info program are properly installed at your site, the command

	 info gnupg

       should give you access to the complete manual including a menu structure and an index.

GnuPG 2.4.4								  2024-01-25								 WATCHGNUPG(1)
