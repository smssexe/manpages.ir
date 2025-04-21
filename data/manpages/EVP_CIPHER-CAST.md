EVP_CIPHER-CAST(7SSL)							    OpenSSL							 EVP_CIPHER-CAST(7SSL)

NAME
       EVP_CIPHER-CAST - The CAST EVP_CIPHER implementations

DESCRIPTION
       Support for CAST symmetric encryption using the EVP_CIPHER API.

   Algorithm Names
       The following algorithms are available in the legacy provider:

       "CAST-128-CBC", "CAST-192-CBC" and  "CAST-256-CBC"
       "CAST-128-CFB", "CAST-192-CFB", "CAST-256-CFB"
       "CAST-128-ECB", "CAST-192-ECB" and "CAST-256-ECB"
       "CAST-192-OFB", "CAST-128-OFB" and "CAST-256-OFB"

   Parameters
       This implementation supports the parameters described in "PARAMETERS" in EVP_EncryptInit(3).

SEE ALSO
       provider-cipher(7), OSSL_PROVIDER-legacy(7)

COPYRIGHT
       Copyright 2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							 EVP_CIPHER-CAST(7SSL)
