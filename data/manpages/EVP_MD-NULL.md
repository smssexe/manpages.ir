EVP_MD-NULL(7SSL)							    OpenSSL							     EVP_MD-NULL(7SSL)

NAME
       EVP_MD-NULL - The NULL EVP_MD implementation

DESCRIPTION
       Support for a NULL digest through the EVP_MD API.  This algorithm does nothing and returns 1 for its init, update and final methods.

   Algorithm Name
       The following algorithm is available in the default provider:

       "NULL"

   Gettable Parameters
       This implementation supports the common gettable parameters described in EVP_MD-common(7).

SEE ALSO
       EVP_MD_CTX_set_params(3), provider-digest(7), OSSL_PROVIDER-default(7)

COPYRIGHT
       Copyright 2023 The OpenSSL Project Authors. All Rights Reserved.

       Licensed	 under the Apache License 2.0 (the "License").	You may not use this file except in compliance with the License.  You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							     EVP_MD-NULL(7SSL)
