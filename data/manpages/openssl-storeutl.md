OPENSSL-STOREUTL(1SSL)							    OpenSSL							OPENSSL-STOREUTL(1SSL)

NAME
       openssl-storeutl - STORE command

SYNOPSIS
       openssl storeutl [-help] [-out file] [-noout] [-passin arg] [-text arg] [-r] [-certs] [-keys] [-crls] [-subject arg] [-issuer arg] [-serial arg]
       [-alias arg] [-fingerprint arg] [-digest] [-engine id] [-provider name] [-provider-path path] [-propquery propq] uri

DESCRIPTION
       This command can be used to display the contents (after decryption as the case may be) fetched from the given URI.

OPTIONS
       -help
	   Print out a usage message.

       -out filename
	   specifies the output filename to write to or standard output by default.

       -noout
	   this option prevents output of the PEM data.

       -passin arg
	   the key password source. For more information about the format of arg see openssl-passphrase-options(1).

       -text
	   Prints out the objects in text form, similarly to the -text output from openssl-x509(1), openssl-pkey(1), etc.

       -r  Fetch objects recursively when possible.

       -certs
       -keys
       -crls
	   Only select the certificates, keys or CRLs from the given URI.  However, if this URI would return a set of names (URIs), those are always returned.

	   Note that all options must be given before the uri argument.	 Otherwise they are ignored.

       -subject arg
	   Search for an object having the subject name arg.

	   The arg must be formatted as "/type0=value0/type1=value1/type2=...".	 Special characters may be escaped by "\" (backslash), whitespace is retained.
	   Empty  values  are permitted but are ignored for the search.	 That is, a search with an empty value will have the same effect as not specifying the
	   type at all.	 Giving a single "/" will lead to an empty sequence of RDNs (a NULL-DN).  Multi-valued RDNs can be formed by placing a	"+"  character
	   instead of a "/" between the AttributeValueAssertions (AVAs) that specify the members of the set.

	   Example:

	   "/DC=org/DC=OpenSSL/DC=users/UID=123456+CN=John Doe"

       -issuer arg
       -serial arg
	   Search for an object having the given issuer name and serial number.	 These two options must be used together.  The issuer arg must be formatted as
	   "/type0=value0/type1=value1/type2=...",  characters	may  be escaped by \ (backslash), no spaces are skipped.  The serial arg may be specified as a
	   decimal value or a hex value if preceded by "0x".

       -alias arg
	   Search for an object having the given alias.

       -fingerprint arg
	   Search for an object having the given fingerprint.

       -digest
	   The digest that was used to compute the fingerprint given with -fingerprint.

       -engine id
	   See "Engine Options" in openssl(1).	This option is deprecated.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

SEE ALSO
       openssl(1)

HISTORY
       This command was added in OpenSSL 1.1.1.

       The -engine option was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2016-2023 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in  the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							OPENSSL-STOREUTL(1SSL)
