EVP_CIPHER-RC5(7SSL)							    OpenSSL							  EVP_CIPHER-RC5(7SSL)

NAME
       EVP_CIPHER-RC5 - The RC5 EVP_CIPHER implementations

DESCRIPTION
       Support for RC5 symmetric encryption using the EVP_CIPHER API.

       Disabled by default. Use the enable-rc5 configuration option to enable.

   Algorithm Names
       The following algorithms are available in the legacy provider:

       "RC5-CBC" or "RC5"
       "RC5-ECB"
       "RC5-OFB"
       "RC5-CFB"

   Parameters
       This implementation supports the parameters described in "PARAMETERS" in EVP_EncryptInit(3).

SEE ALSO
       provider-cipher(7), OSSL_PROVIDER-legacy(7)

COPYRIGHT
       Copyright 2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							  EVP_CIPHER-RC5(7SSL)
