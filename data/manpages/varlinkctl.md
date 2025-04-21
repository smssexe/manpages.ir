VARLINKCTL(1)								  varlinkctl								 VARLINKCTL(1)

NAME
       varlinkctl - Introspect with and invoke Varlink services

SYNOPSIS

       varlinkctl [OPTIONS...] info ADDRESS

       varlinkctl [OPTIONS...] list-interfaces ADDRESS

       varlinkctl [OPTIONS...] introspect ADDRESS INTERFACE

       varlinkctl [OPTIONS...] call ADDRESS METHOD [PARAMETERS]

       varlinkctl [OPTIONS...] validate-idl [FILE]

DESCRIPTION
       varlinkctl may be used to introspect and invoke Varlink[1] services.

       Services are referenced by one of the following:

       •   A Varlink service reference starting with the "unix:" string, followed by an absolute AF_UNIX path, or by "@" and an arbitrary string (the latter
	   for referencing sockets in the abstract namespace).

       •   A Varlink service reference starting with the "exec:" string, followed by an absolute path of a binary to execute.

       For convenience these two simpler (redundant) service address syntaxes are also supported:

       •   A file system path to an AF_UNIX socket, either absolute (i.e. begins with "/") or relative (in which case it must begin with "./").

       •   A file system path to an executable, either absolute or relative (as above, must begin with "/", resp.  "./").

COMMANDS
       The following commands are understood:

       info ADDRESS
	   Show brief information about the specified service, including vendor name and list of implemented interfaces. Expects a service address in the
	   formats described above.

	   Added in version 255.

       list-interfaces ADDRESS
	   Show list of interfaces implemented by the specified service. Expects a service address in the formats described above.

	   Added in version 255.

       introspect ADDRESS INTERFACE
	   Show interface definition of the specified interface provided by the specified service. Expects a service address in the formats described above
	   and a Varlink interface name.

	   Added in version 255.

       call ADDRESS METHOD [ARGUMENTS]
	   Call the specified method of the specified service. Expects a service address in the format described above, a fully qualified Varlink method name,
	   and a JSON arguments object. If the arguments object is not specified, it is read from STDIN instead. To pass an empty list of parameters, specify
	   the empty object "{}".

	   The reply parameters are written as JSON object to STDOUT.

	   Added in version 255.

       validate-idl [FILE]
	   Reads a Varlink interface definition file, parses and validates it, then outputs it with syntax highlighting. This checks for syntax and internal
	   consistency of the interface. Expects a file name to read the interface definition from. If omitted reads the interface definition from STDIN.

	   Added in version 255.

       help
	   Show command syntax help.

	   Added in version 255.

OPTIONS
       The following options are understood:

       --more
	   When used with call: expect multiple method replies. If this flag is set the method call is sent with the more flag set, which tells the service to
	   generate multiple replies, if needed. The command remains running until the service sends a reply message that indicates it is the last in the
	   series. This flag should be set only for method calls that support this mechanism.

	   If this mode is enabled output is automatically switched to JSON-SEQ mode, so that individual reply objects can be easily discerned.

	   Added in version 255.

       --oneway
	   When used with call: do not expect a method reply. If this flag is set the method call is sent with the oneway flag set (the command exits
	   immediately after), which tells the service not to generate a reply.

	   Added in version 255.

       --json=MODE
	   Selects the JSON output formatting, one of "pretty" (for nicely indented, colorized output) or "short" (for terse output with minimal whitespace
	   and no newlines), defaults to "short".

	   Added in version 255.

       -j
	   Equivalent to --json=pretty when invoked interactively from a terminal. Otherwise equivalent to --json=short, in particular when the output is
	   piped to some other program.

	   Added in version 255.

       --no-pager
	   Do not pipe output into a pager.

       -h, --help
	   Print a short help text and exit.

       --version
	   Print a short version string and exit.

EXAMPLES
       Example 1. Investigating a Service

       The following three commands inspect the "io.systemd.Resolve" service implemented by systemd-resolved.service(8), listing general service information
       and implemented interfaces, and then displaying the interface definition of its primary interface:

	   $ varlinkctl info /run/systemd/resolve/io.systemd.Resolve
	       Vendor: The systemd Project
	      Product: systemd (systemd-resolved)
	      Version: 254 (254-1522-g4790521^)
		  URL: https://systemd.io/
	   Interfaces: io.systemd
		       io.systemd.Resolve
		       org.varlink.service
	   $ varlinkctl list-interfaces /run/systemd/resolve/io.systemd.Resolve
	   io.systemd
	   io.systemd.Resolve
	   org.varlink.service
	   $ varlinkctl introspect /run/systemd/resolve/io.systemd.Resolve io.systemd.Resolve
	   interface io.systemd.Resolve
	   type ResolvedAddress(
		   ifindex: ?int,
		   ...

       (Interface definition has been truncated in the example above, in the interest of brevity.)

       Example 2. Invoking a Method

       The following command resolves a hostname via systemd-resolved.service(8)'s ResolveHostname method call.

	   $ varlinkctl call /run/systemd/resolve/io.systemd.Resolve io.systemd.Resolve.ResolveHostname '{"name":"systemd.io","family":2}' -j
	   {
		   "addresses" : [
			   {
				   "ifindex" : 2,
				   "family" : 2,
				   "address" : [
					   185,
					   199,
					   111,
					   153
				   ]
			   }
		   ],
		   "name" : "systemd.io",
		   "flags" : 1048577
	   }

       Example 3. Investigating a Service Executable

       The following command inspects the /usr/lib/systemd/systemd-pcrextend executable and the IPC APIs it provides. It then invokes a method on it:

	   # varlinkctl info /usr/lib/systemd/systemd-pcrextend
	       Vendor: The systemd Project
	      Product: systemd (systemd-pcrextend)
	      Version: 254 (254-1536-g97734fb)
		  URL: https://systemd.io/
	   Interfaces: io.systemd
		       io.systemd.PCRExtend
		       org.varlink.service
	   # varlinkctl introspect /usr/lib/systemd/systemd-pcrextend io.systemd.PCRExtend
	   interface io.systemd.PCRExtend

	   method Extend(
		   pcr: int,
		   text: ?string,
		   data: ?string
	   ) -> ()
	   # varlinkctl call /usr/lib/systemd/systemd-pcrextend io.systemd.PCRExtend.Extend '{"pcr":15,"text":"foobar"}'
	   {}

SEE ALSO
       busctl(1), Varlink[1]

NOTES
	1. Varlink
	   https://varlink.org/

systemd 255																	 VARLINKCTL(1)
