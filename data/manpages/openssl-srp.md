OPENSSL-SRP(1SSL)							    OpenSSL							     OPENSSL-SRP(1SSL)

NAME
       openssl-srp - maintain SRP password file

SYNOPSIS
       openssl srp [-help] [-verbose] [-add] [-modify] [-delete] [-list] [-name section] [-srpvfile file] [-gn identifier] [-userinfo text] [-passin arg]
       [-passout arg] [-engine id] [-rand files] [-writerand file] [-provider name] [-provider-path path] [-propquery propq] [-config configfile] [user ...]

DESCRIPTION
       This command is deprecated. It is used to maintain an SRP (secure remote password) file. At most one of the -add, -modify, -delete, and -list options
       can be specified.  These options take zero or more usernames as parameters and perform the appropriate operation on the SRP file.  For -list, if no
       user is given then all users are displayed.

       The configuration file to use, and the section within the file, can be specified with the -config and -name flags, respectively.

OPTIONS
       -help
	   Display an option summary.

       -verbose
	   Generate verbose output while processing.

       -add
	   Add a user and SRP verifier.

       -modify
	   Modify the SRP verifier of an existing user.

       -delete
	   Delete user from verifier file.

       -list
	   List users.

       -name
	   The particular SRP definition to use.

       -srpvfile file
	   If the config file is not specified, -srpvfile can be used to specify the file to operate on.

       -gn Specifies the g and N values, using one of the strengths defined in IETF RFC 5054.

       -userinfo
	   specifies additional information to add when adding or modifying a user.

       -passin arg, -passout arg
	   The password source for the input and output file.  For more information about the format of arg see openssl-passphrase-options(1).

       -engine id
	   See "Engine Options" in openssl(1).	This option is deprecated.

       -rand files, -writerand file
	   See "Random State Options" in openssl(1) for details.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

       -config configfile
	   See "Configuration Option" in openssl(1).

	   [-rand files] [-writerand file]

HISTORY
       The -engine option was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2017-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							     OPENSSL-SRP(1SSL)
