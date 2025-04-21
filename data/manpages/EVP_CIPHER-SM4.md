EVP_CIPHER-SM4(7SSL)							    OpenSSL							  EVP_CIPHER-SM4(7SSL)

NAME
       EVP_CIPHER-SM4 - The SM4 EVP_CIPHER implementations

DESCRIPTION
       Support for SM4 symmetric encryption using the EVP_CIPHER API.

   Algorithm Names
       The following algorithms are available in the default provider:

       "SM4-CBC:SM4"
       "SM4-ECB"
       "SM4-CTR"
       "SM4-OFB" or "SM4-OFB128"
       "SM4-CFB" or "SM4-CFB128"

   Parameters
       This implementation supports the parameters described in "PARAMETERS" in EVP_EncryptInit(3).

SEE ALSO
       provider-cipher(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							  EVP_CIPHER-SM4(7SSL)
