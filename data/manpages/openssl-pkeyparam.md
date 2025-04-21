OPENSSL-PKEYPARAM(1SSL)							    OpenSSL						       OPENSSL-PKEYPARAM(1SSL)

NAME
       openssl-pkeyparam - public key algorithm parameter processing command

SYNOPSIS
       openssl pkeyparam [-help] [-in filename] [-out filename] [-text] [-noout] [-check] [-engine id] [-provider name] [-provider-path path] [-propquery
       propq]

DESCRIPTION
       This command processes public key algorithm parameters.	They can be checked for correctness and their components printed out.

OPTIONS
       -help
	   Print out a usage message.

       -in filename
	   This specifies the input filename to read parameters from or standard input if this option is not specified.

       -out filename
	   This specifies the output filename to write parameters to or standard output if this option is not specified.

       -text
	   Prints out the parameters in plain text in addition to the encoded version.

       -noout
	   Do not output the encoded version of the parameters.

       -check
	   This option checks the correctness of parameters.

       -engine id
	   See "Engine Options" in openssl(1).	This option is deprecated.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

EXAMPLES
       Print out text version of parameters:

	openssl pkeyparam -in param.pem -text

NOTES
       There are no -inform or -outform options for this command because only PEM format is supported because the key type is determined by the PEM headers.

SEE ALSO
       openssl(1), openssl-genpkey(1), openssl-rsa(1), openssl-pkcs8(1), openssl-dsa(1), openssl-genrsa(1), openssl-gendsa(1)

HISTORY
       The -engine option was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2006-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05						       OPENSSL-PKEYPARAM(1SSL)
