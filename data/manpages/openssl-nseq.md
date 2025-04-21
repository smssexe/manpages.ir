OPENSSL-NSEQ(1SSL)							    OpenSSL							    OPENSSL-NSEQ(1SSL)

NAME
       openssl-nseq - create or examine a Netscape certificate sequence

SYNOPSIS
       openssl nseq [-help] [-in filename] [-out filename] [-toseq] [-provider name] [-provider-path path] [-propquery propq]

DESCRIPTION
       This command takes a file containing a Netscape certificate sequence and prints out the certificates contained in it or takes a file of certificates
       and converts it into a Netscape certificate sequence.

       A Netscape certificate sequence is an old Netscape-specific format that can be sometimes be sent to browsers as an alternative to the standard PKCS#7
       format when several certificates are sent to the browser, for example during certificate enrollment.  It was also used by Netscape certificate server.

OPTIONS
       -help
	   Print out a usage message.

       -in filename
	   This specifies the input filename to read or standard input if this option is not specified.

       -out filename
	   Specifies the output filename or standard output by default.

       -toseq
	   Normally  a Netscape certificate sequence will be input and the output is the certificates contained in it. With the -toseq option the situation is
	   reversed: a Netscape certificate sequence is created from a file of certificates.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

EXAMPLES
       Output the certificates in a Netscape certificate sequence

	openssl nseq -in nseq.pem -out certs.pem

       Create a Netscape certificate sequence

	openssl nseq -in certs.pem -toseq -out nseq.pem

COPYRIGHT
       Copyright 2000-2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in  the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							    OPENSSL-NSEQ(1SSL)
