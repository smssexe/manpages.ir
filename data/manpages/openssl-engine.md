OPENSSL-ENGINE(1SSL)							    OpenSSL							  OPENSSL-ENGINE(1SSL)

NAME
       openssl-engine - load and query engines

SYNOPSIS
       openssl engine [-help] [-v] [-vv] [-vvv] [-vvvv] [-c] [-t] [-tt] [-pre command] ...  [-post command] ...	 [engine ...]

DESCRIPTION
       This command has been deprecated.  Providers should be used instead of engines.

       This command is used to query the status and capabilities of the specified engines.  Engines may be specified before and after all other command-line
       flags.  Only those specified are queried.

OPTIONS
       -help
	   Display an option summary.

       -v -vv -vvv -vvvv
	   Provides information about each specified engine. The first flag lists all the possible run-time control commands; the second adds a description of
	   each command; the third adds the input flags, and the final option adds the internal input flags.

       -c  Lists the capabilities of each engine.

       -t  Tests if each specified engine is available, and displays the answer.

       -tt Displays an error trace for any unavailable engine.

       -pre command
       -post command
	   Command-line configuration of engines.  The -pre command is given to the engine before it is loaded and the -post command is given after the engine
	   is loaded.  The command is of the form cmd:val where cmd is the command, and val is the value for the command.  See the example below.

	   These two options are cumulative, so they may be given more than once in the same command.

EXAMPLES
       To list all the commands available to a dynamic engine:

	$ openssl engine -t -tt -vvvv dynamic
	(dynamic) Dynamic engine loading support
	     [ unavailable ]
	     SO_PATH: Specifies the path to the new ENGINE shared library
		  (input flags): STRING
	     NO_VCHECK: Specifies to continue even if version checking fails (boolean)
		  (input flags): NUMERIC
	     ID: Specifies an ENGINE id name for loading
		  (input flags): STRING
	     LIST_ADD: Whether to add a loaded ENGINE to the internal list (0=no,1=yes,2=mandatory)
		  (input flags): NUMERIC
	     DIR_LOAD: Specifies whether to load from 'DIR_ADD' directories (0=no,1=yes,2=mandatory)
		  (input flags): NUMERIC
	     DIR_ADD: Adds a directory from which ENGINEs can be loaded
		  (input flags): STRING
	     LOAD: Load up the ENGINE specified by other settings
		  (input flags): NO_INPUT

       To list the capabilities of the rsax engine:

	$ openssl engine -c
	(rsax) RSAX engine support
	 [RSA]
	(dynamic) Dynamic engine loading support

ENVIRONMENT
       OPENSSL_ENGINES
	   The path to the engines directory.

SEE ALSO
       openssl(1), config(5)

HISTORY
       This command was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2016-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							  OPENSSL-ENGINE(1SSL)
