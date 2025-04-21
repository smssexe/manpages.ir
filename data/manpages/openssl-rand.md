OPENSSL-RAND(1SSL)							    OpenSSL							    OPENSSL-RAND(1SSL)

NAME
       openssl-rand - generate pseudo-random bytes

SYNOPSIS
       openssl rand [-help] [-out file] [-base64] [-hex] [-engine id] [-rand files] [-writerand file] [-provider name] [-provider-path path] [-propquery
       propq] num

DESCRIPTION
       This command generates num random bytes using a cryptographically secure pseudo random number generator (CSPRNG).

       The random bytes are generated using the RAND_bytes(3) function, which provides a security level of 256 bits, provided it managed to seed itself
       successfully from a trusted operating system entropy source.  Otherwise, the command will fail with a nonzero error code.  For more details, see
       RAND_bytes(3), RAND(7), and EVP_RAND(7).

OPTIONS
       -help
	   Print out a usage message.

       -out file
	   Write to file instead of standard output.

       -base64
	   Perform base64 encoding on the output.

       -hex
	   Show the output as a hex string.

       -engine id
	   See "Engine Options" in openssl(1).	This option is deprecated.

       -rand files, -writerand file
	   See "Random State Options" in openssl(1) for details.

       -provider name
       -provider-path path
       -propquery propq
	   See "Provider Options" in openssl(1), provider(7), and property(7).

SEE ALSO
       openssl(1), RAND_bytes(3), RAND(7), EVP_RAND(7)

HISTORY
       The -engine option was deprecated in OpenSSL 3.0.

COPYRIGHT
       Copyright 2000-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							    OPENSSL-RAND(1SSL)
