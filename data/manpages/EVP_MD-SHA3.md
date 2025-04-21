EVP_MD-SHA3(7SSL)							    OpenSSL							     EVP_MD-SHA3(7SSL)

NAME
       EVP_MD-SHA3 - The SHA3 EVP_MD implementations

DESCRIPTION
       Support for computing SHA3 digests through the EVP_MD API.

   Identities
       This implementation is available with the FIPS provider as well as the default provider, and includes the following varieties:

       "SHA3-224"
       "SHA3-256"
       "SHA3-384"
       "SHA3-512"

   Gettable Parameters
       This implementation supports the common gettable parameters described in EVP_MD-common(7).

SEE ALSO
       provider-digest(7), OSSL_PROVIDER-FIPS(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							     EVP_MD-SHA3(7SSL)
