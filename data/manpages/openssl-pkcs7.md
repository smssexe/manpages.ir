OPENSSL-PKCS7(1SSL)							    OpenSSL							   OPENSSL-PKCS7(1SSL)

NAME
       openssl-pkcs7 - PKCS#7 command

SYNOPSIS
       openssl pkcs7 [-help] [-inform DER|PEM] [-outform DER|PEM] [-in filename] [-out filename] [-print] [-print_certs] [-text] [-noout] [-engine id]
       [-provider name] [-provider-path path] [-propquery propq]

DESCRIPTION
       This command processes PKCS#7 files.  Note that it only understands PKCS#7 v 1.5 as specified in IETF RFC 2315.	It cannot currently parse CMS as
       described in IETF RFC 2630.

OPTIONS
       -help
	   Print out a usage message.

       -inform DER|PEM, -outform DER|PEM
	   The input and formats; the default is PEM.  See openssl-format-options(1) for details.

	   The data is a PKCS#7 Version 1.5 structure.

       -in filename
	   This specifies the input filename to read from or standard input if this option is not specified.

       -out filename
	   Specifies the output filename to write to or standard output by default.

       -print
	   Print out the full PKCS7 object.

       -print_certs
	   Prints out any certificates or CRLs contained in the file. They are preceded by their subject and issuer names in one line format.

       -text
	   Prints out certificate details in full rather than just subject and issuer names.

       -noout
	   Don't output the encoded version of the PKCS#7 structure (or certificates if -print_certs is set).

       -engine id
	   See "Engine Options" in openssl(1).	This option is deprecated.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

EXAMPLES
       Convert a PKCS#7 file from PEM to DER:

	openssl pkcs7 -in file.pem -outform DER -out file.der

       Output all certificates in a file:

	openssl pkcs7 -in file.pem -print_certs -out certs.pem

SEE ALSO
       openssl(1), openssl-crl2pkcs7(1)

HISTORY
       The -engine option was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2000-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							   OPENSSL-PKCS7(1SSL)
