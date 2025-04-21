EVP_MD-BLAKE2(7SSL)							    OpenSSL							   EVP_MD-BLAKE2(7SSL)

NAME
       EVP_MD-BLAKE2 - The BLAKE2 EVP_MD implementation

DESCRIPTION
       Support for computing BLAKE2 digests through the EVP_MD API.

   Identities
       This implementation is only available with the default provider, and includes the following varieties:

       BLAKE2S-256
	   Known names are "BLAKE2S-256" and "BLAKE2s256".

       BLAKE2B-512
	   Known names are "BLAKE2B-512" and "BLAKE2b512".

   Gettable Parameters
       This implementation supports the common gettable parameters described in EVP_MD-common(7).

SEE ALSO
       provider-digest(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2020-2022 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							   EVP_MD-BLAKE2(7SSL)
