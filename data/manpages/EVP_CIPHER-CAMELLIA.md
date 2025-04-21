EVP_CIPHER-CAMELLIA(7SSL)						    OpenSSL						     EVP_CIPHER-CAMELLIA(7SSL)

NAME
       EVP_CIPHER-CAMELLIA - The CAMELLIA EVP_CIPHER implementations

DESCRIPTION
       Support for CAMELLIA symmetric encryption using the EVP_CIPHER API.

   Algorithm Names
       The following algorithms are available in the default provider:

       "CAMELLIA-128-CBC", "CAMELLIA-192-CBC" and  "CAMELLIA-256-CBC"
       "CAMELLIA-128-CBC-CTS", "CAMELLIA-192-CBC-CTS" and "CAMELLIA-256-CBC-CTS"
       "CAMELLIA-128-CFB", "CAMELLIA-192-CFB", "CAMELLIA-256-CFB", "CAMELLIA-128-CFB1", "CAMELLIA-192-CFB1", "CAMELLIA-256-CFB1", "CAMELLIA-128-CFB8",
       "CAMELLIA-192-CFB8" and "CAMELLIA-256-CFB8"
       "CAMELLIA-128-CTR", "CAMELLIA-192-CTR" and "CAMELLIA-256-CTR"
       "CAMELLIA-128-ECB", "CAMELLIA-192-ECB" and "CAMELLIA-256-ECB"
       "CAMELLIA-192-OFB", "CAMELLIA-128-OFB" and "CAMELLIA-256-OFB"

   Parameters
       This implementation supports the parameters described in "PARAMETERS" in EVP_EncryptInit(3).

SEE ALSO
       provider-cipher(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05						     EVP_CIPHER-CAMELLIA(7SSL)
