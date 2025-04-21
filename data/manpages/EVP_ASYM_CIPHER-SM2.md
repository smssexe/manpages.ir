EVP_ASYM_CIPHER-SM2(7SSL)						    OpenSSL						     EVP_ASYM_CIPHER-SM2(7SSL)

NAME
       EVP_ASYM_CIPHER-SM2 - SM2 Asymmetric Cipher algorithm support

DESCRIPTION
       Asymmetric Cipher support for the SM2 key type.

   SM2 Asymmetric Cipher parameters
       "digest" (OSSL_ASYM_CIPHER_PARAM_DIGEST) <UTF8 string>
       "digest-props" (OSSL_ASYM_CIPHER_PARAM_DIGEST_PROPS) <UTF8 string>
	   See "Asymmetric Cipher Parameters" in provider-asym_cipher(7).

SEE ALSO
       EVP_PKEY-SM2(7), EVP_PKEY(3), provider-asym_cipher(7), provider-keymgmt(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05						     EVP_ASYM_CIPHER-SM2(7SSL)
