OSSL_STORE-FILE(7SSL)							    OpenSSL							 OSSL_STORE-FILE(7SSL)

NAME
       ossl_store-file - The store 'file' scheme loader

SYNOPSIS
       #include <openssl/store.h>

DESCRIPTION
       Support for the 'file' scheme is built into "libcrypto".	 Since files come in all kinds of formats and content types, the 'file' scheme has its own
       layer of functionality called "file handlers", which are used to try to decode diverse types of file contents.

       In case a file is formatted as PEM, each called file handler receives the PEM name (everything following any '"-----BEGIN "') as well as possible PEM
       headers, together with the decoded PEM body.  Since PEM formatted files can contain more than one object, the file handlers are called upon for each
       such object.

       If the file isn't determined to be formatted as PEM, the content is loaded in raw form in its entirety and passed to the available file handlers as is,
       with no PEM name or headers.

       Each file handler is expected to handle PEM and non-PEM content as appropriate.	Some may refuse non-PEM content for the sake of determinism (for
       example, there are keys out in the wild that are represented as an ASN.1 OCTET STRING.  In raw form, it's not easily possible to distinguish those from
       any other data coming as an ASN.1 OCTET STRING, so such keys would naturally be accepted as PEM files only).

NOTES
       When needed, the 'file' scheme loader will require a pass phrase by using the UI_METHOD that was passed via OSSL_STORE_open().  This pass phrase is
       expected to be UTF-8 encoded, anything else will give an undefined result.  The files made accessible through this loader are expected to be standard
       compliant with regards to pass phrase encoding.	Files that aren't should be re-generated with a correctly encoded pass phrase.	See
       passphrase-encoding(7) for more information.

SEE ALSO
       ossl_store(7), passphrase-encoding(7)

COPYRIGHT
       Copyright 2018 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							 OSSL_STORE-FILE(7SSL)
