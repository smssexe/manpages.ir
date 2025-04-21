EVP_ASYM_CIPHER-RSA(7SSL)						    OpenSSL						     EVP_ASYM_CIPHER-RSA(7SSL)

NAME
       EVP_ASYM_CIPHER-RSA - RSA Asymmetric Cipher algorithm support

DESCRIPTION
       Asymmetric Cipher support for the RSA key type.

   RSA Asymmetric Cipher parameters
       "pad-mode" (OSSL_ASYM_CIPHER_PARAM_PAD_MODE) <UTF8 string>
	   The default provider understands these RSA padding modes in string form:

	   "none" (OSSL_PKEY_RSA_PAD_MODE_NONE)
	   "oaep" (OSSL_PKEY_RSA_PAD_MODE_OAEP)
	   "pkcs1" (OSSL_PKEY_RSA_PAD_MODE_PKCSV15)
	   "x931" (OSSL_PKEY_RSA_PAD_MODE_X931)
       "pad-mode" (OSSL_ASYM_CIPHER_PARAM_PAD_MODE) <integer>
	   The default provider understands these RSA padding modes in integer form:

	   1 (RSA_PKCS1_PADDING)
	   3 (RSA_NO_PADDING)
	   4 (RSA_PKCS1_OAEP_PADDING)
	   5 (RSA_X931_PADDING)

	   See EVP_PKEY_CTX_set_rsa_padding(3) for further details.

       "digest" (OSSL_ASYM_CIPHER_PARAM_OAEP_DIGEST) <UTF8 string>
       "digest-props" (OSSL_ASYM_CIPHER_PARAM_OAEP_DIGEST_PROPS) <UTF8 string>
       "mgf1-digest" (OSSL_ASYM_CIPHER_PARAM_MGF1_DIGEST) <UTF8 string>
       "mgf1-digest-props" (OSSL_ASYM_CIPHER_PARAM_MGF1_DIGEST_PROPS) <UTF8 string>
       "oaep-label" (OSSL_ASYM_CIPHER_PARAM_OAEP_LABEL) <octet string>
       "tls-client-version" (OSSL_ASYM_CIPHER_PARAM_TLS_CLIENT_VERSION) <unsigned integer>
	   See RSA_PKCS1_WITH_TLS_PADDING on the page EVP_PKEY_CTX_set_rsa_padding(3).

       "tls-negotiated-version" (OSSL_ASYM_CIPHER_PARAM_TLS_CLIENT_VERSION) <unsigned integer>
	   See RSA_PKCS1_WITH_TLS_PADDING on the page EVP_PKEY_CTX_set_rsa_padding(3).

	   See "Asymmetric Cipher Parameters" in provider-asym_cipher(7) for more information.

SEE ALSO
       EVP_PKEY-RSA(7), EVP_PKEY(3), provider-asym_cipher(7), provider-keymgmt(7), OSSL_PROVIDER-default(7) OSSL_PROVIDER-FIPS(7)

COPYRIGHT
       Copyright 2022 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05						     EVP_ASYM_CIPHER-RSA(7SSL)
