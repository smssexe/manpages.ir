SUDO_SENDLOG(8)							    System Manager's Manual						       SUDO_SENDLOG(8)

NAME
       sudo_sendlog — send sudo I/O log to log server

SYNOPSIS
       sudo_sendlog [-AnV] [-b ca_bundle] [-c cert_file] [-h host] [-i iolog-id] [-k key_file] [-p port] [-r restart-point] [-R reject-reason] [-s stop-point]
		    [-t number] path

DESCRIPTION
       sudo_sendlog can be used to send the existing sudoers I/O log path to a remote log server such as sudo_logsrvd(8) for central storage.

       The options are as follows:

       -A, --accept-only
	       Only  send the accept event, not the I/O associated with the log.  This can be used to test the logging of accept events without any associated
	       I/O.

       -b, --ca-bundle
	       The path to a certificate authority bundle file, in PEM format, to use instead of the system's default certificate authority database when  au‐
	       thenticating the log server.  The default is to use the system's default certificate authority database.

       -c, --cert
	       The path to the client's certificate file in PEM format.	 This setting is required when the connection to the remote log server is secured with
	       TLS.

       --help  Display a short help message to the standard output and exit.

       -h, --host
	       Connect to the specified host instead of localhost.

       -i, --iolog-id
	       Use  the	 specified  iolog-id when restarting a log transfer.  The iolog-id is reported by the server when it creates the remote I/O log.  This
	       option may only be used in conjunction with the -r option.

       -k, --key
	       The path to the client's private key file in PEM format.	 This setting is required when the connection to the remote log server is secured with
	       TLS.

       -n, --no-verify
	       If specified, the server's certificate will not be verified during the TLS handshake.  By default, sudo_sendlog verifies that the server's cer‐
	       tificate is valid and that it contains either the server's host name or its IP address.	This setting is only supported when the connection  to
	       the remote log server is secured with TLS.

       -p, --port
	       Use the specified network port when connecting to the log server instead of the default, port 30344.

       -r, --restart
	       Restart an interrupted connection to the log server.  The specified restart-point is used to tell the server the point in time at which to con‐
	       tinue the log.  The restart-point is specified in the form “seconds,nanoseconds” and is usually the last commit point received from the server.
	       The -i option must also be specified when restarting a transfer.

       -R, --reject
	       Send  a reject event for the command using the specified reject-reason, even though it was actually accepted locally.  This can be used to test
	       the logging of reject events; no I/O will be sent.

       -s, --stop-after
	       Stop sending log records and close the connection when stop-point is reached.  This can be used for testing purposes to send a partial I/O  log
	       to  the	server.	  Partial  logs	 can  be  restarted  using  the	 -r  option.   The  stop-point	is  an	elapsed	 time  specified  in  the form
	       “seconds,nanoseconds”.

       -t, --test
	       Open number simultaneous connections to the log server and send the specified I/O log file on each one.	This option is useful for  performance
	       testing.

       -V, --version
	       Print the sudo_sendlog version and exit.

   Debugging sendlog
       sudo_sendlog supports a flexible debugging framework that is configured via Debug lines in the sudo.conf(5) file.

       For more information on configuring sudo.conf(5), refer to its manual.

FILES
       /etc/sudo.conf		 Sudo front-end configuration

SEE ALSO
       sudo.conf(5), sudo(8), sudo_logsrvd(8)

AUTHORS
       Many people have worked on sudo over the years; this version consists of code written primarily by:

	     Todd C. Miller

       See  the	 CONTRIBUTORS.md file in the sudo distribution (https://www.sudo.ws/about/contributors/) for an exhaustive list of people who have contributed
       to sudo.

BUGS
       If you believe you have found a bug in sudo_sendlog, you can submit a bug report at https://bugzilla.sudo.ws/

SUPPORT
       Limited free support is available via the sudo-users mailing list, see  https://www.sudo.ws/mailman/listinfo/sudo-users	to  subscribe  or  search  the
       archives.

DISCLAIMER
       sudo_sendlog  is	 provided  “AS IS” and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and
       fitness for a particular purpose are disclaimed.	 See the LICENSE.md file distributed with sudo or https://www.sudo.ws/about/license/ for complete  de‐
       tails.

Sudo 1.9.15p5							       January 16, 2023							       SUDO_SENDLOG(8)
