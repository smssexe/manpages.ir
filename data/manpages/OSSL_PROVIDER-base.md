OSSL_PROVIDER-BASE(7SSL)						    OpenSSL						      OSSL_PROVIDER-BASE(7SSL)

NAME
       OSSL_PROVIDER-base - OpenSSL base provider

DESCRIPTION
       The OpenSSL base provider supplies the encoding for OpenSSL's asymmetric cryptography.

   Properties
       The implementations in this provider specifically have this property defined:

       "provider=base"

       It may be used in a property query string with fetching functions.

       It isn't mandatory to query for this property, except to make sure to get implementations of this provider and none other.

       "type=parameters"
       "type=private"
       "type=public"

       These  may  be  used  in	 a property query string with fetching functions to select which data are to be encoded.  Either the private key material, the
       public key material or the domain parameters can be selected.

       "format=der"
       "format=pem"
       "format=text"

       These may be used in a property query string with fetching functions to select the encoding output format.  Either  the	DER,  PEM  and	plaintext  are
       currently permitted.

OPERATIONS AND ALGORITHMS
       The OpenSSL base provider supports these operations and algorithms:

   Asymmetric Key Encoder
       In addition to "provider=base", some of these encoders define the property "fips=yes", to allow them to be used together with the FIPS provider.

       RSA, see OSSL_ENCODER-RSA(7)
       DH, see OSSL_ENCODER-DH(7)
       DSA, see OSSL_ENCODER-DSA(7)
       EC, see OSSL_ENCODER-EC(7)
       X25519, see OSSL_ENCODER-X25519(7)
       X448, see OSSL_ENCODER-X448(7)

SEE ALSO
       OSSL_PROVIDER-default(7), openssl-core.h(7), openssl-core_dispatch.h(7), provider(7)

HISTORY
       This functionality was added in OpenSSL 3.0.

COPYRIGHT
       Copyright 2020 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05						      OSSL_PROVIDER-BASE(7SSL)
