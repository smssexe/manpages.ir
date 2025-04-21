EVP_MD-RIPEMD160(7SSL)							    OpenSSL							EVP_MD-RIPEMD160(7SSL)

NAME
       EVP_MD-RIPEMD160 - The RIPEMD160 EVP_MD implementation

DESCRIPTION
       Support for computing RIPEMD160 digests through the EVP_MD API.

   Identities
       This implementation is available in both the default and legacy providers, and is identified with any of the names "RIPEMD-160", "RIPEMD160", "RIPEMD"
       and "RMD160".

   Gettable Parameters
       This implementation supports the common gettable parameters described in EVP_MD-common(7).

SEE ALSO
       provider-digest(7), OSSL_PROVIDER-default(7)

HISTORY
       This digest was added to the default provider in OpenSSL 3.0.7.

COPYRIGHT
       Copyright 2020-2022 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							EVP_MD-RIPEMD160(7SSL)
