OPENSSL-ENV(7SSL)							    OpenSSL							     OPENSSL-ENV(7SSL)

NAME
       openssl-env - OpenSSL environment variables

DESCRIPTION
       The OpenSSL libraries use environment variables to override the compiled-in default paths for various data.  To avoid security risks, the environment
       is usually not consulted when the executable is set-user-ID or set-group-ID.

       CTLOG_FILE
	   Specifies the path to a certificate transparency log list.  See CTLOG_STORE_new(3).

       OPENSSL
	   Specifies  the  path to the openssl executable. Used by the rehash script (see "Script Configuration" in openssl-rehash(1)) and by the CA.pl script
	   (see "NOTES" in CA.pl(1)

       OPENSSL_CONF, OPENSSL_CONF_INCLUDE
	   Specifies the path to a configuration file and the directory for included files.  See config(5).

       OPENSSL_CONFIG
	   Specifies a configuration option and filename for the req and ca commands invoked by the CA.pl script.  See CA.pl(1).

       OPENSSL_ENGINES
	   Specifies the directory from which dynamic engines are loaded.  See openssl-engine(1).

       OPENSSL_MALLOC_FD, OPENSSL_MALLOC_FAILURES
	   If built with debugging, this allows memory allocation to fail.  See OPENSSL_malloc(3).

       OPENSSL_MODULES
	   Specifies the directory from which cryptographic providers are loaded.  Equivalently, the generic -provider-path command-line option may be used.

       OPENSSL_WIN32_UTF8
	   If set, then UI_OpenSSL(3) returns UTF-8 encoded strings, rather than ones encoded in the current  code  page,  and	the  openssl(1)	 program  also
	   transcodes  the  command-line  parameters  from  the	 current  code	page to UTF-8.	This environment variable is only checked on Microsoft Windows
	   platforms.

       RANDFILE
	   The state file for the random number generator.  This should not be needed in normal use.  See RAND_load_file(3).

       SSL_CERT_DIR, SSL_CERT_FILE
	   Specify the default directory or file containing CA certificates.  See SSL_CTX_load_verify_locations(3).

       TSGET
	   Additional arguments for the tsget(1) command.

       OPENSSL_ia32cap, OPENSSL_sparcv9cap, OPENSSL_ppccap, OPENSSL_armcap, OPENSSL_s390xcap
	   OpenSSL supports a number of different algorithm implementations for various machines and, by default, it determines which  to  use	based  on  the
	   processor  capabilities  and	 run time feature enquiry.  These environment variables can be used to exert more control over this selection process.
	   See OPENSSL_ia32cap(3), OPENSSL_s390xcap(3).

       NO_PROXY, HTTPS_PROXY, HTTP_PROXY
	   Specify a proxy hostname.  See OSSL_HTTP_parse_url(3).

COPYRIGHT
       Copyright 2019-2021 The OpenSSL Project Authors. All Rights Reserved.

       Licensed under the Apache License 2.0 (the "License").  You may not use this file except in compliance with the License.	 You can obtain a copy in  the
       file LICENSE in the source distribution or at <https://www.openssl.org/source/license.html>.

3.0.13									  2025-02-05							     OPENSSL-ENV(7SSL)
