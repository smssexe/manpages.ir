OPENSSL-CRL(1SSL)							    OpenSSL							     OPENSSL-CRL(1SSL)

NAME
       openssl-crl - CRL command

SYNOPSIS
       openssl crl [-help] [-inform DER|PEM] [-outform DER|PEM] [-key filename] [-keyform DER|PEM|P12] [-dateopt] [-text] [-in filename] [-out filename]
       [-gendelta filename] [-badsig] [-verify] [-noout] [-hash] [-hash_old] [-fingerprint] [-crlnumber] [-issuer] [-lastupdate] [-nextupdate] [-nameopt
       option] [-CAfile file] [-no-CAfile] [-CApath dir] [-no-CApath] [-CAstore uri] [-no-CAstore] [-provider name] [-provider-path path] [-propquery propq]

DESCRIPTION
       This command processes CRL files in DER or PEM format.

OPTIONS
       -help
	   Print out a usage message.

       -inform DER|PEM
	   The CRL input format; unspecified by default.  See openssl-format-options(1) for details.

       -outform DER|PEM
	   The CRL output format; the default is PEM.  See openssl-format-options(1) for details.

       -key filename
	   The private key to be used to sign the CRL.

       -keyform DER|PEM|P12
	   The format of the private key file; unspecified by default.	See openssl-format-options(1) for details.

       -in filename
	   This specifies the input filename to read from or standard input if this option is not specified.

       -out filename
	   Specifies the output filename to write to or standard output by default.

       -gendelta filename
	   Output a comparison of the main CRL and the one specified here.

       -badsig
	   Corrupt the signature before writing it; this can be useful for testing.

       -dateopt
	   Specify the date output format. Values are: rfc_822 and iso_8601.  Defaults to rfc_822.

       -text
	   Print out the CRL in text form.

       -verify
	   Verify the signature in the CRL.

       -noout
	   Don't output the encoded version of the CRL.

       -fingerprint
	   Output the fingerprint of the CRL.

       -crlnumber
	   Output the number of the CRL.

       -hash
	   Output a hash of the issuer name. This can be use to lookup CRLs in a directory by issuer name.

       -hash_old
	   Outputs the "hash" of the CRL issuer name using the older algorithm as used by OpenSSL before version 1.0.0.

       -issuer
	   Output the issuer name.

       -lastupdate
	   Output the lastUpdate field.

       -nextupdate
	   Output the nextUpdate field.

       -nameopt option
	   This specifies how the subject or issuer names are displayed.  See openssl-namedisplay-options(1) for details.

       -CAfile file, -no-CAfile, -CApath dir, -no-CApath, -CAstore uri, -no-CAstore
	   See "Trusted Certificate Options" in openssl-verification-options(1) for details.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

EXAMPLES
       Convert a CRL file from PEM to DER:

	openssl crl -in crl.pem -outform DER -out crl.der

       Output the text form of a DER encoded certificate:

	openssl crl -in crl.der -text -noout

BUGS
       Ideally it should be possible to create a CRL using appropriate options and files too.

SEE ALSO
       openssl(1), openssl-crl2pkcs7(1), openssl-ca(1), openssl-x509(1), ossl_store-file(7)

COPYRIGHT
       Copyright 2000-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							     OPENSSL-CRL(1SSL)
